#!/usr/bin/env python3
"""
Grow the glossary from the pages already generated
==================================================
The glossary is what keeps one English term reading the same way on every page of a
language. Hand-writing it does not scale: the graph's concept names and aliases cover 2 of
the 39 terms that actually needed pinning, the textbooks carry term lists in only 31
sections of 233 books, and asking the prompt for "consistent terminology" cannot work
because every page is a separate API call that cannot see any other page.

So the pages build it themselves. Each English page ends with a line the model writes:

    <!-- TERMS: refraction, normal, angle of incidence, refractive index -->

and the localisation prompt requires the English word in brackets on the first appearance
of exactly those terms -- ପ୍ରତିସରଣ (refraction). This script reads those pairs back off the
localised pages and pins them, so the first page to render a term fixes it and every later
page inherits it. No extra API calls: it rides along with generation that is happening
anyway, and it works for any subject or grade with no word list existing in advance.

What it will NOT pin on its own:
  * a term two pages render differently -- someone has to choose, and choosing wrongly
    propagates to every page afterwards
  * a rendering that is just the English word in Indic letters, which is the exact defect
    the whole approach exists to avoid

Usage:
  python scripts/build_glossary.py                    # report only, changes nothing
  python scripts/build_glossary.py --write            # apply the unambiguous additions
  python scripts/build_glossary.py --lang te --verbose
"""

import argparse
import json
import pathlib
import sys
from collections import Counter, defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from check_translations import (  # noqa: E402
    GLOSSARY, LANGS, PAGES, body_of, collapse, latin_ratio, looks_transliterated,
    overlaps, term_pairs,
)


def load() -> tuple[dict, dict]:
    """The glossary file and its terms dict. The file carries a _comment to preserve."""
    if not GLOSSARY.exists():
        return {"terms": {}}, {}
    doc = json.loads(GLOSSARY.read_text(encoding="utf-8"))
    return doc, doc.setdefault("terms", {})


def subjects_seen() -> dict[str, list[str]]:
    """english term -> the subjects whose pages bracketed it.

    A pin is only safe to enforce on the subject it came from. Several of these terms are
    ordinary English words as well: "product" is a maths term and a milk product, "even"
    is a maths term and an adverb, "normal" is an optics term and "a normal walk". Without
    this, the maths rendering was demanded on biology pages that never meant it. Harvested
    from every language at once, because provenance is a property of the term, not of the
    translation.
    """
    out: dict[str, set[str]] = defaultdict(set)
    for lang in LANGS:
        for path in sorted(PAGES.glob(f"**/*.{lang}.md")):
            # .../generated_pages/<subject>/grade<N>/<slug>.<lang>.md
            subject = path.parent.parent.name
            for eng, native in term_pairs(body_of(path)):
                if latin_ratio(native) < 0.3:
                    out[eng].add(subject)
    return {eng: sorted(subs) for eng, subs in sorted(out.items())}


def harvest(lang: str) -> dict[str, Counter]:
    """english term -> Counter of the renderings seen for it, across every page."""
    seen: dict[str, Counter] = defaultdict(Counter)
    for path in sorted(PAGES.glob(f"**/*.{lang}.md")):
        for eng, native in term_pairs(body_of(path)):
            # A rendering that is mostly Latin is the English word left untranslated, or
            # the bracket convention misfiring on a formula. Neither is a term.
            if latin_ratio(native) < 0.3:
                seen[eng][native] += 1
    return seen


