#!/usr/bin/env python3
"""
Check generated pages for the defects that reading them by hand would catch
===========================================================================
Nobody reviews 900 pages. These are the failures actually found by reading the first
sixteen, each turned into a test so the next batch is checked by machine:

  citations        a page citing a source it was never given
  no_citations     a page with no tags at all — nothing in it can be traced
  length           outside the band for its grade
  sections         missing the spine, or carrying a heading that was not offered
  drifting_section a section whose text matches a DIFFERENT section's heading better
                   than its own — a "Divisibility by 4 and 8" section that is really
                   about 9, which is exactly what happened at Grade 8
  questioning      written as a worksheet rather than a reference, which is what the
                   discovery-style books invite
  repetition       a looping phrase or a runaway bullet list
  markdown         raw "##" or "* " surviving into the text, i.e. something the
                   renderer will show literally

Usage:
  python scripts/check_pages.py
  python scripts/check_pages.py --lang en --verbose
"""

import argparse
import json
import pathlib
import re
from collections import Counter, defaultdict

BASE = pathlib.Path(__file__).resolve().parent.parent
PAGES = BASE / "data" / "generated_pages"
SPINE = ("key points",)
ALLOWED = ("worked example", "key points")
STOP = {"the", "and", "for", "with", "this", "that", "from", "its", "are", "how", "why",
        "what", "when", "into", "them", "their", "using", "rules", "rule"}


def words(text: str) -> set[str]:
    """Content words of a heading or a section, reduced to four-letter stems.

    Exact tokens made the drifting_section check unusable. "Reading and Writing Large
    Numbers" scored 25% against its OWN section, because the heading says reading, writing
    and numbers while the body says read, written and number -- so the section looked like
    it was about some other heading and a correct page was held back. The same morphology
    problem produced false positives on "Everyday Measurements", "How the Numbers Grow" and
    "Step-by-Step Summary". Four letters is enough to tie read/reading, number/numbers and
    write/writing together, and this is only ever used to compare a heading against prose,
    where the odd collision (factor/factory) costs nothing.
    """
    return {w[:4] for w in re.findall(r"[a-z0-9]+", text.lower())
            if w not in STOP and len(w) > 1}


def sections(body: str) -> list[tuple[str, str]]:
    out, parts = [], re.split(r"^##\s+(.+)$", body, flags=re.M)
    for i in range(1, len(parts), 2):
        out.append((parts[i].strip(), parts[i + 1]))
    return out


