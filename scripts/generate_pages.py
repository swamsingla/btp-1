#!/usr/bin/env python3
"""
Generate page content from the assembled prompts
=================================================
Sends the prompts built by build_context.py to Sarvam and saves each page with the
exact sources it was written from, so a claim can always be traced back.

Nothing is sent unless --send is given: without it this writes the prompts to disk
so they can be read first. Textbook extracts leave the machine on --send, which is
the point, but it should be a deliberate act.

Start small. A handful of pages across grades and subjects answers the question the
cluster spend depends on — does a grounded prompt produce a grounded page — and
costs almost nothing:

  python scripts/generate_pages.py --sample 12                  # write prompts only
  python scripts/generate_pages.py --sample 12 --send           # actually generate
  python scripts/generate_pages.py --concept solar-eclipse --grade 7 --send
  python scripts/generate_pages.py --all --send                 # the full run

Output: data/generated_pages/{subject}/grade{N}/{slug}.md, each with front matter
recording the model, the anchors used and whether its citations check out.

Configuration comes from .env (see .env.example):
  SARVAM_API_KEY    required for --send
  SARVAM_MODEL      default sarvam-105b
  SARVAM_BASE_URL   default https://api.sarvam.ai/v1
  SARVAM_MAX_TOKENS         default 3500 — covers reasoning AND the page
  SARVAM_REASONING_EFFORT   default none — low/medium/high to turn thinking back on
  SARVAM_TEMPERATURE        default 0.3
Verify the endpoint and model name against Sarvam's current docs before a big run —
they are configurable here precisely because they change.
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    # On Windows stdout defaults to cp1252, which cannot encode Devanagari, Telugu or
    # Odia. That is fatal, not cosmetic: this script prints the first fault line when it
    # retries a page, those lines quote the term at fault, and a quoted Hindi term killed
    # a 63-page localisation run mid-page with UnicodeEncodeError. Replace rather than
    # raise -- a progress line is worth less than the run.
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_context as bc  # noqa: E402
import check_arithmetic as arith  # noqa: E402
import check_grounding as grounding  # noqa: E402  (torch is imported lazily inside)
from check_pages import structural_problems  # noqa: E402
from check_translations import localisation_problems  # noqa: E402

BASE = Path(__file__).resolve().parent.parent
OUT_DIR = BASE / "data" / "generated_pages"
AUDIT_DIR = BASE / "data" / "intermediate" / "generated_tagged"
# A page that failed every retry used to be published anyway, with its own frontmatter
# recording the failure. The first Grade 6 maths run put 29 pages under the word floor and
# 10 pages citing nothing into data/generated_pages, which is the one thing the project
# claims cannot happen. Failures now land here instead: the paid output is kept, and the
# published corpus only contains pages that passed.
HELD_DIR = BASE / "data" / "intermediate" / "generated_held"
PROMPT_DIR = BASE / "data" / "intermediate" / "prompts"
# What the verification pass said about each page, kept so a verdict can be read back
# later. The verdicts are NOT applied — see the gate in main() for why — but they are the
# only record of why a page was generated three times.
VERIFY_DIR = BASE / "data" / "intermediate" / "verification"

# A bracket group containing a source tag: [S1], [S1][S2], [S1, S2], [S1 and S2].
CITATION = re.compile(r"\s*\[[^\]]*?S\s*\d[^\]]*\]")

DEFAULT_BASE_URL = "https://api.sarvam.ai/v1"
# sarvam-m was retired in 2026; the API names the current models in its
# 400 response, so a stale default surfaces immediately rather than silently.
DEFAULT_MODEL = "sarvam-105b"
RETRIES = 3
# Attempts at one English page, shared by every gate it has to clear. Four, because the
# faults are stochastic slips rather than things the model cannot do — a page it miscounts
# on one run it usually gets right on the next — and because each attempt is a full page's
# worth of tokens.
MAX_PAGE_TRIES = 4
# ...except that the arithmetic gate gets at least this many looks whatever else happens.
# The gates are run cheapest first, so an attempt rejected for citations or length never
# reaches the arithmetic check at all. The first Grade 7 page spent three of its four
# attempts on tagging and was published on the strength of ONE arithmetic look, which is
# the gate this whole stage exists for. Two looks because a single `fail` carries a real
# false-alarm rate (4 of 8 hand-verified pages), so one flag is not evidence enough to
# spend another page on, but a fault that survives a regeneration usually is.
MIN_MATHS_CHECKS = 2
# Absolute stop, so no single page can cost unboundedly when both gates keep failing.
HARD_PAGE_CEILING = 6
# Attempts a short page is worth before its length is recorded rather than enforced.
# Measured on the first Grade 7 run: area-of-circle was asked six times and returned 362,
# 483, 494 and 501 words against a 900 floor. The length a topic draws out of the model is
# stable, so four further attempts bought 139 words for ten paid calls — and the arithmetic
# gate, which is the whole point of this stage, never ran once because length kept failing
# first. Length is real but it is the least of the three faults: a thin page that is correct
# and traceable still serves a reader, whereas a withheld page serves nobody. So after two
# tries it is recorded on the page and the remaining budget goes to the arithmetic check.
LENGTH_TRIES = 2
# A verification verdict longer than this is treated as no opinion rather than a fault.
# Measured over the first 7 Grade 7 verdicts, the split is total: at 787, 1,551, 1,594 and
# 2,389 tokens all four were coherent and two were genuine catches, while at 9,245, 9,370
# and 9,690 tokens all three were confabulated false `fail`s — one reused a token count
# from an earlier section to "correct" a 5x3 example to 10, another ended every bullet with
# "so no arithmetic fault" and still returned fail, a third contradicted itself inside one
# sentence. It is the same failure as reasoning_effort: past a few thousand tokens the model
# is spiralling rather than checking, and its output stops tracking the page. Acting on
# those three cost two paid page-generations each for a flag with no precision at all.
VERDICT_TOKEN_LIMIT = 5000


def load_env() -> dict[str, str]:
    env = {}
    path = BASE / ".env"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    return {**env, **os.environ}


def call_sarvam(prompt: str, env: dict[str, str]) -> str:
    key = env.get("SARVAM_API_KEY")
    if not key or key.startswith("your_"):
        raise SystemExit(
            "SARVAM_API_KEY is not set in .env — add it, or drop --send to write "
            "prompts only."
        )
    url = env.get("SARVAM_BASE_URL", DEFAULT_BASE_URL).rstrip("/") + "/chat/completions"
    payload = {
        "model": env.get("SARVAM_MODEL", DEFAULT_MODEL),
        "messages": [{"role": "user", "content": prompt}],
        "temperature": float(env.get("SARVAM_TEMPERATURE", 0.3)),
        # Reasoning tokens are billed and count against max_tokens, so this has to leave
        # room for both. With max_tokens=800 the model spent the entire budget thinking
        # about the words "Say OK." and returned an empty message.
        "max_tokens": int(env.get("SARVAM_MAX_TOKENS", 8000)),
    }
    # sarvam-105b deliberates before answering. The deliberation for this task was already
    # done when the prompt was assembled — which extracts, what shape, what length — so it
    # is paid-for tokens spent re-deciding settled questions. Set SARVAM_REASONING_EFFORT
    # to low/medium/high to turn it back on and compare.
    # It has to be sent explicitly as null. Leaving the field out is not the same thing:
    # the API then applies its own default of "medium" and reasons anyway, which is how
    # two pages came back empty after ~1,500 words of deliberation each.
    effort = env.get("SARVAM_REASONING_EFFORT", "none").strip().lower()
    payload["reasoning_effort"] = None if effort in ("none", "off", "") else effort
    body = json.dumps(payload).encode()

    last = None
    for attempt in range(RETRIES):
        req = urllib.request.Request(url, data=body, headers={
            "Content-Type": "application/json",
            "api-subscription-key": key,
            "Authorization": f"Bearer {key}",
        })
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                data = json.loads(resp.read())
            choice = data["choices"][0]
            content = choice["message"].get("content")
            if content:
                return content, data.get("usage", {})
            # An empty message with finish_reason "length" means the budget went on
            # reasoning and none was left to answer with — say so plainly rather than
            # failing on a None further down.
            thought = len((choice["message"].get("reasoning_content") or "").split())
            raise SystemExit(
                f"Sarvam returned an empty page (finish_reason="
                f"{choice.get('finish_reason')}, ~{thought} words of reasoning). "
                f"Raise SARVAM_MAX_TOKENS or set SARVAM_REASONING_EFFORT=none in .env."
            )
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")[:300]
            last = f"HTTP {e.code}: {detail}"
            if e.code not in (429, 500, 502, 503, 504):
                raise SystemExit(f"Sarvam rejected the request — {last}")
        except Exception as e:                                  # noqa: BLE001
            last = f"{type(e).__name__}: {e}"
        time.sleep(2 ** attempt)
    raise SystemExit(f"Sarvam call failed after {RETRIES} attempts — {last}")


# Sections the page is allowed to write without citations: the opening framing, the
# model's own worked example and the forward link are all Tier B by design.
TIER_B_HEADINGS = re.compile(r"^#{1,3}\s*(worked example|what comes next|key points)",
                             re.IGNORECASE | re.MULTILINE)


# A later-grade page that repeats the earlier grade's page has failed at the one thing it
# exists for. Measured as the share of its words that sit in sentences found word for word
# on the earlier page. Calibrated on the 14 concepts Grades 6 and 7 share: the eight Grade
# 7 pages that had copied their Grade 6 page scored 0.32-1.00, the six that had not scored
# 0.00-0.12, and no two different Grade 6 maths concepts scored above 0.06.
MAX_REPEATED = 0.25


def repeated_from(page: str, earlier: str) -> float:
    def sentences(text: str) -> list[str]:
        out = []
        for line in bc.strip_terms(CITATION.sub("", text)).splitlines():
            line = re.sub(r"^\s*(#+|[-*])\s*", "", line)
            for sentence in re.split(r"(?<=[.!?])\s+", line):
                words = re.findall(r"[a-z0-9]+", sentence.lower())
                if len(words) >= 6:          # shorter ones recur by chance
                    out.append(" ".join(words))
        return out

    mine, theirs = sentences(page), set(sentences(earlier))
    total = sum(len(x.split()) for x in mine)
    return sum(len(x.split()) for x in mine if x in theirs) / max(total, 1)


def check_citations(page: str, ctx: dict, reference: str | None = None) -> dict:
    """Do the citations point at sources this page was actually given?

    Not a quality score — that comes later. This catches the one failure that makes
    grounding worthless: a page citing [S7] when it was handed four sources.

    Uncited paragraphs are counted but do NOT fail the page. Under the two-tier rules
    the opening, the analogies and the model's own worked example are supposed to carry
    no citation, and an earlier version of this check failed both test pages for exactly
    that — the page was right and the checker was wrong.
    """
    # Citations arrive as [S1], [S1][S2] and [S1, S2]. Matching only the first form
    # silently found zero citations on a page full of "[S1, S2]" and failed it.
    refs = {n for group in re.findall(r"\[([^\]]*?S\s*\d[^\]]*)\]", page)
            for n in re.findall(r"S\s*(\d+)", group)}
    given = {a["ref"][1:] for a in ctx["anchors"]}
    invented = refs - given

    # Count uncited prose only in the part of the page before the Tier B sections, and
    # skip everything before the first ## heading: the opening paragraph is framing, which
    # the rules explicitly say needs no tag. Counting it made every page look guilty.
    body = TIER_B_HEADINGS.split(page)[0]
    after_opening = re.split(r"^##\s", body, maxsplit=1, flags=re.MULTILINE)
    body = after_opening[1] if len(after_opening) > 1 else body
    uncited = [p for p in body.split("\n\n")
               if len(p.split()) > 25 and "[S" not in p and not p.lstrip().startswith("#")]

    # Untraceable SECTIONS, not untraceable paragraphs. The paragraph count above is kept
    # because it is useful to see, but it cannot decide whether a page is grounded, and
    # using it that way contradicted both this function's own docstring and the prompt.
    # The prompt asks for "a worked example of your own, using your own numbers ... for
    # EVERY rule or idea you state", and the two-tier rules say such an example carries no
    # tag. A page with four topic sections, each pairing a sourced rule with its own
    # example, therefore has four untagged paragraphs while being perfectly traceable --
    # and 18 of the 38 Grade 6 maths pages were failed on exactly that. What actually
    # matters is whether each part of the page can be traced back to something: a section
    # with a tagged rule and an untagged example is fine, a section with no tag anywhere
    # is not. One such section is allowed, for a page that opens with framing under a
    # heading of its own.
    topic_sections = re.split(r"^##\s+", body, flags=re.MULTILINE)
    untraceable = [s for s in topic_sections
                   if len(s.split()) > 40 and "[S" not in s]
    out = {
        "cited": sorted(refs, key=int),
        "invented_citations": sorted(invented, key=int),
        "unused_sources": sorted(given - refs, key=int),
        "explanatory_paragraphs_without_a_citation": len(uncited),
        "words": len(page.split()),
        "target_words": ctx["plan"]["target_words"],
        # How MANY of the offered sources were used does not matter — a page honestly
        # built on one extract is fine. What matters is whether its claims can be traced,
        # so the test is untagged explanatory paragraphs, allowing one for an analogy.
        "untraceable_sections": len(untraceable),
        "ok": not invented and bool(refs) and len(untraceable) <= 1,
    }
    if reference is not None:
        # A localised page is a copy of the English one, so counting its untagged
        # paragraphs measures nothing: TIER_B_HEADINGS only matches English headings, so
        # on a Hindi page the Key points list and worked example — untagged by design —
        # get counted as failures. What matters here is whether the tags survived the
        # translation, so compare against the page it was written from.
        theirs = len(re.findall(r"\[[^\]]*?S\s*\d[^\]]*\]", reference))
        mine = len(re.findall(r"\[[^\]]*?S\s*\d[^\]]*\]", page))
        out["tags_vs_english"] = f"{mine}/{theirs}"
        out["explanatory_paragraphs_without_a_citation"] = 0
        out["ok"] = not invented and (theirs == 0 or mine >= theirs * 0.7)
    return out


def verify_maths(page: str, env: dict[str, str]) -> dict:
    """Hand the finished page back to the model and ask it to recompute every number.

    Every other check in this file is structural: it can tell that a page cites nothing,
    repeats itself or runs short, and none of it notices a tally of 20 answers reported as
    20+7+8+2, or 360/7 given as 52 6/7, or a bag of 15 negative numbers worked out as
    5 x (-3). Those are the faults that actually reach a student, and the only thing that
    catches them without a human reading every page is a second call that recomputes the
    arithmetic with no memory of having written it.

    A TRIGGER, and nothing else. The verdict is never used to EDIT the page, because its
    reasoning is unreliable even when its flag is right: measured over 18 Grade 6 pages it
    caught 8 of 10 real faults, but on one it "corrected" a factorisation by asserting
    2x2x2x3x3x5 = 720, and on another it flagged the right page for the wrong reason. The
    flag carries information; the explanation does not. Applying the explanations would
    write fresh errors over real ones, which is what the repair stage did with provenance.

    It is not allowed to hold a page back either. On 8 pages verified correct by hand it
    returned 4 `fail`s, of which only 1-2 were genuine false alarms — a noise floor too
    high to publish on, since gating publication would withhold good pages on a coin-flip.
    """
    # Check what a reader sees. The source tags are scaffolding, and bracketed tags
    # mid-sentence are noise to something being asked to add up the numbers in front of it.
    reader = bc.strip_terms(CITATION.sub("", page)).strip()
    said, usage = call_sarvam(bc.render_verify(reader), env)
    # The reply form asked for is "VERDICT: fail" then one line per fault. The template's
    # own placeholder bullets come back verbatim often enough to be the first line of a
    # verdict, which makes a run log unreadable, so skip them and take the first line that
    # says something.
    bullets = [ln.strip() for ln in said.splitlines() if ln.strip().startswith("-")
               and "what the page says" not in ln and "one line per fault" not in ln]
    spent = usage.get("total_tokens", 0)
    verdict = "fail" if "VERDICT: fail" in said else (
        "ok" if "VERDICT: ok" in said else "unparsed")
    # A long verdict is the model spiralling, not checking — see VERDICT_TOKEN_LIMIT. Kept
    # under its own name, with the full text still saved, so the call can be audited and
    # this decision reversed on more evidence rather than silently swallowed.
    if verdict == "fail" and spent > VERDICT_TOKEN_LIMIT:
        verdict = "spiralled"
    return {
        "verdict": verdict,
        "first_fault": bullets[0] if bullets else "(no fault named)",
        "tokens": usage.get("total_tokens", 0),
        "said": said.strip(),
    }


def fix_page(page: str, env: dict[str, str]) -> tuple[str, dict]:
    """Hand the page back for correction and return what comes back, plus what it cost.

    The counterpart to verify_maths and a different bet. verify_maths asks "is this
    right?" and a `fail` throws the page away and rolls a new one, which is why a page
    correct everywhere but one sum gets re-rolled wholesale; this asks for the page back
    with the wrong parts put right, and publishes the reply.

    No judgement is parsed, so there is nothing here to be fooled by: the measured
    problem with the verdict shape was that long deliberations confabulated faults and
    short `ok`s missed real ones. This shape cannot produce either. What it can do
    instead is come back mangled -- tags dropped, sections merged, the page shortened to
    a summary -- so the reply is returned raw and the caller re-runs every check on it.
    """
    said, usage = call_sarvam(bc.render_fix(page), env)
    return said.strip(), usage


def main() -> None:
    ap = argparse.ArgumentParser(description="Generate pages from the assembled prompts")
    ap.add_argument("--concept")
    ap.add_argument("--grade", type=int)
    ap.add_argument("--subject", choices=list(bc.GRAPHS))
    ap.add_argument("--sample", type=int, help="N pages spread across grades and subjects")
    ap.add_argument("--all", action="store_true",
                    help="every generatable page, narrowed by --subject and --grade")
    ap.add_argument("--langs", default="en",
                    help="comma-separated language codes, or 'all' "
                         f"({', '.join(bc.LANGUAGES)}). Each is a separate call.")
    ap.add_argument("--send", action="store_true",
                    help="actually call Sarvam; without this only prompts are written")
    ap.add_argument("--min-source", type=int, metavar="WORDS",
                    help="override build_context.MIN_SOURCE_WORDS for this run, to see "
                         "what a concept with thin retrieved source actually produces. "
                         "Lowering it does not make the source cover the topic.")
    ap.add_argument("--once", action="store_true",
                    help="exactly ONE generation call per English page: no tag repair, "
                         "no structural retry, no verification pass. For runs whose "
                         "faults are going to be found and fixed by hand afterwards, "
                         "where a second model call only spends tokens on a page a "
                         "reader is going to correct anyway.")
    ap.add_argument("--fix-pass", action="store_true",
                    help="second pass CORRECTS the page instead of judging it: generate "
                         "once, hand the page back asking for anything wrong to be "
                         "fixed, publish what comes back. No regeneration loop.")
    ap.add_argument("--no-verify", action="store_true",
                    help="skip the arithmetic verification pass (on by default for "
                         "English pages; costs ~2k tokens a page, plus a regeneration "
                         "whenever it reports a fault)")
    ap.add_argument("--ground", action="store_true",
                    help="check every cited sentence against the passage it cites "
                         "(MiniCheck, local, no API cost) and regenerate a page that is "
                         "substantially ungrounded. Needs the python that has torch — on "
                         "Windows that is the CPython install, not msys2")
    ap.add_argument("--ground-threshold", type=float, default=0.5, metavar="P",
                    help="support probability below which a cited sentence counts as "
                         "unsupported (0.5; measured separation is 0.96+ vs under 0.04, "
                         "so the middle is empty and this is not a delicate choice)")
    ap.add_argument("--ground-max-unsupported", type=float, default=0.34, metavar="F",
                    help="fraction of a page's cited sentences that may be unsupported "
                         "before it is regenerated (0.34). Not zero: 19%% of Grade 6 "
                         "science citations failed, mostly over-tagged worked examples, "
                         "so a zero-tolerance gate would regenerate almost every page")
    ap.add_argument("--resume", action="store_true",
                    help="skip any page already written, published or held, instead of "
                         "paying for it again — use this to restart an interrupted run")
    args = ap.parse_args()

    langs = (list(bc.LANGUAGES) if args.langs == "all"
             else [x.strip() for x in args.langs.split(",") if x.strip()])
    unknown = [x for x in langs if x not in bc.LANGUAGES]
    if unknown:
        raise SystemExit(f"unknown language code(s) {unknown}; "
                         f"known: {', '.join(bc.LANGUAGES)}")

    env = load_env()
    graphs, passages, evidence = bc.load()
    levels = bc.level_profile(passages)
    if args.min_source:
        print(f"  MIN_SOURCE_WORDS {bc.MIN_SOURCE_WORDS} -> {args.min_source}")
        bc.MIN_SOURCE_WORDS = args.min_source

    targets: list[tuple[str, str, int]] = []
    if args.concept:
        subject = args.subject or next(
            (s for s in bc.GRAPHS if args.concept in graphs[s]["concepts"]), None)
        if subject is None:
            raise SystemExit(f"{args.concept} is in neither graph")
        # No --grade means every grade the concept is taught in. A concept that appears
        # in two grades needs both pages, and they should differ.
        grades = ([args.grade] if args.grade
                  else graphs[subject]["concepts"][args.concept]["grades"])
        targets = [(subject, args.concept, g) for g in grades]
    elif args.all or args.sample:
        targets = sorted(evidence)
        # --subject and --grade narrow --all too. Without this they were read only
        # alongside --concept, so a whole grade of one subject could not be asked for: the
        # choices were one concept at a time or every generatable pair in both graphs. The
        # natural guess, --all --subject maths --grade 6, silently accepted both flags and
        # ran all ~884 pages, which on a paid API is not a mistake worth leaving available.
        if args.subject:
            targets = [t for t in targets if t[0] == args.subject]
        if args.grade:
            targets = [t for t in targets if t[2] == args.grade]
        if not targets:
            raise SystemExit("no generatable pages match that --subject/--grade")
        if args.sample:
            # spread across (subject, grade) rather than taking the first N, which
            # would be one subject and one grade and would prove nothing
            by_slot: dict[tuple, list] = {}
            for t in targets:
                by_slot.setdefault((t[0], t[2]), []).append(t)
            spread, i = [], 0
            while len(spread) < args.sample and any(by_slot.values()):
                for slot in sorted(by_slot):
                    if by_slot[slot] and len(spread) < args.sample:
                        spread.append(by_slot[slot].pop(i % max(len(by_slot[slot]), 1)))
                i += 1
            targets = spread
    else:
        raise SystemExit("give --concept, --sample N or --all")

    # Never generate a page for a grade the graph does not place the concept in. The
    # evidence index is keyed by (subject, slug, grade) and holds an entry wherever usable
    # source could be found, which is not the same question as whether the concept belongs
    # to that grade. For Grade 6 maths that produced two pages nothing had asked for:
    # Euclidean Algorithm, which the graph places at Grade 10, and Ratios and Proportions,
    # which it places at Grade 7. Both then borrowed Grade 7 source and read at the wrong
    # level, and Ratios could not be grounded at all because the corpus has no ratio
    # section to cite. The graph's `grades` list is the authority on which pages exist.
    # A slug missing from the graph entirely is the same ruling, more strongly: the
    # concept does not exist, so no page does. It has to be handled rather than indexed
    # blindly, because the evidence index is built separately and outlives graph edits --
    # deleting sense-organs from the science graph, which has no source at any grade,
    # left an evidence entry behind and crashed this line with a KeyError.
    before = len(targets)
    targets = [(s, slug, gr) for s, slug, gr in targets
               if gr in graphs[s]["concepts"].get(slug, {}).get("grades", [])]
    if len(targets) < before:
        print(f"  skipping {before - len(targets)} page(s) for grades the graph does not "
              f"assign the concept to")

    PROMPT_DIR.mkdir(parents=True, exist_ok=True)
    written = skipped = failed = clean = unresolved = resumed = 0
    # English first, always: the other languages are written from the finished English
    # page so that every language has the same sections, facts and examples.
    ordered = (["en"] if "en" in langs else []) + [x for x in langs if x != "en"]

    for subject, slug, grade in targets:
        try:
            ctx = bc.build(subject, slug, grade, graphs, passages, evidence, levels)
        except SystemExit as e:
            print(f"  ERROR {slug} gr{grade}: {e}")
            failed += 1
            continue

        if not ctx["generate"]:
            reason = (f"no Grade {grade} text of its own: same extracts as its Grade "
                      f"{ctx['same_source_as']} page" if ctx.get("same_source_as")
                      else f"{len(ctx['anchors'])} sources")
            print(f"  skip  {ctx['name'][:38]:40} gr{grade}  ({reason})")
            skipped += 1
            continue

        english = None            # the tagged English page, once it exists
        for lang in ordered:
            # A 63-page run is one DNS blip away from dying half finished, and the Grade 6
            # science localisation did exactly that -- the connection dropped after 19
            # pages. Nothing downstream is idempotent, so a plain restart pays the full
            # token cost of every page already on disk. Held counts as done: a held page
            # failed a check, which a re-ask at this temperature is unlikely to fix, and
            # silently regenerating it would also destroy the evidence of what it failed.
            # English is skipped the same way -- the loop reads the tagged copy back from
            # AUDIT_DIR anyway, which is the hand-corrected spec and better than a fresh
            # draft.
            suffix = "" if lang == "en" else "." + lang
            if args.resume and any(
                    (d / ctx["stream"] / f"grade{grade}" / f"{slug}{suffix}.md").exists()
                    for d in (OUT_DIR, HELD_DIR)):
                resumed += 1
                continue
            if lang == "en":
                # When this concept is also taught at an earlier grade, hand that grade's
                # finished English page to the model so it extends it rather than
                # re-deriving the same definitions and examples (see the comment on
                # "prior_grade" in build_context.build). Read from the tagged copy, the
                # same convention as the localisation path below, since that is the
                # hand-corrected spec — but handed over with the tags and TERMS line
                # taken off: those tags number that page's extracts, not this one's.
                prior_page = None
                if ctx.get("prior_grade"):
                    prior_grade_path = (AUDIT_DIR / ctx["stream"]
                                         / f"grade{ctx['prior_grade']}" / f"{slug}.md")
                    if prior_grade_path.exists():
                        prior_page = bc.strip_terms(CITATION.sub(
                            "", prior_grade_path.read_text(encoding="utf-8")))
                prompt = bc.render(ctx, prior_page=prior_page)
            else:
                # The tagged copy is the spec, not the published one: carrying the tags
                # across is what lets the localised page be checked the same way.
                if english is None:
                    prior = AUDIT_DIR / ctx["stream"] / f"grade{grade}" / f"{slug}.md"
                    english = prior.read_text(encoding="utf-8") if prior.exists() else None
                if english is None:
                    print(f"  ERROR {ctx['name'][:30]} gr{grade} {lang}: no English page "
                          f"to work from — generate 'en' first, or add it to --langs")
                    failed += 1
                    continue
                # Parsed from the English page itself, so it works whether English was
                # generated in this loop or read back from an earlier run.
                declared = bc.terms_in(english)
                prompt = bc.render_localised(ctx, english, lang)
            (PROMPT_DIR / f"{subject}_{slug}_g{grade}{'' if lang == 'en' else '.' + lang}.txt").write_text(prompt, encoding="utf-8")
            if not args.send:
                written += 1
                continue

            # For a localised page the yardstick is the English page it was written from,
            # not its own untagged-paragraph count: that count is meaningless in Hindi,
            # because TIER_B_HEADINGS only matches English headings and so the Key points
            # list and worked example — untagged by design — are counted as failures.
            spec = None if lang == "en" else english

            if lang == "en":
                floor, ceil = ctx["plan"]["target_words"]

                # Under-length counts as a fault: the model writes short stochastically —
                # the same Adjoint prompt produced 665 words one run and 1,145 the next —
                # so a thin page is usually worth one more ask rather than a lower target.
                def en_faults(p: str) -> list[str]:
                    f = structural_problems(p)
                    n = len(p.split())
                    if n < floor * 0.85:
                        f = f or [f"length: {n} words, under {floor}"]
                    # Over-length too, now that max_tokens is 8000 and no longer truncates
                    # a runaway into something that merely looks short.
                    elif n > ceil * 1.5:
                        f = [f"length: {n} words, far over {ceil}"] + f
                    # The instruction not to repeat the earlier grade's page is checked,
                    # not trusted: it was given once and ignored eight times out of eight.
                    if prior_page:
                        share = repeated_from(p, prior_page)
                        if share > MAX_REPEATED:
                            f = f + [f"repeats: {share:.0%} of this page is word for word "
                                     f"the Grade {ctx['prior_grade']} page"]
                    # Arithmetic worked out in Python, on every attempt, because it is
                    # free and -- unlike the model -- cannot be talked into agreeing with
                    # a wrong sum. This is the gate that catches 750 - 75 = 725, which
                    # survived the paid verification call. Measured on 184 published
                    # pages: one flag, and it was a real error. See check_arithmetic.py.
                    return f + arith.problems(p)

                # ONE flat retry loop over three gates, run cheapest first on every
                # attempt: are the claims traceable, is the page structurally sound, does
                # its arithmetic hold up.
                #
                # Flat on purpose. The gates were nested at first — citations, then
                # structure, then arithmetic, each with its own retries — and a page
                # regenerated by a later gate was never re-checked by the earlier ones.
                # The first Grade 7 page did exactly that: the arithmetic check correctly
                # caught a worked example computing 5 x (-3) = -15, the regeneration came
                # back with no source tags at all, and the page was held for citations
                # after three paid calls. A regeneration is a new page and has to face
                # every gate again, so the gates now share one loop and one budget.
                verdicts: list[dict] = []
                why: list[str] = []
                attempt = short_tries = 0
                while True:
                    attempt += 1
                    if attempt > 1:
                        print(f"        {why[0][:84]} — regenerating "
                              f"(attempt {attempt})")
                    # Generated at the top of every attempt, including the first. `page`
                    # outlives this loop — it is the variable the whole concept loop
                    # publishes from — so a first attempt that did not assign it would
                    # quietly check the PREVIOUS concept's page and publish it twice.
                    page, usage = call_sarvam(prompt, env)
                    report = check_citations(page, ctx)

                    # Repair rather than regenerate, where it fits: adding the missing
                    # tags to a finished page is a narrower task than writing the page
                    # again, and it leaves the arithmetic of an otherwise sound page
                    # alone instead of re-rolling it.
                    if not report["ok"] and ctx["anchors"] and not args.once:
                        print("        untraceable — asking for the tags to be added")
                        repaired, rusage = call_sarvam(bc.render_repair(ctx, page), env)
                        fixed = check_citations(repaired, ctx)
                        # keep the repair only if it helped and kept the page intact
                        if fixed["ok"] and 0.6 < len(repaired.split()) / max(len(page.split()), 1) < 1.4:
                            page, report, usage = repaired, fixed, rusage

                    faults = en_faults(page)
                    short = [f for f in faults if f.startswith("length:")]
                    short_tries += bool(short)
                    # Length stops blocking once it has had LENGTH_TRIES goes — see the
                    # constant. Dropped from structural_problems, not just from `why`, or
                    # the page would be held at the end on a fault we have stopped acting
                    # on; recorded under "short" so the thinness is still on the page.
                    if short and short_tries > LENGTH_TRIES:
                        faults = [f for f in faults if not f.startswith("length:")]
                        report["short"] = short
                    report["structural_problems"] = faults
                    why = [] if report["ok"] else [
                        f"citations: {report['untraceable_sections']} untraceable "
                        f"section(s), {len(report['invented_citations'])} invented"]
                    why += report["structural_problems"]

                    # Grounding next: does each CITED sentence actually follow from the
                    # passage it cites? The citation gate above only checks that a tag
                    # exists. This is the gate that would have caught "polar bears ...
                    # during hibernation [S1]" if the source had not itself said it.
                    #
                    # Placed before the arithmetic gate because it costs no API tokens --
                    # MiniCheck runs locally -- so it is the cheaper of the two in money,
                    # if not in time. It can only judge TAGGED sentences: an untagged
                    # worked example or opening is untagged by design and is not its
                    # business. Needs the interpreter that has torch; see check_grounding.
                    if not why and args.ground:
                        gfaults, gdetail = grounding.grounding_problems(
                            page, ctx["anchors"], threshold=args.ground_threshold,
                            max_unsupported=args.ground_max_unsupported)
                        report["grounding"] = gdetail
                        if gfaults:
                            print(f"        {gfaults[0][:88]}")
                        why += gfaults

                    # Arithmetic last, and only on a page that would otherwise go out:
                    # it costs a call of its own, and a page already being regenerated
                    # for length does not need its sums checked first.
                    checked_maths = (not args.no_verify and not args.fix_pass
                                     and not args.once)
                    if not why and checked_maths:
                        verdicts.append(verify_maths(page, env))
                        # Only a readable `fail` costs a regeneration. "spiralled" and
                        # "unparsed" are the check failing, not the page.
                        if verdicts[-1]["verdict"] == "fail":
                            why = [f"maths: {verdicts[-1]['first_fault']}"]
                    if not why or args.once:
                        break
                    # Out of budget when the attempts are used up AND the arithmetic gate
                    # has had its look — whichever of those comes last — or at the ceiling.
                    enough = (attempt >= MAX_PAGE_TRIES
                              and (not checked_maths
                                   or len(verdicts) >= MIN_MATHS_CHECKS))
                    if enough or attempt >= HARD_PAGE_CEILING:
                        break

                if verdicts:
                    vdir = VERIFY_DIR / ctx["stream"] / f"grade{grade}"
                    vdir.mkdir(parents=True, exist_ok=True)
                    (vdir / f"{slug}.json").write_text(
                        json.dumps(verdicts, indent=2, ensure_ascii=False),
                        encoding="utf-8")
                    report["verification"] = {
                        "verdict": verdicts[-1]["verdict"],
                        "checks": len(verdicts),
                        "tokens": sum(v["tokens"] for v in verdicts),
                    }
                # The second shape of the second pass: hand the finished page back and
                # ask for anything wrong to be CORRECTED, then publish the reply. The
                # verdict shape above throws a page away on a `fail` and rolls a new one;
                # this one keeps the page and changes the wrong parts, so a page right
                # everywhere but one sum is not re-rolled wholesale.
                #
                # It runs on the page the loop settled on, not on a raw draft. The loop's
                # gates are free checks for faults the fix pass is not being asked about
                # — a missing Key points section, untagged claims — and without them a
                # structurally broken draft is simply lost, since nothing here regenerates.
                if args.fix_pass:
                    before = page
                    page, fusage = fix_page(page, env)
                    usage = fusage

                    # Re-checked on the REPLY, never on the draft: in this shape the reply
                    # is the page, and the one failure a verdict cannot have is coming
                    # back with the tags, the TERMS line or whole sections missing.
                    report = check_citations(page, ctx)
                    faults = en_faults(page)
                    short = [f for f in faults if f.startswith("length:")]
                    if short:
                        faults = [f for f in faults if not f.startswith("length:")]
                        report["short"] = short
                    report["structural_problems"] = faults

                    # Both versions kept. Without the draft there is no telling a page the
                    # fix pass corrected from one it never touched, which is the whole
                    # question this mode exists to answer.
                    fdir = VERIFY_DIR / ctx["stream"] / f"grade{grade}"
                    fdir.mkdir(parents=True, exist_ok=True)
                    (fdir / f"{slug}.draft.md").write_text(before, encoding="utf-8")
                    (fdir / f"{slug}.fixed.md").write_text(page, encoding="utf-8")
                    same = before.strip() == page.strip()
                    report["fix_pass"] = {
                        "draft_words": len(before.split()),
                        "fixed_words": len(page.split()),
                        "identical": same,
                        "tokens": fusage.get("total_tokens", 0),
                    }
                    print(f"        fix pass: {len(before.split())} -> "
                          f"{len(page.split())} words, "
                          f"{'unchanged' if same else 'EDITED'}, "
                          f"{fusage.get('total_tokens', 0)} tokens")

                english = page      # spec for the other languages
            else:
                page, usage = call_sarvam(prompt, env)
                report = check_citations(page, ctx, spec)
                # A localisation that dropped the English page's tags cannot be compared
                # with it at all, and compliance is stochastic at this temperature, so
                # ask again rather than accept it.
                if not report["ok"] and ctx["anchors"]:
                    print(f"        tags {report.get('tags_vs_english')} — retrying {lang}")
                    page, usage = call_sarvam(prompt, env)
                    report = check_citations(page, ctx, spec)
                # Until this existed, a localised page was published on ONE test -- that
                # its source tags survived. Sections, numbers, formulas and the pinned
                # terminology were checked only by a human running check_translations.py
                # afterwards, which is how an Odia page saying ରିଫ୍ରାକ୍ସନ୍ (the English word
                # in Odia letters) reached data/generated_pages. The English page is the
                # spec, so a localisation that disagrees with it is wrong by definition and
                # worth one more ask.
                spec_clean = bc.strip_terms(english)

                # Bracketing the declared terms is how build_glossary.py harvests a
                # rendering, so it matters — but it is not something a READER can be harmed
                # by. A page that uses the pinned term correctly and simply does not repeat
                # the English word in brackets is accurate and complete, so withholding it
                # punishes the reader for a gap in our tooling. Over the first 30 Grade 6
                # localisations, brackets alone accounted for 8 of the 11 held pages while
                # their source tags and parity were perfect (32/32 and 59/59 tags). Parity
                # and the pinned terminology still block publication; a missing bracket is
                # retried once and then recorded as `not_harvestable` and allowed through.
                # `glossary:` joins brackets as advisory, 2026-10-09, on the user's
                # instruction: "same word can be used in many diff contexts". A pin is a
                # plain substring test against the ENGLISH term, so it fires on senses it
                # was never meant for -- the maths pin for "even" on the adverb in "or even
                # 10 students", "product" on a foodstuff in components-of-food, "normal" on
                # body temperature in a biology page judged against a geometry glossary.
                # It held 4 pages that were correct and bought 8 paid retries on the Grade 6
                # science run for cross-page consistency, a feature already dropped.
                # Still REPORTED, so a real terminology drift is visible to a reader of the
                # report; it simply no longer blocks a page or costs a call.
                ADVISORY = ("brackets:", "glossary:")

                def split_faults(fs: list[str]) -> tuple[list[str], list[str]]:
                    return ([f for f in fs if not f.startswith(ADVISORY)],
                            [f for f in fs if f.startswith(ADVISORY)])

                advisory: list[str] = []
                for _ in range(2):
                    faults, advisory = split_faults(
                        localisation_problems(page, spec_clean, lang, declared,
                                              ctx["stream"]))
                    # Only a BLOCKING fault is worth a paid call. A missing bracket is
                    # advisory -- it cannot hold the page -- yet retrying on it dominated
                    # the spend: 50 of 65 retries on the Grade 6 science run and 27 of 33
                    # on Grade 6 maths, where the credits ran out 17 concepts short. The
                    # brackets exist only so build_glossary.py can harvest a rendering for
                    # cross-page terminology, which is a feature the user has dropped, so
                    # those calls bought nothing. Brackets are still asked for in the
                    # prompt and still recorded as `not_harvestable`; they just no longer
                    # cost a regeneration.
                    if not faults:
                        break
                    print(f"        {faults[0][:88]} — retrying {lang}")
                    page, usage = call_sarvam(prompt, env)
                    report = check_citations(page, ctx, spec)
                faults, advisory = split_faults(
                    localisation_problems(page, spec_clean, lang, declared,
                                          ctx["stream"]))
                report["localisation_problems"] = faults
                if advisory:
                    report["not_harvestable"] = advisory
            passed = (report["ok"] and not report.get("structural_problems")
                      and not report.get("localisation_problems"))
            clean += passed

            # The tags are how the page is held to its sources, but they are scaffolding, not
            # something a student should read. Check against the tagged text, publish without
            # it, and keep the tagged copy so any sentence can still be traced later.
            audit = AUDIT_DIR / ctx["stream"] / f"grade{grade}"
            audit.mkdir(parents=True, exist_ok=True)
            (audit / f"{slug}{'' if lang == 'en' else '.' + lang}.md").write_text(page, encoding="utf-8")
            # The TERMS comment is scaffolding for the other languages, like the tags:
            # the audit copy above keeps it, nothing a reader sees does.
            page = bc.strip_terms(re.sub(r"\n{3,}", "\n\n", CITATION.sub("", page)).strip())

            out = (OUT_DIR if passed else HELD_DIR) / ctx["stream"] / f"grade{grade}"
            out.mkdir(parents=True, exist_ok=True)
            front = {
                "concept": ctx["name"], "slug": slug, "grade": grade,
                "language": lang, "subject": ctx["stream"], "area": ctx["area"],
                "model": env.get("SARVAM_MODEL", DEFAULT_MODEL),
                "settings": {
                    "temperature": float(env.get("SARVAM_TEMPERATURE", 0.3)),
                    "max_tokens": int(env.get("SARVAM_MAX_TOKENS", 8000)),
                    "reasoning_effort": env.get("SARVAM_REASONING_EFFORT", "none"),
                },
                "usage": usage,
                "target_words": ctx["plan"]["target_words"],
                "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "source_grade": ctx["source_grade"], "grade_delta": ctx["grade_delta"],
                "sources": [{"ref": a["ref"], "passage_id": a["passage_id"],
                             "chapter": a["chapter"], "section": a["section"]}
                            for a in ctx["anchors"]],
                "citation_check": report,
                "terms": bc.terms_in(english) if lang == "en" else declared,
            }
            (out / f"{slug}{'' if lang == 'en' else '.' + lang}.md").write_text(
                "---\n" + json.dumps(front, indent=2, ensure_ascii=False) + "\n---\n\n" + page,
                encoding="utf-8")
            if not passed:
                why = (report.get("structural_problems")
                       or report.get("localisation_problems") or ["citations"])
                print(f"        HELD (not published): {why[0][:70]}")
                # Localising a page that failed would spend three more calls copying a
                # known-bad page into three languages.
                if lang == "en":
                    break

            # Localisations are copies of the English page. Regenerating English alone
            # leaves them describing a page that no longer exists — stale content under
            # headings that have since changed.
            if lang == "en" and "en" in langs and len(langs) == 1:
                stale = sorted(p.name for p in out.glob(f"{slug}.??.md"))
                if stale:
                    print(f"        NOTE: {len(stale)} localisation(s) are now stale "
                          f"({', '.join(s.split('.')[-2] for s in stale)}) — rerun with "
                          f"--langs all")

            written += 1
            flag = "" if report["ok"] else "   <-- citation problem"
            v = report.get("verification")
            if v and v["verdict"] != "ok":
                flag += f"   <-- maths {v['verdict']} after {v['checks']} checks"
                unresolved += 1
            print(f"  wrote {ctx['name'][:38]:40} gr{grade}  "
                  f"{len(page.split())} words, cited {len(report['cited'])}"
                  f"/{len(ctx['anchors'])}{flag}")

    verb = "generated" if args.send else "prompts written"
    print(f"\n{written} {verb}, {skipped} skipped, {failed} errors")
    if resumed:
        print(f"{resumed} already on disk, skipped by --resume")
    if args.send and written:
        print(f"{clean}/{written} passed the citation check")
        if args.fix_pass:
            print(f"every page got one fix pass — drafts and fixed copies in "
                  f"{VERIFY_DIR.relative_to(BASE).as_posix()}")
        elif not args.no_verify:
            print(f"{unresolved}/{written} published with the arithmetic check still "
                  f"reporting a fault — verdicts in "
                  f"{VERIFY_DIR.relative_to(BASE).as_posix()}")
        print(f"pages in {OUT_DIR.relative_to(BASE).as_posix()}")
        if HELD_DIR.exists() and any(HELD_DIR.glob("**/*.md")):
            print(f"held back in {HELD_DIR.relative_to(BASE).as_posix()} — these failed "
                  f"their checks and were NOT published")
    else:
        print(f"prompts in {PROMPT_DIR.relative_to(BASE).as_posix()} — read a few, "
              f"then rerun with --send")


if __name__ == "__main__":
    main()