def classify(eng: str, counts: Counter, pinned: str | None) -> tuple[str, str, str]:
    """(verdict, rendering, note) for one English term in one language."""
    # Inflected forms of one word are one rendering: Telugu fuses case endings onto the
    # noun, so యానకం and యానకానికి are the same term and must not look like a disagreement.
    variants = collapse(set(counts))
    best = max(variants, key=lambda v: (counts[v], -len(v)))

    if pinned:
        if any(overlaps(v, pinned) for v in variants):
            return "agrees", pinned, ""
        return "deviates", best, f"pinned {pinned}"
    if len(variants) > 1:
        return "conflict", best, " / ".join(sorted(variants))
    if looks_transliterated(eng, best):
        return "held", best, "reads as the English word in Indic letters"
    # Precision guard, from what the first dry run actually produced. A multi-word
    # rendering seen on ONE page is where the bracket trim over-grabs: "absolute refractive
    # index" came back as हम निरपेक्ष अपवर्तनांक and ଆମେ ପରମ ପ୍ରତିସରଣାଙ୍କ, both starting with
    # the pronoun "we", and "wave theory of light" as అంచనా కాంతి తరంగ సిద్ధాంతం, starting
    # with "estimate". An n-word English term keeps n Indic tokens, so a lead-in word rides
    # along whenever the real term is shorter than the English one. A wrong pin propagates
    # to every page generated afterwards, which is worse than no pin, so these are reported
    # for a human and never written. A single word cannot carry a lead-in, and two pages
    # agreeing is evidence no stray word is involved; either is pinned automatically.
    if " " in best and sum(counts.values()) < 2:
        return "review", best, "multi-word, seen once -- check the first word belongs"
    return "new", best, f"{counts[best]} page(s)"


def main() -> None:
    ap = argparse.ArgumentParser(description="Grow the glossary from generated pages")
    ap.add_argument("--write", action="store_true",
                    help="apply the unambiguous additions to glossary.json")
    ap.add_argument("--lang", choices=LANGS, help="only this language")
    ap.add_argument("--verbose", action="store_true", help="list terms that already agree")
    args = ap.parse_args()

    doc, terms = load()
    langs = [args.lang] if args.lang else list(LANGS)
    totals: Counter = Counter()
    additions = 0

    for lang in langs:
        seen = harvest(lang)
        if not seen:
            print(f"\n{lang}: no bracketed terms found on any page")
            continue
        print(f"\n{lang}  ({len(seen)} English terms bracketed across the pages)")
        for eng in sorted(seen):
            pinned = terms.get(eng, {}).get(lang)
            verdict, rendering, note = classify(eng, seen[eng], pinned)
            totals[verdict] += 1
            if verdict == "agrees" and not args.verbose:
                continue
            print(f"    {verdict:9} {eng:26} {rendering:26} {note}")
            if verdict == "new" and args.write:
                terms.setdefault(eng, {})[lang] = rendering
                additions += 1

    print("\n" + ", ".join(f"{v} {k}" for k, v in sorted(totals.items())) or "nothing found")
    print("  new       a term nothing had pinned -- safe to add")
    print("  agrees    the pages match the pin")
    print("  deviates  a page disagrees with the pin: regenerate that page, or change "
          "the pin if the page is right")
    print("  conflict  pages disagree with each other: choose one by hand, then --write")
    print("  review    multi-word and seen once: pin it by hand if the wording is right")
    print("  held      looks transliterated, never pinned automatically")

    if args.write:
        # Provenance is refreshed on every --write, not only when a term is added, so a
        # glossary written before this existed gains it. Merged rather than replaced: if
        # the pages a term came from are later regenerated or removed, dropping its
        # subjects would make it unscoped again, which is the bug this prevents.
        before = json.dumps(doc.get("subjects", {}), sort_keys=True)
        known = dict(doc.get("subjects", {}))
        for eng, subs in subjects_seen().items():
            known[eng] = sorted(set(known.get(eng, [])) | set(subs))
        doc["subjects"] = dict(sorted(known.items()))
        rescoped = json.dumps(doc["subjects"], sort_keys=True) != before

        if additions:
            doc["terms"] = dict(sorted(terms.items()))
        if additions or rescoped:
            GLOSSARY.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n",
                                encoding="utf-8")
            where = GLOSSARY.relative_to(GLOSSARY.parent.parent.parent).as_posix()
            print(f"\nwrote {additions} new pin(s) to {where}"
                  + (", and refreshed which subjects each pin came from"
                     if rescoped else ""))
        else:
            print("\nnothing unambiguous to add")
    else:
        print("\n(report only -- pass --write to apply the 'new' rows)")


if __name__ == "__main__":
    main()
