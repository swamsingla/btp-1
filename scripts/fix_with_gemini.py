#!/usr/bin/env python3
"""
Hand a generated page to Gemini with its sources and ask for a corrected copy
=============================================================================
A cross-model check. This is NOT the same experiment as the Sarvam second pass, which
measured ~40% recall: that was *intrinsic* self-correction -- the same model re-reading
its own work -- and Huang et al. (ICLR 2024, "Large Language Models Cannot Self-Correct
Reasoning Yet") report the same ceiling. A different model reading the page cold does not
share the author model's blind spot, and it is the only thing tried so far that reaches
the class nothing else can: an invented explanation, a false statement, a worked example
built on the wrong numbers.

What it is given, and why
-------------------------
- The page, in full.
- The exact source extracts the page was written from, rebuilt with bc.build(), so the
  fixer can tell "unsupported" from "wrong". Without them it would have to judge from its
  own memory, which is how pages get "corrected" into disagreeing with NCERT.
- The two-tier rule, so it does not strip the model's own worked examples for being
  untagged.
- The page-shape rules, so the reply is still publishable: same headings, tags kept,
  Key points kept.

Deliberately NOT given: permission to rewrite. The instruction is to correct and return,
leaving everything it cannot fault alone, because a free rewrite makes the diff unreadable
and loses the hand-checked parts of the page.

Usage
-----
  python scripts/fix_with_gemini.py --list
  python scripts/fix_with_gemini.py --concept bayes-theorem --subject maths --grade 12
  python scripts/fix_with_gemini.py --from-file pages.txt
  python scripts/fix_with_gemini.py --concept X --subject maths --grade 12 --dry-run
"""

import argparse
import http.client
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_context as bc  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

BASE = pathlib.Path(__file__).resolve().parent.parent
AUDIT = BASE / "data" / "intermediate" / "generated_tagged"
PAGES = BASE / "data" / "generated_pages"
HELD = BASE / "data" / "intermediate" / "generated_held"
OUT = BASE / "data" / "intermediate" / "gemini_fixed"

# Free tier has no Pro access (Pro went behind a paywall on 2026-04-01 and returns 429
# on this key), so the best reachable model is the newest Flash. Checked 2026-10-08:
# every Flash variant correctly identified the r^2 "square inside the diameter" fault.
DEFAULT_MODEL = "gemini-3.8-flash"
ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent?key={k}"
STREAMS = ("maths", "biology", "chemistry", "physics")