def structural_problems(body: str) -> list[str]:
    """Defects visible in an English page's own structure, with no metadata needed.

    Split out so generate_pages.py can run it before saving and ask for the page again:
    three rounds of prompt tuning did not stop the model collecting several rules under
    one heading and then explaining two of them, and a retry is cheaper than a page that
    misleads the reader.
    """
    problems = []
    secs = sections(body)

    # Checked here, not only in check(), because this function is what generate_pages.py
    # retries on. area-rectangle-square shipped with no Key points section at all: the page
    # simply stopped after the worked example, and the spine test that would have caught it
    # ran afterwards, when the only remedy left was a human noticing.
    titles = [t.lower() for t, _ in secs]
    for need in SPINE:
        if not any(need in t for t in titles):
            problems.append(f"sections: no '{need}' section")

    # There used to be a second drift test here, comparing each section's heading words
    # against every other heading's words and flagging a section whose body matched some
    # other heading better than its own. It was removed after being measured: across 64
    # generated pages it produced seven false positives and not one true one, and four
    # correct Grade 6 pages were held back by it. The premise is wrong. A heading is often
    # a label rather than a summary -- "Everyday Measurements", "Step-by-Step Summary",
    # "Spacing and Intervals", "How the Numbers Grow" -- and a section is not required to
    # repeat its own title in its prose, while the vocabulary of neighbouring headings
    # (number, fraction, angle) naturally recurs everywhere on a page about that topic.
    # Stemming the comparison fixed some cases and not others, because the real signal is
    # absent, not obscured. The defect this check was written for -- a heading promising
    # several rules and the section explaining different ones -- is caught by the test
    # below, which is specific and has held up.
    for title, text in secs:
        named = set(re.findall(r"\d+", title))
        if named and not any(a in title.lower() for a in ALLOWED):
            # Counted two ways on purpose. The word-bounded count is what catches a heading
            # that promises a rule the section never returns to. But on its own it flagged
            # "Dividing by Powers of 10", whose section is full of 10, 100 and 1000 -- the
            # bounded count sees only the bare "10" and reads the section as being about
            # something else. A number that keeps appearing inside larger numbers is still
            # the subject matter, so a digit has to be absent by both counts to be a fault.
            #
            # ABSENT, not merely scarce. This asked for two mentions until it was measured
            # across 206 generated page versions: at that threshold it flagged two sections,
            # both the same false positive -- a Grade 7 section headed "Why Triangles Add Up
            # to $180^{\circ}$" which argues exactly that, via parallel lines and a straight
            # angle, and states the number once at the end of the argument. Nothing obliges
            # a correct section to repeat the number in its own heading, and that page was
            # held back for it. Requiring the number to be missing ENTIRELY flagged nothing
            # in the same 206 versions, and still catches what this test was written for: a
            # heading promising a rule about a number the section never discusses.
            thin = [n for n in sorted(named)
                    if not re.search(rf"\b{n}\b", text)
                    and n not in text]
            if thin:
                problems.append(
                    f"drifting_section: '{title}' names {', '.join(thin)} but barely "
                    f"mentions it again — the section is about something else")

    # Degenerate repetition. Grade 8 Algebraic Identities came back at 5,662 words on a
    # 1000-1400 band: the page was fine until "Key points", where one bullet looped 84
    # times. max_tokens=3500 used to truncate the loop, so it surfaced as a SHORT page and
    # was misread as thin source. Catch the loop itself.
    # Math is stripped first: a maths page restates $(a+b)^2 = a^2 + 2ab + b^2$ in several
    # sections, and with the symbols removed that collapses into an identical token run.
    # Repeated PROSE is the defect; a repeated formula is the subject matter.
    # Display math needs its own alternative, listed FIRST. "\$[^$]*\$" alone matches the
    # empty span BETWEEN the two dollars of $$...$$, so the formula survived into the token
    # stream and \times / \mathrm read as looping prose: Divisibility gr8 was flagged
    # "repeats 13 times (times times times)" and Adjoint gr12 "repeats 6 times". 10 of 28
    # pages use $$, and this check gates a paid retry, so a false flag costs two calls.
    toks = re.findall(r"[a-z]+",
                      re.sub(r"\$\$.*?\$\$|\$[^$\n]*\$", " ", body, flags=re.S).lower())
    if len(toks) > 40:
        runs = Counter(" ".join(toks[i:i + 8]) for i in range(len(toks) - 8))
        phrase, n = runs.most_common(1)[0]
        # Threshold measured, not guessed. Across 16 English pages the max repeated 8-gram
        # is 1-2 on thirteen of them; the only two above 3 are both CORRECT parallel
        # phrasing in an enumerative page -- "a number is divisible by _ if it ends" six
        # times across six divisibility rules, "you add a drop of blue litmus solution"
        # four times across four tests. At >= 4 this check sent those back for two paid
        # retries each and the page came back no better. The defect it exists for repeated
        # 84 times, and that page was also 5,662 words on a 1000-1400 band, so the
        # over-length retry in generate_pages.py catches a runaway on its own -- this is a
        # second net and can afford to be loose. A rule-by-rule page may legitimately reach
        # eight; nothing legitimate reaches ten.
        if n >= 10:
            problems.append(f"repetition: a phrase repeats {n} times "
                            f"(\"{phrase[:40]}...\") — the model is looping")

    for title, text in secs:
        if "key points" in title.lower():
            nb = len(re.findall(r"^\s*[-*]\s", text, flags=re.M))
            if nb > 8:
                problems.append(f"repetition: 'Key points' has {nb} bullets, asked for 3-5")

    if body.count("?") >= 4:
        problems.append(f"questioning: {body.count('?')} question marks — "
                        f"written as a worksheet")
    return problems


