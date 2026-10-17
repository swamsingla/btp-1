#!/usr/bin/env python3
"""
Does each cited sentence actually follow from the passage it cites?
==================================================================
The citation gate already in the pipeline checks that a claim is TAGGED. It has never
checked that the tag SUPPORTS the claim. That gap is why

    "the thick layer of fat under a polar bear's skin helps them survive for months
     without eating during hibernation [S1]"

was published: the tag was real, the passage said nothing about hibernation, and polar
bears do not hibernate. A false claim tags as [S1] exactly as happily as a true one.

This script closes that gap with MiniCheck (Tang et al., EMNLP 2024), a model trained for
one question -- "does this document support this sentence?" -- and reported to match GPT-4
on it at 770M parameters. It runs locally; no API, no credits.

What it does NOT do
-------------------
It cannot judge an UNTAGGED sentence. Under the two-tier rules the opening, the analogies
and the model's own worked example are supposed to carry no tag, so "unsupported" is the
correct state for them and flagging it would be meaningless. The invented-explanation
class therefore stays out of reach: the r^2 "area of a square that fits inside the
diameter" claim sat in an untagged paragraph with no source to check it against. The
mitigation for that is the prompt rule in build_context.render(), not this file.

Interpreter
-----------
Needs torch, which the msys2 python used for the rest of the pipeline cannot install
(platform tag mingw_x86_64_ucrt_gnu; PyPI ships win_amd64). Run it with the Windows
CPython that has torch:

  "$LOCALAPPDATA/Programs/Python/Python313/python.exe" scripts/check_grounding.py --all

Setup, once:
  pip install "minicheck @ git+https://github.com/Liyan06/MiniCheck.git@main"
  python -c "import nltk; nltk.download('punkt_tab')"

That second line is not optional and the installer does not do it: MiniCheck pulls nltk
and fetches `punkt`, but its sentence splitter asks for `punkt_tab`, so the first real run
dies with LookupError: Resource 'punkt_tab' not found after the model has already loaded.

Usage
-----
  python scripts/check_grounding.py --concept area-of-circle --subject maths --grade 7
  python scripts/check_grounding.py --all --grade 6 --subject science
  python scripts/check_grounding.py --all --json
"""

import argparse
import json
import os
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_context as bc  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

BASE = pathlib.Path(__file__).resolve().parent.parent
AUDIT = BASE / "data" / "intermediate" / "generated_tagged"
PAGES = BASE / "data" / "generated_pages"
OUT = BASE / "data" / "intermediate" / "grounding"

# Deliberately outside the repo: the repo lives in a OneDrive folder, and a multi-GB
# checkpoint dropped inside it would be uploaded to the cloud in the background.
CACHE = pathlib.Path(os.environ.get("MINICHECK_CACHE",
                                    pathlib.Path.home() / ".cache" / "minicheck"))

CITATION = re.compile(r"\[([^\]]*?S\s*\d[^\]]*)\]")
TIER_B = re.compile(r"^##\s+(?:key points|worked example)", re.I | re.M)
MATH = re.compile(r"\$\$.+?\$\$|\$[^$\n]+\$", re.S)
MIN_CLAIM_WORDS = 6


def sentences(text: str) -> list[str]:
    """Split into sentences without being fooled by the maths.

    A full stop inside `$1.5 \\times 10^3$` is a decimal point, and splitting there
    produces two fragments that mean nothing and that MiniCheck would judge as
    unsupported. Math spans are masked out, split, then put back.
    """
    holes: list[str] = []

    def stash(m):
        holes.append(m.group(0))
        return f"\x00{len(holes) - 1}\x00"

    masked = MATH.sub(stash, text)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Zऀ-ൿ])", masked)

    def restore(s):
        return re.sub(r"\x00(\d+)\x00", lambda m: holes[int(m.group(1))], s)

    return [restore(p).strip() for p in parts if p.strip()]