def api_key() -> str:
    env = BASE / ".env"
    for line in env.read_text(encoding="utf-8").splitlines():
        if line.startswith("GEMINI_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("GEMINI_API_KEY is not in .env")


def find_page(slug: str, grade: int) -> tuple[pathlib.Path, pathlib.Path, str]:
    """(tagged copy, published-or-held copy, stream). The tagged copy is the one to fix:
    it still carries the [S#] tags, and those are what make the page checkable."""
    for stream in STREAMS:
        tagged = AUDIT / stream / f"grade{grade}" / f"{slug}.md"
        if not tagged.exists():
            continue
        for d in (PAGES, HELD):
            reader = d / stream / f"grade{grade}" / f"{slug}.md"
            if reader.exists():
                return tagged, reader, stream
        return tagged, tagged, stream
    raise SystemExit(f"no tagged page for {slug} grade {grade}")


def render_fix_prompt(page: str, ctx: dict) -> str:
    sources = []
    for a in ctx["anchors"]:
        sources.append(f"[{a['ref']}] Grade {a['grade']} {a['subject']}, {a['chapter']}, "
                       f"\"{a['section']}\"\n{a['text'].strip()}")
    return "\n".join([
        f"You are checking one page of a school textbook website for a Grade "
        f"{ctx['grade']} student. The topic is {ctx['name']} ({ctx['stream']}).",
        "",
        "Find everything that is WRONG with the page and return a corrected copy of the "
        "WHOLE page.",
        "",
        "=" * 70,
        "THE ONLY SOURCES THIS PAGE MAY USE",
        "=" * 70,
        "These are the extracts the page was written from. A factual claim is allowed "
        "only if these extracts support it. If the page states a fact these extracts do "
        "not support, that is a fault EVEN IF the fact is true, because the page cannot "
        "be checked against anything else. If the page contradicts these extracts, the "
        "extracts win.",
        "",
        *sources,
        "",
        "=" * 70,
        "WHAT COUNTS AS A FAULT",
        "=" * 70,
        "  1. A wrong number, or a worked example that uses the wrong quantities. Work "
        "every calculation out yourself; do not read along and agree. Check that the "
        "numbers plugged in are the ones the question actually gives.",
        "  2. A false statement, or an explanation of WHY something is true that the "
        "extracts do not support. An invented reason is the worst fault here.",
        "  3. A reference to something the reader cannot see: \"Example 12\", "
        "\"Theorem 1\", \"Table 5.1\", \"Fig 1.2\", \"Eq. (7.3)\", \"the extracts\", "
        "\"as we saw earlier\", a \\tag{...} equation number, or a geometric setup that "
        "names points from a figure that is not on the page. The page is all the reader "
        "gets. Rewrite these so they stand alone, or remove them.",
        "  4. A heading that promises something the section does not deliver, a section "
        "that repeats another, or a stub section of one or two sentences.",
        "  5. A Key point that states something the body never covers.",
        "  6. LaTeX that will not render: unbalanced braces, a command missing its "
        "argument.",
        "  7. The page drifting off its own topic.",
        "",
        "=" * 70,
        "WHAT IS NOT A FAULT -- DO NOT 'FIX' THESE",
        "=" * 70,
        "  - A sentence with no [S#] tag that is framing, an analogy, or the page's own "
        "worked example. Only factual claims need a source. Untagged does not mean wrong.",
        "  - The page's own invented example using its own numbers, as long as the "
        "numbers are right and the method matches a rule the extracts state.",
        "  - British spelling, or Indian number words and currency.",
        "",
        "=" * 70,
        "HOW TO RETURN IT",
        "=" * 70,
        "  - Correct what is wrong and CHANGE NOTHING ELSE. This is a correction, not a "
        "rewrite.",
        "  - Keep every heading, in the same order, with the same wording, unless the "
        "heading itself is the fault.",
        "  - Keep the [S1], [S2] ... source tags exactly where they are, in Latin "
        "letters, and keep the <!-- TERMS: ... --> line at the end exactly as it is if "
        "the page has one.",
        "  - Keep a Key points section. If the page has none, add one with 3-5 bullets "
        "drawn from the page's own content.",
        "  - Return ONLY the page, starting directly with its # heading. No preamble, no "
        "list of what you changed, no notes, no code fence.",
        "",
        "=" * 70,
        "THE PAGE",
        "=" * 70,
        "",
        page.strip(),
    ])


# Flash models go in and out of "high demand" (HTTP 503) through the day, and the newest
# is the most contended. Checked 2026-10-08: 3.8 and 3.7 both 503'd at times while 3.6,
# 3.5, 3-flash-preview and flash-latest answered. All of them correctly spotted the r^2
# "square inside the diameter" fault, so dropping down a version costs little; losing the
# whole run to one overloaded model costs a lot.
FALLBACK_MODELS = ["gemini-3.8-flash", "gemini-3.6-flash", "gemini-3.5-flash",
                   "gemini-flash-latest", "gemini-3-flash-preview"]


def call_gemini(prompt: str, model: str, key: str, retries: int = 4) -> tuple[str, dict]:
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        # Zero temperature: this is a correction task, and a different answer on every
        # run makes the result impossible to audit.
        #
        # maxOutputTokens has to be large because THINKING TOKENS COUNT AGAINST IT. At
        # 16000 the first run billed 22,174 tokens for a 832-word reply: roughly 17,000
        # went on deliberation, the budget ran out, and the page came back truncated
        # mid-sentence at "## Worked Example\n\nConsider" -- losing its Associativity
        # section, its Key points and its TERMS line. It looked like aggressive editing
        # and was nothing of the kind. The same trap bit this project once before, with
        # Sarvam's reasoning_effort returning empty pages after ~1,500 words of thinking.
        "generationConfig": {"temperature": 0, "maxOutputTokens": 65536},
    }
    body = json.dumps(payload).encode()
    last = ""
    for attempt in range(retries):
        req = urllib.request.Request(ENDPOINT.format(m=model, k=key), data=body,
                                     headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                d = json.loads(r.read())
            cand = (d.get("candidates") or [{}])[0]
            parts = (cand.get("content") or {}).get("parts") or []
            text = "".join(p.get("text", "") for p in parts).strip()
            finish = cand.get("finishReason")
            if not text:
                last = f"empty reply, finishReason={finish}"
            elif finish not in (None, "STOP"):
                # A truncated page is worse than no page: it silently loses its last
                # sections and reads as a confident edit. Refuse it.
                last = f"finishReason={finish} (reply truncated, {len(text.split())} words)"
            else:
                usage = d.get("usageMetadata", {})
                usage["finishReason"] = finish
                return text, usage
        except urllib.error.HTTPError as e:
            raw = e.read().decode("utf-8", "replace")
            last = f"HTTP {e.code}: {raw[:160]}"
            # 429 is the free tier's per-minute limit; 503 is transient load. Both are
            # worth waiting out rather than failing the page.
            if e.code in (429, 503):
                time.sleep(20 * (attempt + 1))
                continue
        # OSError covers ConnectionResetError, and http.client.HTTPException covers
        # RemoteDisconnected / BadStatusLine, which are NOT subclasses of URLError. The
        # first version caught only URLError and a RemoteDisconnected at page 15 killed a
        # 30-page run outright. Catch broadly: a dropped connection is a retry, never a
        # reason to abandon the batch.
        except (urllib.error.URLError, OSError, http.client.HTTPException,
                TimeoutError, ValueError) as e:
            last = f"{type(e).__name__}: {e}"
        time.sleep(5 * (attempt + 1))
    # Returning rather than raising: one overloaded model must not destroy a 30-page run.
    # The first version of this raised SystemExit and a single 503 on page 2 aborted the
    # whole batch after one page had been fixed.
    return "", {"error": last}


def call_with_fallback(prompt: str, models: list[str], key: str) -> tuple[str, dict, str]:
    """Try each model in turn; return the first real answer and which model gave it."""
    last = ""
    for m in models:
        reply, usage = call_gemini(prompt, m, key, retries=2)
        if reply:
            return reply, usage, m
        last = str(usage.get("error", ""))[:90]
        print(f"[{m} unavailable] ", end="", flush=True)
    return "", {"error": last}, ""


def strip_fence(text: str) -> str:
    """Models wrap replies in ``` even when told not to."""
    t = text.strip()
    if t.startswith("```"):
        t = re.sub(r"^```[a-zA-Z]*\s*\n", "", t)
        t = re.sub(r"\n```\s*$", "", t)
    return t.strip()


def return_trip_faults(before: str, after: str) -> list[str]:
    """What the reply LOST relative to the page it was asked to correct.

    The whole risk of handing a page over for correction is the return trip, and the
    first run demonstrated it: the reply dropped a whole section, the Key points and the
    <!-- TERMS: --> line, and the word count made it look like tightening. A reply that
    loses structure is not a corrected page, whatever else it fixed, so it is reported
    rather than silently published. The TERMS line matters beyond this page -- it is what
    pins terminology for the Hindi, Telugu and Odia versions.
    """
    faults = []
    heads_before = re.findall(r"^##\s+(.+)$", before, flags=re.M)
    heads_after = re.findall(r"^##\s+(.+)$", after, flags=re.M)
    lost = [h for h in heads_before if h not in heads_after]
    if lost:
        faults.append(f"lost section(s): {', '.join(h[:34] for h in lost[:4])}")
    if "TERMS:" in before and "TERMS:" not in after:
        faults.append("lost the <!-- TERMS: --> line (breaks localisation)")
    if not re.search(r"^##\s*key points", after, flags=re.M | re.I):
        faults.append("no Key points section")
    tags_before = len(re.findall(r"\[[^\]]*?S\s*\d[^\]]*\]", before))
    tags_after = len(re.findall(r"\[[^\]]*?S\s*\d[^\]]*\]", after))
    if tags_before and tags_after < tags_before * 0.7:
        faults.append(f"lost source tags: {tags_after}/{tags_before}")
    if len(after.split()) < 0.6 * len(before.split()):
        faults.append(f"shrank to {len(after.split())}/{len(before.split())} words")
    # A tag alone on its own line is a corruption, not a citation.
    if re.search(r"^\s*\[S\s*\d+\s*\]\s*$", after, flags=re.M):
        faults.append("a source tag is stranded on its own line")
    return faults


def main() -> None:
    ap = argparse.ArgumentParser(description="Ask Gemini to correct a generated page")
    ap.add_argument("--concept")
    ap.add_argument("--subject", choices=["maths", "science"])
    ap.add_argument("--grade", type=int)
    ap.add_argument("--from-file", type=pathlib.Path,
                    help="lines of 'subject slug grade'")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--resume", action="store_true",
                    help="skip any page that already has an .after.md")
    ap.add_argument("--no-fallback", dest="fallback", action="store_false",
                    help="do not drop to an older Flash model on HTTP 503")
    ap.add_argument("--dry-run", action="store_true", help="print the prompt, send nothing")
    ap.add_argument("--list", action="store_true", help="list available models")
    args = ap.parse_args()

    key = api_key()

    if args.list:
        url = f"https://generativelanguage.googleapis.com/v1beta/models?key={key}"
        with urllib.request.urlopen(url, timeout=60) as r:
            data = json.loads(r.read())
        for m in data.get("models", []):
            if "generateContent" in m.get("supportedGenerationMethods", []):
                print("  ", m["name"].replace("models/", ""))
        return

    jobs: list[tuple[str, str, int]] = []
    if args.from_file:
        for line in args.from_file.read_text(encoding="utf-8").splitlines():
            line = line.strip().replace("\r", "")
            if not line or line.startswith("#"):
                continue
            subj, slug, grade = line.split()
            jobs.append((subj, slug, int(grade)))
    elif args.concept:
        if not (args.subject and args.grade):
            raise SystemExit("--concept needs --subject and --grade")
        jobs.append((args.subject, args.concept, args.grade))
    else:
        raise SystemExit("give --concept ... or --from-file ... or --list")

    graphs, passages, evidence = bc.load()
    levels = bc.level_profile(passages)
    OUT.mkdir(parents=True, exist_ok=True)
    total_tokens = 0
    skipped: list[str] = []
    damaged: list[str] = []

    for subj, slug, grade in jobs:
        tagged, reader, stream = find_page(slug, grade)
        ctx = bc.build(subj, slug, grade, graphs, passages, evidence, levels)
        out_dir = OUT / stream / f"grade{grade}"
        if args.resume and (out_dir / f"{slug}.after.md").exists():
            print(f"  {stream}/{slug} gr{grade} -- already fixed, skipped")
            continue
        page = tagged.read_text(encoding="utf-8")
        prompt = render_fix_prompt(page, ctx)

        if args.dry_run:
            print(prompt)
            print(f"\n--- prompt is {len(prompt.split())} words, page "
                  f"{len(page.split())} words, {len(ctx['anchors'])} sources")
            continue

        print(f"  {stream}/{slug} gr{grade} ... ", end="", flush=True)
        models = ([args.model] + [m for m in FALLBACK_MODELS if m != args.model]
                  if args.fallback else [args.model])
        reply, usage, used = call_with_fallback(prompt, models, key)
        if not reply:
            print(f"SKIPPED — all models failed ({usage.get('error', '')})")
            skipped.append(slug)
            continue
        reply = strip_fence(reply)
        tok = usage.get("totalTokenCount", 0)
        total_tokens += tok

        d = OUT / stream / f"grade{grade}"
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{slug}.before.md").write_text(page, encoding="utf-8")
        (d / f"{slug}.after.md").write_text(reply + "\n", encoding="utf-8")
        same = page.strip() == reply.strip()
        rt = return_trip_faults(page, reply)
        print(f"{len(page.split())} -> {len(reply.split())} words, "
              f"{'UNCHANGED' if same else 'edited'}, {tok} tokens, {used}")
        if rt:
            damaged.append(slug)
            for f in rt:
                print(f"       RETURN-TRIP DAMAGE: {f}")
        time.sleep(7)        # free tier is ~10 requests per minute

    if total_tokens:
        print(f"\n{len(jobs)} page(s), {total_tokens} tokens total")
        print(f"before/after pairs in {OUT.relative_to(BASE).as_posix()}")
    if skipped:
        print(f"{len(skipped)} page(s) skipped, every model unavailable: "
              f"{', '.join(skipped)}")
    if damaged:
        print(f"{len(damaged)} reply/replies came back DAMAGED (structure lost) and "
              f"must not be published as-is: {', '.join(damaged)}")


if __name__ == "__main__":
    main()