def check(path: pathlib.Path) -> tuple[dict, list[str]]:
    raw = path.read_text(encoding="utf-8")
    meta = json.loads(raw.split("---")[1])
    body = raw.split("---", 2)[2]
    lang = meta.get("language", "en")
    problems = []

    cc = meta.get("citation_check", {})
    if cc.get("invented_citations"):
        problems.append(f"citations: cites {cc['invented_citations']} which were not given")
    if not cc.get("cited"):
        problems.append("no_citations: nothing in this page can be traced to a source")
    # Sections, not paragraphs. The prompt asks the model for its own worked example in
    # every section and the two-tier rules say that example carries no tag, so counting
    # untagged paragraphs failed pages that were correctly sourced — see the note in
    # generate_pages.check_citations. A section with a tagged rule and an untagged example
    # is traceable; a section with no tag anywhere is not.
    untraceable = cc.get("untraceable_sections", 0)
    if untraceable > 1:
        problems.append(f"untraceable: {untraceable} sections carry no citation at all — "
                        f"nothing in them can be checked against a source")

    lo, hi = cc.get("target_words", (0, 10**6))
    n = len(body.split())
    # word counts are calibrated on English; other scripts tokenise differently
    if lang == "en" and not (lo * 0.85 <= n <= hi * 1.15):
        problems.append(f"length: {n} words, outside {lo}-{hi}")

    secs = sections(body)
    if lang != "en":
        # Headings are translated, so an English string can never match. What matters for
        # a localised page is that it mirrors the English one, which is its spec.
        sibling = path.with_name(path.name.replace(f".{lang}.md", ".md"))
        if sibling.exists():
            en_secs = len(sections(sibling.read_text(encoding="utf-8").split("---", 2)[2]))
            if en_secs != len(secs):
                problems.append(f"sections: {len(secs)} sections but the English page has "
                                f"{en_secs} — the languages have diverged")

    if lang == "en":
        for title, _ in secs:
            low = title.lower()
            if any(a in low for a in ALLOWED):
                continue
            # topic sections are free-titled, so only flag headings that were dropped
            if "comes next" in low:
                problems.append(f"sections: '{title}' is no longer part of the page shape")

        problems += structural_problems(body)

    # Only markup at the START of a line can render literally. Matching "**" followed by
    # spaces anywhere flagged "**Solution:** " — ordinary bold, which renders fine.
    text_only = re.sub(r"^#{1,4}\s.*$|^\s*[-*•]\s+|^\s*\d+[.)]\s+", "", body, flags=re.M)
    if re.search(r"^\s*#{1,6}(?!\s)|^\s*\*\s{2,}", text_only, flags=re.M):
        problems.append("markdown: raw markup will render literally")

    return meta, problems


def main() -> None:
    ap = argparse.ArgumentParser(description="Check generated pages")
    ap.add_argument("--lang", help="only this language code")
    ap.add_argument("--verbose", action="store_true", help="list clean pages too")
    args = ap.parse_args()

    files = sorted(PAGES.glob("**/*.md"))
    if not files:
        raise SystemExit(f"no pages in {PAGES.relative_to(BASE).as_posix()}")

    counts: defaultdict[str, int] = defaultdict(int)
    bad = 0
    for f in files:
        meta, problems = check(f)
        if args.lang and meta.get("language") != args.lang:
            continue
        label = (f"{meta['concept'][:26]:28} gr{meta['grade']:<3} "
                 f"{meta.get('language', 'en')}")
        if problems:
            bad += 1
            print(f"  {label}")
            for p in problems:
                counts[p.split(":")[0]] += 1
                print(f"       {p}")
        elif args.verbose:
            print(f"  {label}   ok")

    print(f"\n{len(files) - bad}/{len(files)} pages clean")
    if counts:
        print("problems by type:", dict(sorted(counts.items(), key=lambda kv: -kv[1])))


if __name__ == "__main__":
    main()