def cited_claims(page: str) -> list[tuple[str, list[str]]]:
    """(claim, [refs]) for every tagged sentence in the sourced part of the page.

    Only the part before Key points / Worked example is read. Those two sections restate
    and invent respectively, so a tag inside them is either a duplicate of a claim already
    checked or attached to the model's own example.
    """
    body = TIER_B.split(page)[0]
    body = re.sub(r"^<!--.*?-->\s*$", "", body, flags=re.M | re.S)

    # Split into blocks on blank lines and drop heading lines BEFORE sentence splitting.
    # The sentence regex breaks on ". " followed by a capital, and a markdown "##" is not
    # a capital, so without this a claim came out as
    #   "we write 15 min, not 15min .\n\n## Measuring Short Intervals\n\nSometimes, we ..."
    # -- one sentence, a heading and the next sentence glued together, judged as a single
    # claim against one passage. That inflated the unsupported count on its own.
    pieces: list[str] = []
    for block in re.split(r"\n\s*\n", body):
        lines = [ln for ln in block.splitlines() if not ln.lstrip().startswith("#")]
        block = " ".join(lines).strip()
        if block:
            pieces.extend(sentences(block))

    out = []
    for raw in pieces:
        if raw.lstrip().startswith("#"):
            continue
        refs = sorted({f"S{n}" for grp in CITATION.findall(raw)
                       for n in re.findall(r"S\s*(\d+)", grp)})
        if not refs:
            continue
        claim = CITATION.sub("", raw).strip()
        claim = re.sub(r"^[-*+]\s*", "", claim).strip()
        if len(claim.split()) < MIN_CLAIM_WORDS:
            continue
        out.append((claim, refs))
    return out


def targets(args, graphs, passages, evidence) -> list[tuple[str, str, int]]:
    """Which (subject, slug, grade) pages to check."""
    if args.concept:
        if not (args.subject and args.grade):
            raise SystemExit("--concept needs --subject and --grade")
        return [(args.subject, args.concept, args.grade)]
    found = []
    for p in sorted(PAGES.glob("**/*.md")):
        if re.search(r"\.(hi|te|od)\.md$", p.name):
            continue                       # a localisation is checked against English
        raw = p.read_text(encoding="utf-8")
        if not raw.lstrip().startswith("---"):
            continue
        try:
            front = json.loads(raw.split("---", 2)[1])
        except (ValueError, IndexError):
            continue
        subject = front.get("subject")
        subject = "maths" if subject == "maths" else "science"
        slug, grade = front.get("slug"), front.get("grade")
        if not slug or grade is None:
            continue
        if args.subject and subject != args.subject:
            continue
        if args.grade and grade != args.grade:
            continue
        found.append((subject, slug, grade))
    return found


def load_lean(dtype_name: str) -> None:
    """Make MiniCheck load on a laptop instead of refusing to load at all.

    MiniCheck hardcodes `device_map="auto"`. On a machine with 15.6 GB of RAM and 3.3 GB
    of it free, accelerate decides the 2.9 GB checkpoint will not fit, tries to offload
    part of it to disk, and then raises

        ValueError: The current `device_map` had weights offloaded to the disk. Please
        provide an `offload_folder` for them.

    so the model never loads. There is no constructor argument to turn that off, so the
    auto-classes it calls are wrapped here to drop `device_map` -- a plain CPU load, which
    is what `self.model.device` in its own inference path expects anyway.

    The dtype needs care. bfloat16 halves the resident size to ~1.5 GB and loads fine, but
    MiniCheck ends its inference with `label_probs[:, 1].cpu().numpy()`, and numpy has no
    bfloat16, so the run dies with "Got unsupported ScalarType BFloat16" AFTER the model
    has loaded and scored. Hence float32 by default: about 2.9 GB resident, which needs
    roughly 4 GB free. --dtype float16 is offered for a tighter machine, but T5 is known
    to be unstable in float16, so treat any run of it as suspect until spot-checked.
    """
    import torch
    import minicheck.inference as mci

    dtype = {"bfloat16": torch.bfloat16, "float16": torch.float16,
             "float32": torch.float32}[dtype_name]

    for cls_name in ("AutoModelForSeq2SeqLM", "AutoModelForSequenceClassification"):
        cls = getattr(mci, cls_name, None)
        if cls is None:
            continue
        original = cls.from_pretrained

        def patched(*a, _original=original, **kw):
            kw.pop("device_map", None)
            # transformers renamed torch_dtype -> dtype; it still accepts the old name but
            # warns, and will eventually stop. Try the new one and fall back, so this
            # keeps working on either side of that change.
            try:
                return _original(*a, dtype=dtype, **kw)
            except TypeError:
                return _original(*a, torch_dtype=dtype, **kw)

        cls.from_pretrained = patched


# --------------------------------------------------------------- used as a GATE
# Loaded once per process and reused. The model is ~2.9 GB resident in float32, so
# re-loading it per page would be both slow and the fastest way to run a laptop out of
# memory -- an earlier post-hoc run scoring all 385 claims of a grade in ONE call grew to
# 5.5 GB and got the whole session reaped. Per page there are only a dozen claims, which
# keeps the working set small; the model itself is the only large thing held.
_SCORER = None


def scorer(model: str = "flan-t5-large", dtype: str = "float32"):
    global _SCORER
    if _SCORER is None:
        load_lean(dtype)
        from minicheck.minicheck import MiniCheck  # noqa: PLC0415  (heavy import)
        CACHE.mkdir(parents=True, exist_ok=True)
        print(f"        loading MiniCheck {model} once for this run ...", flush=True)
        _SCORER = MiniCheck(model_name=model, cache_dir=str(CACHE))
    return _SCORER


def grounding_problems(page: str, anchors: list[dict], threshold: float = 0.5,
                       max_unsupported: float = 0.34, model: str = "flan-t5-large",
                       dtype: str = "float32") -> tuple[list[str], dict]:
    """Do this page's cited sentences follow from the passages they cite?

    Returns (faults, detail). `faults` is non-empty only when the UNSUPPORTED FRACTION
    exceeds `max_unsupported`, not when any single sentence fails. That threshold is the
    whole design question. Measured on 13 Grade 6 science pages, 19 of 98 cited sentences
    (19%) did not follow from what they cite, spread over 10 of the 13 pages -- so a gate
    that regenerated on a single failure would regenerate nearly every page, and most of
    those failures are over-tagging (the model's own worked example wearing a source tag)
    rather than a false claim a reader would notice. A fraction catches the page that is
    substantially ungrounded while tolerating the odd mis-tagged sentence.

    The detail is recorded whatever the verdict, so the number is available even on pages
    that pass.
    """
    claims = cited_claims(page)
    by_ref = {a["ref"]: a["text"] for a in anchors}
    jobs, missing, unjudgeable = [], [], []
    for claim, refs in claims:
        # MiniCheck is a text-entailment model and cannot read mathematics. Measured
        # twice: on Grade 6 it scored "there are exactly 60 minutes in one hour" at 0.201
        # against a passage containing "$60\,\mathrm{min} = 1\,\mathrm{h}$", and on Grade
        # 12 it scored the standard conditional-probability formula at 0.429 against a
        # passage that states it. A claim whose substance is a formula is outside its
        # competence, so it is counted separately rather than held against the page --
        # otherwise the gate spends paid regenerations on maths it cannot judge.
        prose = MATH.sub(" ", claim)
        if MATH.search(claim) and len(prose.split()) < 10:
            unjudgeable.append((claim, refs))
            continue
        doc = "\n\n".join(by_ref[r] for r in refs if r in by_ref)
        (jobs if doc else missing).append((claim, refs, doc))

    detail: dict = {"cited_sentences": len(claims), "checked": len(jobs),
                    "not_judgeable_mostly_maths": len(unjudgeable),
                    "cites_a_source_never_given": len(missing), "unsupported": []}
    if not jobs:
        return [], detail

    _, probs, _, _ = scorer(model, dtype).score(
        docs=[j[2] for j in jobs], claims=[j[0] for j in jobs])

    for (claim, refs, _), prob in zip(jobs, probs):
        if prob is None or prob < threshold:
            detail["unsupported"].append(
                {"claim": claim[:200], "cites": refs,
                 "support_probability": None if prob is None else round(float(prob), 3)})

    bad = len(detail["unsupported"]) + len(missing)
    # Over the claims it could actually judge, not over every tagged sentence. Including
    # the formula claims in the denominator would quietly forgive a page for having lots
    # of maths, and including them in the numerator would condemn it for the same thing.
    detail["unsupported_fraction"] = round(bad / max(len(jobs) + len(missing), 1), 3)
    detail["threshold"] = threshold
    detail["max_unsupported_fraction"] = max_unsupported

    faults = []
    if detail["unsupported_fraction"] > max_unsupported:
        faults.append(f"grounding: {bad} of {len(jobs) + len(missing)} judgeable cited "
                      f"sentence(s) are not supported by the passage they cite")
    elif missing:
        # Citing a source the page was never given is a different failure from a weak
        # one: the tag points at nothing, so it cannot be checked by anyone, ever.
        faults.append(f"grounding: {len(missing)} sentence(s) cite a source this page "
                      f"was never given")
    return faults, detail


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Check that each cited sentence follows from the passage it cites")
    ap.add_argument("--concept")
    ap.add_argument("--subject", choices=["maths", "science"])
    ap.add_argument("--grade", type=int)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--model", default="flan-t5-large",
                    help="MiniCheck model: flan-t5-large (770M, default), "
                         "roberta-large, deberta-v3-large")
    ap.add_argument("--threshold", type=float, default=0.5,
                    help="support probability below which a claim is reported (0.5)")
    ap.add_argument("--dtype", default="float32",
                    choices=["bfloat16", "float16", "float32"],
                    help="model precision; float32 is the only one MiniCheck can "
                         "convert to numpy at the end (default)")
    ap.add_argument("--limit", type=int, help="stop after N pages (for a quick look)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--dry-run", action="store_true",
                    help="count the claims and show a few, load no model at all")
    args = ap.parse_args()
    if not (args.all or args.concept):
        raise SystemExit("give --concept ... or --all")

    graphs, passages, evidence = bc.load()
    levels = bc.level_profile(passages)
    todo = targets(args, graphs, passages, evidence)
    if args.limit:
        todo = todo[:args.limit]

    jobs = []          # (subject, slug, grade, claim, refs, doc)
    skipped = []
    for subject, slug, grade in todo:
        tagged = None
        for stream in ("maths", "biology", "chemistry", "physics"):
            cand = AUDIT / stream / f"grade{grade}" / f"{slug}.md"
            if cand.exists():
                tagged = cand
                break
        if tagged is None:
            skipped.append((slug, grade, "no tagged copy"))
            continue
        try:
            ctx = bc.build(subject, slug, grade, graphs, passages, evidence, levels)
        except SystemExit as e:
            skipped.append((slug, grade, f"build failed: {e}"))
            continue
        anchors = {a["ref"]: a["text"] for a in ctx["anchors"]}
        claims = cited_claims(tagged.read_text(encoding="utf-8"))
        if not claims:
            skipped.append((slug, grade, "no tagged sentences"))
            continue
        for claim, refs in claims:
            # Everything the sentence cites, together. A sentence citing [S1, S2] is
            # supported if the two passages support it between them, and judging each
            # tag alone would report half of such a sentence as unsupported.
            doc = "\n\n".join(anchors[r] for r in refs if r in anchors)
            if not doc:
                jobs.append((subject, slug, grade, claim, refs, None))
                continue
            jobs.append((subject, slug, grade, claim, refs, doc))

    missing_ref = [j for j in jobs if j[5] is None]
    jobs = [j for j in jobs if j[5] is not None]
    print(f"{len(todo)} page(s), {len(jobs)} cited sentence(s) to check"
          + (f", {len(missing_ref)} citing a ref the page was never given" if missing_ref else "")
          + (f", {len(skipped)} page(s) skipped" if skipped else ""))
    for slug, grade, why in skipped[:10]:
        print(f"   skip {slug} gr{grade}: {why}")

    if args.dry_run:
        for subject, slug, grade, claim, refs, doc in jobs[:5]:
            print(f"\n  {slug} gr{grade} {refs}\n    claim: {claim[:110]}"
                  f"\n    doc  : {len(doc.split())} words")
        for subject, slug, grade, claim, refs, _ in missing_ref[:5]:
            print(f"\n  {slug} gr{grade} cites {refs} which is not among its sources")
            print(f"    claim: {claim[:110]}")
        return

    from minicheck.minicheck import MiniCheck  # noqa: E402  (heavy; only when needed)
    CACHE.mkdir(parents=True, exist_ok=True)
    load_lean(args.dtype)
    print(f"loading MiniCheck {args.model} (cache: {CACHE}, dtype: {args.dtype}) ...")
    scorer = MiniCheck(model_name=args.model, cache_dir=str(CACHE))

    docs = [j[5] for j in jobs]
    claims = [j[3] for j in jobs]
    labels, probs, _, _ = scorer.score(docs=docs, claims=claims)

    report: dict[str, list[dict]] = {}
    for (subject, slug, grade, claim, refs, _), label, prob in zip(jobs, labels, probs):
        if prob is not None and prob >= args.threshold:
            continue
        key = f"{subject}/grade{grade}/{slug}"
        report.setdefault(key, []).append({
            "claim": claim, "cites": refs,
            "support_probability": None if prob is None else round(float(prob), 3),
        })
    for subject, slug, grade, claim, refs, _ in missing_ref:
        key = f"{subject}/grade{grade}/{slug}"
        report.setdefault(key, []).append({
            "claim": claim, "cites": refs, "support_probability": None,
            "note": "cites a source this page was never given",
        })

    OUT.mkdir(parents=True, exist_ok=True)
    stamp = OUT / "unsupported_claims.json"
    stamp.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                     encoding="utf-8")

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        for key, rows in sorted(report.items()):
            print(f"\n{key}")
            for r in rows:
                p = r["support_probability"]
                print(f"   [{r['cites']}] p(support)={p}"
                      + (f"  {r['note']}" if r.get("note") else ""))
                print(f"      {r['claim'][:150]}")
    flagged = sum(len(v) for v in report.values())
    print(f"\n{len(jobs)} cited sentence(s) checked, {flagged} reported "
          f"below p={args.threshold}, across {len(report)} page(s)")
    print(f"written to {stamp.relative_to(BASE).as_posix()}")


if __name__ == "__main__":
    main()
