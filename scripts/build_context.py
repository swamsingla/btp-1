#!/usr/bin/env python3
"""
Assemble the generation prompt for one (concept, grade) pair
=============================================================
Everything before this script existed to make this prompt possible: the extraction
gave clean text, the passages gave citable units, the retrieval found the right ones,
and the graph says what the student already knows and what must not be mentioned yet.

The prompt carries six things, and each exists because of a specific failure it
prevents:

  1. anchor passages          — the model writes from the book, not from memory
  2. grade_delta warning      — when the text had to be borrowed from another grade,
                                say so, or Grade 9 text gets reproduced at Grade 7
  3. assumed knowledge        — prerequisites at lower grades, so the page does not
                                re-teach fractions every time
  4. out-of-scope fence       — concepts that depend on this one at higher grades, so
                                a Grade 8 page does not drift into Grade 11 material
  5. measured level targets   — taken from that grade's own prose, so "write for Grade
                                7" means something checkable instead of a vibe
  6. citation rules           — every claim traceable to a passage id

Usage:
  python scripts/build_context.py --concept photosynthesis --grade 7
  python scripts/build_context.py --concept solar-eclipse --grade 7 --subject science
  python scripts/build_context.py --sample 5        # one prompt per grade band
  python scripts/build_context.py --concept X --grade 7 --json   # machine-readable
"""

import argparse
import json
import re
import statistics as st
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
EV_DIR = BASE / "data" / "intermediate" / "concept_evidence"
PASSAGES = BASE / "data" / "intermediate" / "index" / "passages.jsonl"
GRAPHS = {s: BASE / "data" / "knowledge_graph" / s / "graph_v2.json" for s in ("maths", "science")}

MATH_SPAN = re.compile(r"\$[^$]*\$")
WORD = re.compile(r"[A-Za-z]+")
MAX_SECTIONS = 4          # anchors are whole sections now, so fewer of them
# One complete section is enough to ground a page — what matters is how much text
# there is, not how many sections it came from. Requiring two sections made 133
# concepts ungeneratable whose whole explanation sits in a single section.
MIN_ANCHORS = 1
MIN_SOURCE_WORDS = 250    # below this there is genuinely too little to work from
ENOUGH_ANCHORS = 3        # below this, borrow from neighbouring sections to top up
MAX_SOURCE_WORDS = 2600   # ceiling on total extract text, to bound prompt size

# How long a page should be, per grade. A junior page is NOT a short page: explaining an
# idea to an eleven-year-old takes more words than stating it for a seventeen-year-old,
# because it needs the build-up, the everyday example and the restatement that a senior
# page can assume. The bands rise with grade only because senior topics carry more
# material, not because junior readers deserve less.
# Raised after measuring the first 16 pages: length tracks THIS BAND and almost nothing
# else. Whole-section retrieval lifted the source given to the model from 1,026 to 1,646
# words (+60%) and the pages grew by 6% — the model writes to the number it is told. So
# the number is the lever, and it is only safe to raise it now that the source behind it
# is 60% larger and the traceability retry catches claims the extracts do not support.
# Then narrowed after a 4-page check: asked for 900-1300, 1000-1400, 1100-1500 and
# 1200-1700, the model returned 1030, 959, 1038 and 994 — a 79-word spread across bands
# 300 words apart, on sources of 1,440 to 2,517 words. It saturates near 1,000 words per
# call. Raising the floor above that does not buy words, it only fails pages that are
# already complete: the 994-word Grade 11 probability page derives the theorem, works two
# examples and covers the topic. So the floors sit just under saturation and the ceilings
# leave room for the occasional long one (Adjoint came in at 1,229). Going materially past
# ~1,000 words needs a second call per page, not a bigger number in the prompt.
# Grade 6 was lowered from 900 to 700 on 2026-10-02 after two full runs of the Grade 6
# maths set — 76 page-generations in all, each short page retried twice. The median page
# came back at about 750 words both times and nothing clustered near 900, even where the
# retrieved source ran to 1,500-2,400 words, so 900 was not a target the model would reach
# for these concepts. It is also the wrong target: a Grade 6 page on types of fractions does
# not need 900 words, and asking for words the topic does not contain is what the expansion
# cap below exists to prevent. 700-1250 is what a substantial Grade 6 page actually looks
# like here. The higher grades are untouched; their bands were measured on their own output.
# Grade 7 was lowered from 900 to 700 on 2026-10-03 for the same reason, measured the same
# way. Across 13 Grade 7 page-generations the lengths were 376, 501, 546, 577, 584, 604,
# 704, 744, 819, 855, 892, 915 and 1011 words: a median of 704, and only 2 of the 10 pages
# on a full 900-1250 band reached their floor. One concept, area of a circle, was asked six
# times and answered 362, 483, 494 and 501 - the length a topic draws out of the model is
# stable, so retrying a short page mostly spends the budget the arithmetic check needs.
# Grade 7's measured median is LOWER than Grade 6's 792, which settles it: these are not
# longer pages than Grade 6's, and 900 was never a number this would reach. Part of the
# cause is upstream of length - the no-figures rule discards much of what a diagram-heavy
# chapter like circles actually contains, so the usable source is far smaller than the raw
# extract count suggests - and that is worth fixing in retrieval, not by demanding words.
# Grades 8-12 are untouched; their bands were measured on their own output.
GRADE_WORDS = {6: (700, 1250), 7: (700, 1250), 8: (950, 1300), 9: (1000, 1350),
               10: (1000, 1350), 11: (1050, 1450), 12: (1050, 1450)}
# The page may say more than the extracts do — framing, analogies and worked examples are
# the model's to write — but not without limit. Asking for 1,200 words from 150 words of
# source is an instruction to invent, which is how last year's Grade 6 page about rulers
# acquired a "Theorem: Standard Unit Definition" and a section on transitivity.
MAX_EXPANSION = 2.5

# The languages the platform targets, as code -> (English name, name in that language).
# Sarvam covers ten Indian languages; these are the three the project set out to serve.
LANGUAGES = {
    "en": ("English", "English"),
    "hi": ("Hindi", "हिन्दी"),
    "te": ("Telugu", "తెలుగు"),
    "od": ("Odia", "ଓଡ଼ିଆ"),
}


def load() -> tuple[dict, dict, dict]:
    graphs = {s: json.loads(p.read_text(encoding="utf-8")) for s, p in GRAPHS.items()}
    passages = {}
    for line in PASSAGES.open(encoding="utf-8"):
        p = json.loads(line)
        passages[p["id"]] = p
    evidence: dict[tuple[str, str, int], dict] = {}
    for subject in GRAPHS:
        for line in (EV_DIR / f"{subject}.jsonl").open(encoding="utf-8"):
            r = json.loads(line)
            evidence[(subject, r["slug"], r["grade"])] = r
    return graphs, passages, evidence


def level_profile(passages: dict) -> dict[tuple[str, int], dict]:
    """What this grade's own prose actually looks like, so the target is measurable.

    Science carries its difficulty in vocabulary and maths in notation, so both are
    reported and the prompt quotes whichever is meaningful for the subject.
    """
    buckets: dict[tuple[str, int], list] = defaultdict(list)
    for p in passages.values():
        if p["kind"] != "text":
            continue
        fam = "maths" if p["subject"] == "maths" else "science"
        buckets[(fam, p["grade"])].append(p)

    out = {}
    for key, ps in buckets.items():
        sent, long_words, with_math = [], [], 0
        for p in ps:
            plain = MATH_SPAN.sub(" ", p["text"])
            sentences = [s for s in re.split(r"[.!?]+", plain) if len(s.split()) > 2]
            if sentences:
                sent.append(st.mean(len(s.split()) for s in sentences))
            words = WORD.findall(plain)
            if words:
                long_words.append(100 * sum(len(w) > 8 for w in words) / len(words))
            with_math += p["has_math"]
        out[key] = {
            "n": len(ps),
            "words_per_sentence": round(st.median(sent), 1) if sent else None,
            "long_word_pct": round(st.median(long_words), 1) if long_words else None,
            "math_pct": round(100 * with_math / len(ps)),
        }
    return out


_SECTION_INDEX: dict[int, dict[tuple, list[dict]]] = {}


def section_index(passages: dict) -> dict[tuple, list[dict]]:
    """Prose passages grouped by the section they belong to, in document order.

    Built once per passage set: doing it inside build() would rebuild 8,000 rows for
    every one of the 959 concept-grade pairs.
    """
    key = id(passages)
    if key not in _SECTION_INDEX:
        index: dict[tuple, list[dict]] = defaultdict(list)
        for p in passages.values():
            if p["kind"] == "text":
                index[(p["grade"], p["subject"], p["chapter"], p["section"])].append(p)
        for group in index.values():
            group.sort(key=lambda p: p["id"])
        _SECTION_INDEX[key] = index
    return _SECTION_INDEX[key]


def stitch(parts: list[str]) -> str:
    """Join consecutive passages of one section, removing the overlap between them.

    build_passages carries ~50 words from each window into the next so that an idea
    spanning a boundary survives in one piece. Concatenating them back without trimming
    would repeat those words, so find the longest suffix of what we have that opens the
    next passage, and drop it.
    """
    out = parts[0].strip()
    for nxt in parts[1:]:
        nxt = nxt.strip()
        tail = out.split()
        head = nxt.split()
        overlap = 0
        for n in range(min(len(tail), len(head), 120), 10, -1):
            if tail[-n:] == head[:n]:
                overlap = n
                break
        out += "\n\n" + " ".join(head[overlap:]) if overlap else "\n\n" + nxt
    return out


def page_plan(anchors: list[dict], grade: int) -> dict:
    """How long the page should be and which sections it may have.

    Both are derived from the sources rather than fixed, because a fixed template is
    what produces invented content: a mandatory "Worked example" heading on a concept
    the books never work an example for gets filled anyway.

    The spine is always present. Everything else is offered only when the extracts
    actually contain that kind of material.
    """
    source_words = sum(len(a["text"].split()) for a in anchors)
    lo, hi = GRADE_WORDS.get(grade, (300, 600))
    # The grade sets the band, the extracts bound it at BOTH ends. A senior page with two
    # thin extracts cannot honestly reach 800 words, and demanding it invites padding —
    # three Grade 10-12 pages came in 150-200 words short of a floor the sources could not
    # support. Scaling the floor too lets a short page be correct rather than a failure.
    hi = min(hi, max(250, int(MAX_EXPANSION * source_words)))
    lo = min(lo, max(250, int(1.3 * source_words)), hi)
    span = (int(round(lo / 25)) * 25, int(round(hi / 25)) * 25)

    optional = ["a short worked example of your own, applying a rule the extracts state"]
    if any("$" in a["text"] for a in anchors):
        # A formula is a claim about the world, so it is Tier A: quote it, do not derive
        # a new one.
        optional.insert(0, "a formula, written as the extracts write it")
    return {"source_words": source_words, "target_words": span, "optional": optional}


def build(subject: str, slug: str, grade: int, graphs: dict, passages: dict,
          evidence: dict, levels: dict) -> dict:
    graph = graphs[subject]
    concepts = graph["concepts"]
    if slug not in concepts:
        raise SystemExit(f"{slug} is not in the {subject} graph")
    concept = concepts[slug]
    if grade not in concept["grades"]:
        raise SystemExit(f"{concept['canonical_name']} is not taught in grade {grade} "
                         f"(graph says {concept['grades']})")

    rec = evidence.get((subject, slug, grade))
    if rec is None:
        raise SystemExit(f"no evidence row for {slug} grade {grade} — run match_concepts.py")

    # Which list to anchor on is already decided by the fallback ladder: a non-zero
    # grade_delta means the tagged grade had nothing solid and another grade did. Reading
    # `hits or fallback_hits` instead would only fall back when the in-grade list is
    # EMPTY, and a weak-but-present list is the dangerous case — Place Value at Grade 6
    # retrieves "A Pinch of History" and "Games and Winning Strategies" at 0.75, while
    # Grade 7 has "3.4 Decimal Place Value" at 0.80.
    hits = rec.get("fallback_hits") or [] if rec["grade_delta"] else rec["hits"]

    # `source_sections` in the graph is a ruling made by hand, after reading the books:
    # this grade's page is written from exactly these sections. It exists because cosine
    # cannot make that call for Ganita Prakash. Grade 6 chapter 10 IS the integers
    # chapter and scored under 0.70 for "Integers" — its sections are titled "Bela's
    # Building of Fun" and "The Token Model" — so Grade 6 borrowed the Grade 7
    # multiplication section and the two grades got one page between them. Aliases were
    # tried first and made it worse: "Bela's building of fun" pulled in "5.6 Fun with
    # numbers", and the rival-heading test below read "Model" as Mean, Median and MODE.
    # An entry is a section title (all of that section's prose) or a single passage id,
    # which is how a chapter summary or a headingless opening page is named.
    pins = (concept.get("source_sections") or {}).get(str(grade))
    if pins:
        hits = []

    # Prose only, and filtered BEFORE truncating — otherwise a concept whose top hits are
    # exercises ends up with two anchors instead of five.
    prose = [h for h in hits if (passages.get(h["passage_id"]) or {}).get("kind") == "text"]

    # A near-duplicate topic steals the slot: Solar Eclipse's top hits held three Lunar
    # Eclipse passages, and Ionic Bonding's held four from "BONDING IN CARBON — THE
    # COVALENT BOND", because those sections are genuinely about bonding and score well.
    #
    # Weighting rare words does not fix it — "ionic" occurs in 11 section titles and
    # "bonding" in only 7, so rarity makes the SHARED word look distinctive. What
    # actually separates the siblings is the graph itself: if a section's heading matches
    # some other concept's name better than it matches ours, that section belongs to that
    # concept's page, not this one.
    def overlap(words: set[str], section: str) -> float:
        return sum(1 for w in words if w in section) / (len(words) or 1)

    name_words = set(re.findall(r"[a-z]{4,}", concept["canonical_name"].lower()))
    rivals = [set(re.findall(r"[a-z]{4,}", c["canonical_name"].lower()))
              for s, c in concepts.items() if s != slug]

    def contested(h: dict) -> bool:
        section = h["section"].lower()
        mine = overlap(name_words, section)
        return any(overlap(r, section) > mine for r in rivals)

    def own(h: dict) -> float:
        return overlap(name_words, h["section"].lower())

    prose.sort(key=lambda h: (-round(own(h), 2), -h["cosine"]))

    # Retrieval finds the right PASSAGE; the page is better served by the whole SECTION it
    # sits in. A section is one complete explanation, so passing all of it stops anchors
    # that open mid-derivation ("On equating the dimensions on both sides...") and gives
    # about 1.5x the material at no extra retrieval cost. Measured over 870 pages: the
    # shortlist already held 2,760 words where the prompt was receiving 1,026.
    sections = section_index(passages)
    anchors: list[dict] = []
    taken: set[tuple] = set()
    budget = MAX_SOURCE_WORDS

    for entry in pins or []:
        if entry in passages:
            group = [passages[entry]]
        else:
            found = [k for k in sections if k[0] == grade and k[3] == entry
                     and (k[1] == "maths") == (subject == "maths")]
            if len(found) != 1:
                raise SystemExit(f"{slug} grade {grade}: source_sections names {entry!r}, "
                                 f"which matches {len(found)} sections in the Grade {grade} "
                                 f"books — it must match exactly one")
            group = sections[found[0]]
        first = group[0]
        anchors.append({
            "ref": f"S{len(anchors) + 1}",
            "passage_id": first["id"], "passage_ids": [q["id"] for q in group],
            "grade": first["grade"], "subject": first["subject"],
            "chapter": first["chapter"], "section": first["section"],
            "page": first["page"], "cosine": 1.0, "borrowed_topic": False,
            "text": stitch([q["text"] for q in group]),
        })

    def take_sections(candidates: list[dict], limit: int,
                      unlabelled: bool = False) -> None:
        nonlocal budget
        for h in candidates:
            if len(anchors) >= limit or budget <= 0:
                return
            p = passages.get(h["passage_id"])
            if p is None:
                continue
            # A passage with no section heading is usually the chapter's opening narrative
            # — the story about Rashmika cycling to school before the physics starts — so
            # it is skipped unless we are scraping for anything at all (see the top-up
            # below).
            labelled = len(p["section"].strip()) >= 4
            if not labelled and not unlabelled:
                continue
            key = (p["grade"], p["subject"], p["chapter"], p["section"])
            if key in taken:
                continue
            # An unlabelled passage stands alone. Grouping by its empty section name would
            # sweep in every other headingless passage in the chapter.
            group = (sections.get(key) or [p]) if labelled else [p]
            text = stitch([q["text"] for q in group])
            words = len(text.split())
            # One section can run to 12,000 words. If others are already in, skip it; if
            # it is the first, keep its opening paragraphs rather than let a single
            # section become a 10,000-token prompt.
            if words > budget:
                if anchors:
                    continue
                kept: list[str] = []
                for para in text.split("\n\n"):
                    if sum(len(k.split()) for k in kept) + len(para.split()) > budget:
                        break
                    kept.append(para)
                text = "\n\n".join(kept) or " ".join(text.split()[:budget])
                words = len(text.split())
            taken.add(key)
            budget -= words
            anchors.append({
                "ref": f"S{len(anchors) + 1}",
                "passage_id": p["id"],
                "passage_ids": [q["id"] for q in group],
                "grade": p["grade"], "subject": p["subject"], "chapter": p["chapter"],
                "section": p["section"], "page": group[0]["page"],
                "cosine": h["cosine"], "borrowed_topic": contested(h), "text": text,
            })

    # Sections another concept owns are a last resort: filling spare slots with them is
    # how an Ionic Bonding page ends up citing "BONDING IN CARBON - THE COVALENT BOND"
    # three times. Take them only to reach a workable number, never to pad to the maximum.
    take_sections([h for h in prose if not contested(h)], MAX_SECTIONS)
    if len(anchors) < ENOUGH_ANCHORS:
        # Topping up only to MIN_ANCHORS starved pages whose own sections were mostly
        # excluded: Addition Theorem had 12 prose hits across 3 sections and used 2,
        # leaving 595 words of source for a page wanting 775. Too little source is not
        # the safe failure it looks like — the model fills the gap from memory, and the
        # repair pass then deletes what it cannot trace.
        take_sections([h for h in prose if contested(h)], ENOUGH_ANCHORS)

    # Last resort: a passage MinerU left without a heading. Usually that is framing and
    # the rule above is right to skip it — Grade 6 chapter 2 opens with "In this chapter,
    # we will explore ... points, lines, rays", which teaches nothing. But Ganita Prakash
    # frequently puts the chapter's PRIMARY DEFINITION on that unlabelled opening page,
    # and discarding it cost four Grade 6 pages outright: chapter 4's headingless opener
    # is where "any collection of facts, numbers, measures ... is called data" is defined,
    # so Data Collection and Organisation was left with no source and no page at all,
    # while Line of Symmetry got 108 words against a 250-word floor and was skipped even
    # though chapter 9 holds 1,500 words of prose. Taken only to clear that floor, after
    # every properly headed section has had its chance, so a real section is never
    # displaced by a chapter opener.
    if sum(len(a["text"].split()) for a in anchors) < MIN_SOURCE_WORDS:
        take_sections(prose, ENOUGH_ANCHORS, unlabelled=True)

    # Still short: fall back to the chapter's own summary blocks. These are marked
    # "summary" rather than "text" and so never reach the shortlist above, but in Ganita
    # Prakash a summary is ordinary exposition — the chapter restating its rules — and not
    # an exercise, so it is safe to teach from. Without it, Data Collection and
    # Organisation had only the 128-word definition of data to work from and Basic
    # Geometrical Concepts only 159 words, both under the floor, so neither got a page at
    # all. Ordered after the headingless top-up, and still only to clear the floor.
    if sum(len(a["text"].split()) for a in anchors) < MIN_SOURCE_WORDS:
        summaries = [h for h in hits
                     if (passages.get(h["passage_id"]) or {}).get("kind") == "summary"]
        summaries.sort(key=lambda h: (-round(own(h), 2), -h["cosine"]))
        take_sections(summaries, ENOUGH_ANCHORS, unlabelled=True)

    known = [{"name": concepts[s]["canonical_name"], "grades": concepts[s]["grades"]}
             for s in concept.get("prerequisites", [])
             if s in concepts and min(concepts[s]["grades"]) <= grade]
    later = [{"name": concepts[s]["canonical_name"], "grades": concepts[s]["grades"]}
             for s in concept.get("leads_to", [])
             if s in concepts and min(concepts[s]["grades"]) > grade]

    # A concept taught at several grades gets one page per grade, and the later page is
    # meant to go further than the earlier one. Two things have to hold for that, and the
    # first is not about the prompt at all.
    #
    # 1. The grade must have text of its own. match_concepts lets a grade with weak text
    #    borrow from the nearest grade that has it, and for a multi-grade concept that
    #    nearest grade is usually the concept's OTHER grade — so both pages are written
    #    from the same extracts, and since a page may state nothing its extracts do not,
    #    the second one has nothing different to say. Of the 14 concepts Grades 6 and 7
    #    share, 13 had one grade borrowing from the other; across both graphs it is 90
    #    pages. Regenerating eight such Grade 7 pages with the Grade 6 page supplied as a
    #    reference made it worse, not better: six came back 85-100% word for word the
    #    Grade 6 page, because with identical extracts that page is the one text that
    #    satisfies every rule in the prompt. No wording fixes a page with nothing to add,
    #    so it is not generated. Which grade keeps the concept is where the book teaches
    #    it; the cure for a wrongly skipped grade is in the graph (drop the grade) or in
    #    retrieval (aliases that find the grade's own section), never here.
    def borrows_from_sibling(g: int) -> int | None:
        if (concept.get("source_sections") or {}).get(str(g)):
            return None
        r = evidence.get((subject, slug, g))
        if r and r["grade_delta"] and r["source_grade"] in concept["grades"]:
            return r["source_grade"]
        return None

    same_source_as = borrows_from_sibling(grade)

    # 2. The model has to know what the earlier page covered, so it extends it instead of
    #    re-deriving it. Only the IMMEDIATELY PRECEDING grade is used, not the lowest one:
    #    percentage at Grade 8 should extend the Grade 7 page, not everything since Grade 6.
    #    A lower grade that itself borrows from a sibling is passed over: its page, where
    #    one was published before rule 1 existed, is written from a sibling's extracts —
    #    often this very grade's — and is no record of what was taught before.
    lower_grades = [g for g in concept["grades"]
                    if g < grade and borrows_from_sibling(g) is None]
    prior_grade = max(lower_grades) if lower_grades else None

    fam = "maths" if subject == "maths" else "science"
    return {
        "slug": slug, "name": concept["canonical_name"], "grade": grade,
        "subject": subject, "stream": concept.get("subject", subject),
        "area": concept["area"], "description": concept["description"],
        "aliases": concept.get("aliases", []),
        "evidence": rec["evidence"], "context_evidence": rec["context_evidence"],
        "source_grade": grade if pins else rec["source_grade"],
        "grade_delta": 0 if pins else rec["grade_delta"],
        "anchors": anchors, "assumed_knowledge": known, "out_of_scope": later,
        "prior_grade": prior_grade, "same_source_as": same_source_as,
        "level": levels.get((fam, grade), {}),
        # A page written from one loosely-related extract is a page written from memory
        # with a citation stapled on. Better to skip it and record why.
        "generate": (same_source_as is None and len(anchors) >= MIN_ANCHORS
                     and sum(len(a["text"].split()) for a in anchors) >= MIN_SOURCE_WORDS),
        "plan": page_plan(anchors, grade),
        # A warning to "not drift into" a neighbouring topic is noise when every extract
        # is from one — that is simply where the book teaches this concept.
        "all_borrowed": bool(anchors) and all(a["borrowed_topic"] for a in anchors),
    }


def language_block(lang: str) -> list[str]:
    """Instructions for writing the page in an Indian language.

    The extracts stay in English because that is the corpus we have, so the model is
    explaining English source material in another language rather than translating a
    finished page. The terminology line matters most: NCERT's own Hindi, Telugu and Odia
    editions have settled technical vocabulary, and a page that invents its own words for
    "divisibility" is useless to a student holding the state edition.
    """
    name, native = LANGUAGES[lang]
    return [
        "",
        f"LANGUAGE: write the whole page in {name} ({native}).",
        f"  - The extracts below are in English. Explain what they say in {name}; do not "
        f"reproduce them sentence by sentence.",
        f"  - Use the technical terms that {name}-medium school textbooks in India use "
        f"for this topic. The first time a technical term appears, put the English term "
        f"in brackets after it, so the reader can match it to an English textbook.",
        f"  - The headings, the bullets and the worked example are all in {name} too.",
        "  - Leave every formula exactly as it is written. Anything between $ or $$ is "
        "mathematics, not language: do not translate, transliterate or re-space it.",
        "  - Keep Indian numerals as the extracts write them (8560 stays 8560).",
        f"  - The source tags stay exactly as they are — [S1], [S2] — in Latin letters. "
        f"They are not words and must not be translated, transliterated or dropped. A "
        f"page written in {name} needs them just as much as an English one: one Telugu "
        f"page came back with none at all, and nothing in it could be checked.",
    ]


GLOSSARY_PATH = BASE / "data" / "knowledge_graph" / "glossary.json"


def glossary_for(english_page: str, lang: str,
                 subject: str | None = None) -> list[tuple[str, str]]:
    """The pinned translations for terms that actually appear in this page.

    Pages are localised one at a time, so nothing otherwise stops the same term being
    rendered two ways: the Odia pages called refraction ରିଫ୍ରାକ୍ସନ୍ — the English word
    sound-spelled — on one page and ପ୍ରତିସରଣ, the real Odia term, on another. Only the
    terms present in this page are sent, to keep the prompt short.

    `subject` restricts the pins to those harvested from that subject's own pages, and it
    matters more than it looks. The pins are English words, and several of them are
    ordinary English as well as technical terms: "product" is गुणनफल in maths and a milk
    product in biology, "even" is सम in maths and "even common sugar" in prose, "normal"
    is अभिलंब in optics and "a normal walk" in a biology page. Matching the bare word
    demanded the maths rendering on biology pages that never meant it -- 8 of the first 63
    Grade 6 science localisations were held for exactly this, with nothing wrong on them.
    A pin with no recorded subject still applies everywhere; those are the hand-added
    multi-word ones, where this collision cannot happen.
    """
    if not GLOSSARY_PATH.exists():
        return []
    doc = json.loads(GLOSSARY_PATH.read_text(encoding="utf-8"))
    terms = doc.get("terms", {})
    if subject is not None:
        from_subject = doc.get("subjects", {})
        terms = {en: langs for en, langs in terms.items()
                 if subject in from_subject.get(en, [subject])}
    page = english_page.lower()
    # Anchored, but allowing English inflections. A bare "en in page" substring test fired
    # the OPTICS "normal" on the adverb "normally" in a biology page, and "factor" on "a
    # factory that produces pens" — then told the model "USE EXACTLY THESE TERMS" for a term
    # the page never uses. A bare \b...\b is the opposite error: "factor" is written
    # "factors" / "factorise" on every page that really is about factors. Plural and verb
    # endings count as the term; "-ly", "-y", "-ies", "-al" do not.
    infl = r"(?:s|es|ed|ing|ise|ises|ised|ising|ize|izes|ized|izing)?"
    found = [(en, langs[lang]) for en, langs in terms.items()
             if lang in langs
             and re.search(rf"\b{re.escape(en.lower())}{infl}\b", page)]
    # longest first, so "refractive index" is pinned before "index" would be
    return sorted(found, key=lambda p: -len(p[0]))


def render_repair(ctx: dict, page: str) -> str:
    """Ask for the tags to be added to a finished page, changing nothing else.

    Whether the model tags diligently turns out to be close to a coin toss, and not a
    retrieval problem: pages that came back untraceable had the same mean cosine (0.787)
    as clean ones (0.791), and the worst of them had strong evidence at 0.82. Rerunning
    the whole generation just re-rolls that, at the cost of a fresh page and fresh
    variance everywhere else. Repairing is a narrower task and a cheaper call.
    """
    lines = [
        "The page below was written from the extracts that follow, but some of its "
        "paragraphs carry no source tag, so those claims cannot be traced.",
        "",
        "Return the SAME page with the missing tags added:",
        "  - Put [S1], [S2] … at the end of every sentence that states something from the "
        "extracts: a definition, a fact, a rule, a formula, a reason why something happens.",
        "  - Change nothing else. Same words, same sentences, same headings, same order, "
        "same worked example. You are annotating, not rewriting.",
        "  - Leave untagged only what you invented: the opening framing, an analogy, and "
        "your own worked example.",
        "  - If a sentence states something the extracts do NOT support, delete that "
        "sentence rather than tagging it.",
        "  - Start directly with the # heading.",
        "",
        "=" * 70,
        "EXTRACTS",
        "=" * 70,
    ]
    for a in ctx["anchors"]:
        lines += ["", f"[{a['ref']}] {a['section']}", a["text"].strip()]
    lines += ["", "=" * 70, "THE PAGE TO TAG", "=" * 70, "", page.strip()]
    return "\n".join(lines)


# The English page ends with a machine-readable list of its own technical terms. Three
# other ways of getting that list were measured and rejected: the graph's concept names and
# aliases cover 2 of 39 terms actually needing a pin, the textbooks carry term lists in only
# 31 sections of 233 books, and simply asking for "consistent terminology" cannot work
# because each page is a separate call that cannot see any other page. The model knows which
# words in the page it just wrote are technical; asking costs nothing on top of generation.
TERMS_RE = re.compile(r"<!--\s*TERMS\s*:(.*?)-->", re.S | re.I)


def terms_in(page: str) -> list[str]:
    """The terms the model declared for this page, lower-cased and de-duplicated."""
    seen: dict[str, None] = {}
    for m in TERMS_RE.finditer(page):
        for raw in m.group(1).split(","):
            term = " ".join(raw.split()).strip(" .;:").lower()
            # a stray sentence means the model ignored the format; a term is a few words
            if term and len(term) <= 40 and len(term.split()) <= 4:
                seen.setdefault(term, None)
    return list(seen)


def strip_terms(page: str) -> str:
    """Remove the TERMS comment. The audit copy keeps it; nothing a reader sees does."""
    return re.sub(r"\n{3,}", "\n\n", TERMS_RE.sub("", page)).strip()


def render_localised(ctx: dict, english_page: str, lang: str) -> str:
    """Ask for the same page again in another language, using the English one as the spec.

    Generating each language independently from the extracts gave four pages that did not
    match: one opened with "Divisibility by 2, 5 and 10" and another with "2, 4, 5 and 10",
    because each run chose its own sections. For a platform where a reader may switch
    language mid-page, that is a defect — the Telugu reader and the Hindi reader should be
    reading the same page.

    This is still generation by the same model, not a translation model: it may reshape a
    sentence so it reads naturally. What it may not do is change what the page says or how
    it is organised.
    """
    name, native = LANGUAGES[lang]
    # The declared list is the spec for terminology; the comment itself must not reach the
    # model, or it copies it into the localised page.
    declared = terms_in(english_page)
    english_page = strip_terms(english_page)
    return "\n".join([
        f"Below is a finished textbook page in English, written for a Grade "
        f"{ctx['grade']} student. Write the same page in {name} ({native}).",
        "",
        f"MATCH THE ENGLISH PAGE:",
        "  - the same sections, in the same order, with the headings translated",
        "  - the same facts, the same examples, the same numbers",
        "  - the same worked example, worked the same way",
        "  - nothing added and nothing left out, including the bullets",
        "",
        f"WRITE IT PROPERLY IN {name.upper()}:",
        f"  - Natural {name}, not word-by-word translation. The meaning must match; the "
        f"phrasing should read as though it was written in {name} to begin with.",
        f"  - Use the technical terms that {name}-medium school textbooks in India use.",
        f"  - Use the established {name} term. Do not spell an English word out in "
        f"{name} letters when a real term exists.",
        f"  - Use the SAME {name} word for the same idea every time it appears on this "
        f"page. If you call something one thing in the first section, call it that in "
        f"every later section too -- do not switch to a synonym part-way through.",
        "  - Leave every formula exactly as written. Anything between $ or $$ is "
        "mathematics, not language: do not translate, transliterate or re-space it.",
        "  - Keep numerals as they are (8560 stays 8560).",
        # The English prompt already forbids pointing at figures, and a sweep of all 294
        # generated pages found no real violation. This is here so the rule survives a
        # localisation too: the model reshapes sentences, and "the two halves match" is
        # one rewrite away from "as you can see in the diagram".
        "  - THERE IS NO DIAGRAM ON THIS PAGE. Never write \"see the figure\", \"as shown "
        "in the diagram\", \"look at the picture above\" or anything else that points the "
        "reader at something to look at. If the English describes a shape or a position "
        "in words, keep it in words.",
        "  - Keep the source tags — [S1], [S2] — exactly as they are, in Latin letters, "
        "in the same sentences. They are not words and must not be translated or dropped.",
        "  - Start directly with the # heading. No preamble, no note about translating.",
        # Bracketing a FIXED list, rather than "the first time a technical term
        # appears", is what makes the rendering harvestable: the page itself says which
        # words it considers technical, so build_glossary.py reads pairs it was promised
        # instead of guessing at running prose — the source of every false positive in the
        # first terminology audit.
        *([] if not declared else [
            "",
            f"BRACKET THESE TERMS. The first time each one appears, put the English word "
            f"in round brackets straight after your {name} term — like "
            f"{'प्रकाश का अपवर्तन (refraction)' if lang == 'hi' else 'X (refraction)'} — "
            f"and only on the first appearance. Every term on this list, and no others:",
            *[f"    {term}" for term in declared],
        ]),
        *([] if not (pinned := glossary_for(english_page, lang, ctx.get("stream"))) else [
            "",
            f"USE EXACTLY THESE {name.upper()} TERMS — they are fixed across the whole "
            f"site, so the same idea reads the same on every page:",
            *[f"    {en}  ->  {native}" for en, native in pinned],
        ]),
        "",
        "=" * 70,
        "ENGLISH PAGE",
        "=" * 70,
        "",
        english_page.strip(),
    ])


def render_verify(page: str) -> str:
    """Ask for the page's own arithmetic to be recomputed, with nothing else to go on.

    Deliberately given the page and NOTHING ELSE — no extracts, no concept, no graph. The
    faults this is for are self-contained: a tally of 20 answers reported as 20+7+8+2, a
    square said to have four lines of symmetry and then shown with two, 360/7 given as
    52 6/7, "5,000,000 is also called five hundred thousand", a section that announced 840
    and then factorised 225. Every one of those is decidable from the page alone, and
    checking arithmetic is far easier than producing it, so a separate call with fresh
    attention is worth more than asking the writer to re-read itself.

    Kept narrow on purpose. Invited to comment on style or sources, the model returns
    opinions, and an opinion cannot gate a page.
    """
    return "\n".join([
        "Below is a finished school textbook page. Check its ARITHMETIC and its INTERNAL "
        "CONSISTENCY. Nothing else.",
        "",
        "RECOMPUTE — do not read along and agree. Work every number out yourself:",
        "  - add the sums up, and divide the divisions out, on your own",
        "  - count the items in any list the page counts, one by one",
        "  - check that a total equals the parts it was made from",
        "",
        "THEN CHECK THE PAGE AGAINST ITSELF:",
        "  - does each worked example actually follow the rule the page stated?",
        "  - if the page claims a count — four lines of symmetry, five groups of tally "
        "marks, three rules — does it then show that many?",
        "  - do two parts of the page contradict each other?",
        "  - does a section explain the thing its own heading names?",
        "",
        "Say NOTHING about style, wording, sources, citations, language, grade level or "
        "teaching approach. Only arithmetic and self-consistency.",
        "",
        "Answer in exactly this form and add nothing else:",
        "VERDICT: ok",
        "  — or —",
        "VERDICT: fail",
        "- what the page says, and what it should be",
        "- (one line per fault)",
        "",
        "=" * 70,
        "THE PAGE TO CHECK",
        "=" * 70,
        "",
        page.strip(),
    ])


def render_fix(page: str) -> str:
    """Hand the finished page back and ask for a corrected copy of the WHOLE page.

    The other shape of the second pass, and the one to compare against render_verify.
    That one asks for a verdict and the page is then regenerated from scratch, which
    throws away a page that was right everywhere except one sum; this one asks for the
    page back with the wrong parts corrected and publishes whatever is returned.

    Given the page and NOTHING ELSE, for the same reason as render_verify: the faults
    being hunted are decidable from the page alone, and fresh attention on a finished
    page beats asking the writer to re-read itself.

    The whole risk of this shape is the return trip. A page handed back loses its source
    tags, its TERMS line or three of its sections and is then unpublishable, so the page
    goes over WITH its tags and the instruction to keep them is the longest one here.
    """
    return "\n".join([
        "Below is a finished school textbook page. Correct anything in it that is WRONG "
        "and return the entire page.",
        "",
        "RECOMPUTE — do not read along and agree. Work every number out yourself:",
        "  - add the sums up, and divide the divisions out, on your own",
        "  - count the items in any list the page counts, one by one",
        "  - check that a total equals the parts it was made from",
        "  - check each worked example actually follows the rule the page stated",
        "  - check that if the page claims a count — four lines of symmetry, three "
        "rules — it then shows that many",
        "  - check that no two parts of the page contradict each other",
        "",
        "WHERE SOMETHING IS WRONG, FIX IT:",
        "  - correct the number, and correct every later number that depended on it",
        "  - if a statement is false, state it correctly",
        "  - if a question is asked and never answered, answer it",
        "",
        "CHANGE NOTHING ELSE. This is a correction, not a rewrite:",
        "  - keep every heading, in the same order, with the same wording",
        "  - keep the [S1], [S2] … source tags exactly where they are, and keep the "
        "<!-- TERMS: --> line at the end exactly as it is",
        "  - keep the same length — do not shorten the page, do not add new sections, "
        "do not add commentary",
        "  - leave correct sentences word for word as they are",
        "",
        "If nothing is wrong, return the page unchanged.",
        "",
        "Return ONLY the page, starting directly with its # heading. No preamble, no "
        "list of what you changed, no notes.",
        "",
        "=" * 70,
        "THE PAGE",
        "=" * 70,
        "",
        page.strip(),
    ])


def render(ctx: dict, lang: str = "en", prior_page: str | None = None) -> str:
    if ctx.get("same_source_as"):
        return (f"SKIP — {ctx['name']} (Grade {ctx['grade']}, {ctx['stream']}): Grade "
                f"{ctx['grade']} has no text of its own on this concept, and the extracts "
                f"found for it are the ones its Grade {ctx['same_source_as']} page is "
                f"written from. A second page from the same extracts can only repeat the "
                f"first. Do not generate.")
    if not ctx["generate"]:
        return (f"SKIP — {ctx['name']} (Grade {ctx['grade']}, {ctx['stream']}): only "
                f"{ctx['plan']['source_words']} words of usable extract across "
                f"{len(ctx['anchors'])} section(s), which is not enough to write a "
                f"grounded page from. Do not generate.")

    L = ctx["level"]
    lines = [
        f"Write one textbook page explaining **{ctx['name']}** for a Grade "
        f"{ctx['grade']} student ({ctx['stream']}).",
        "",
        f"WHAT THE TOPIC IS: {ctx['description']}",
        "  (that line is a label to tell you which topic this page is about. It is not a "
        "source and has not been checked against any book — never repeat a fact from it. "
        "A description reading \"divisibility by 2, 3, 4, 5, 6, 8, 9, 10, 11\" led one "
        "page to claim it had covered all eleven when the extracts covered five.)",
    ]
    if ctx["aliases"]:
        lines.append(f"ALSO CALLED: {', '.join(ctx['aliases'])}")

    if lang != "en":
        lines += language_block(lang)

    lines += ["", "SOURCE TEXT — write only from these extracts, and cite them."]
    if not ctx["anchors"]:
        lines.append("  (none found — do not write this page)")
    for a in ctx["anchors"]:
        note = ("  — NOTE: this section is mainly about a neighbouring topic. Use it only "
                "for background or contrast, and do not let the page drift into it."
                if a.get("borrowed_topic") and not ctx["all_borrowed"] else "")
        lines += [
            "",
            f"[{a['ref']}] Grade {a['grade']} {a['subject']}, {a['chapter']}, "
            f"\"{a['section']}\"{note}",
            a["text"].strip(),
        ]

    if ctx["grade_delta"]:
        direction = "above" if ctx["grade_delta"] > 0 else "below"
        # The two directions need opposite advice. "Simpler words, shorter sentences" was
        # written for text borrowed from above and was being given unchanged for text
        # borrowed from below, telling a Grade 7 page to be simpler than its Grade 6 source.
        rewrite = ("simpler words, shorter sentences, and drop any method the student has "
                   "not met yet" if ctx["grade_delta"] > 0 else
                   "the extracts were written for younger readers, so write at the level "
                   "given under WRITING LEVEL below, but add no fact, method or reason "
                   "that they do not state")
        lines += [
            "",
            f"LEVEL WARNING: no Grade {ctx['grade']} text covers this topic, so the "
            f"extracts above are from Grade {ctx['source_grade']} — "
            f"{abs(ctx['grade_delta'])} year(s) {direction}. Keep the ideas, rewrite them "
            f"for Grade {ctx['grade']}: {rewrite}.",
        ]

    if ctx["assumed_knowledge"]:
        lines += ["", "THE STUDENT ALREADY KNOWS THIS — do not re-teach it:"]
        lines += [f"  - {k['name']} (Grade {min(k['grades'])})" for k in ctx["assumed_knowledge"]]

    if ctx["out_of_scope"]:
        lines += ["", "DO NOT INTRODUCE — these are taught in later grades:"]
        lines += [f"  - {k['name']} (Grade {min(k['grades'])})" for k in ctx["out_of_scope"]]

    # `prior_page` must arrive WITHOUT its source tags. The first version of this block
    # pasted the tagged copy, whose [S1] [S2] refer to that page's extracts and not to the
    # ones above: a finished page in exactly the format being asked for, tags included, is
    # an answer to copy rather than a thing to build on, and it was copied.
    if ctx.get("prior_grade") and prior_page:
        was = ctx["prior_grade"]
        lines += [
            "",
            f"WHAT THE READER HAS ALREADY BEEN TAUGHT — the Grade {was} page on this same "
            f"concept is reproduced below, so that you know where this page starts. It is "
            f"not a source and it is not a model for this page.",
            f"  - Do not write that page again. Reuse none of its sentences, none of its "
            f"worked examples and none of the numbers in them.",
            f"  - Do not re-teach what it explains. Where this page needs one of its ideas, "
            f"recall it in a single sentence beginning \"You may already know\" and move on.",
            f"  - Spend this page on what the extracts above teach that the Grade {was} "
            f"page does not reach: a new method, a new case, a harder kind of problem, a "
            f"new use. Every section must teach something that page does not.",
            f"  - Make each worked example harder than the ones on that page: more steps, "
            f"more awkward numbers, or the new method.",
            f"  - Nothing about sources changes. Every fact on this page still comes from "
            f"the extracts above and carries their tag; a fact that appears only on the "
            f"Grade {was} page and not in the extracts is left out.",
            "",
            f"--- START OF THE GRADE {was} PAGE ---",
            prior_page.strip(),
            f"--- END OF THE GRADE {was} PAGE ---",
        ]

    if L:
        target = (f"about {L['words_per_sentence']} words per sentence; "
                  f"roughly {L['long_word_pct']}% long words")
        if ctx["subject"] == "maths" or L["math_pct"] > 30:
            target += f"; {L['math_pct']}% of passages at this level carry a formula"
        lines += ["", f"WRITING LEVEL, measured from Grade {ctx['grade']} "
                      f"{ctx['subject']} textbooks: {target}."]

    plan = ctx["plan"]
    lo, hi = plan["target_words"]
    example_note = next((o for o in plan["optional"] if o.startswith("a short worked")), "")
    lines += [
        "",
        "PAGE SHAPE — these headings, in this order, and no others:",
        f"  # {ctx['name']}",
        "  (an opening paragraph of 2-4 sentences: what it is and why it matters)",
        "  ## ...  three to five sections, each titled by you after what it explains",
        "  ## Worked example    (optional — " + (example_note or "your own numbers") + ")",
        "  ## Key points        (3-5 bullets, and always last)",
        *([] if lang == "en" else
          [f"  Write these headings in {LANGUAGES[lang][0]}, keeping the same order "
           f"and the same meaning."]),
        "  Do not add a heading beyond these. An empty section gets filled with invention.",
        "",
        f"LENGTH: {lo}-{hi} words, and aim for the upper half of that range. A thin page "
        f"is a failure: the reader came here instead of the textbook, so the idea needs "
        f"building up, showing in an everyday situation, and then stating plainly. Earn "
        f"the length with explanation and examples, never with repetition.",
        "",
        "WHAT MUST COME FROM THE EXTRACTS, each with a source tag:",
        "  - definitions of terms",
        "  - facts about the world: values, constants, dates, names, places, measurements",
        "  - rules, laws and formulas, and the conditions under which they hold",
        "  - causes and mechanisms, the reason something happens",
        "  If the extracts do not support it, leave it out. Never state a fact about the "
        "world that the extracts do not state, however confident you are of it.",
        "",
        "  HOW TO TAG: put the source in square brackets at the end of the sentence, like",
        "  this —",
        "      The frequency of a light wave does not change when it is refracted [S1].",
        "      Both angles are measured from the normal to the surface [S2, S3].",
        "  Putting a fact in your own words does not remove the need for the tag. If a "
        "sentence states something you learned from an extract, tag it, however much you "
        "have rewritten it. A page with no tags has failed, however well written it is.",
        "",
        "  THE TEST TO APPLY TO EVERY PARAGRAPH: could a reader check this against the "
        "extracts? If yes, it needs a tag. A paragraph may go untagged only when you "
        "invented all of it — the opening, an analogy, or your own worked example. "
        "Explaining a definition, a law or a mechanism in your own words is not "
        "inventing it.",
        "",
        "  NEVER REFER TO THE EXTRACTS AS A THING THE READER CAN SEE. They cannot: this "
        "page is all they get. Write \"each outcome has probability 1/8\", never \"the text "
        "assigns 1/8\"; no \"as the extract says\", \"the passage above\" or \"the textbook\". "
        "The source tag is the only place a source is mentioned.",
        "",
        "WHAT YOU SHOULD WRITE YOURSELF — no tag needed:",
        "  - how the page is organised and the order the ideas come in",
        "  - the opening, everyday context, and analogies that make the idea land",
        "  - a worked example of your own, using your own numbers, applying a rule the "
        "extracts state. Give one for EVERY rule or idea you state, not just once at the "
        "end — that is what makes a page long enough to be worth reading, and it costs "
        "nothing in accuracy because the rule itself came from an extract.",
        "  - links back to what the student already knows, and forward to what comes next",
        "  This part is why the page is worth reading instead of the textbook. Use it. It "
        "must never contradict the extracts, and must never introduce a new fact about "
        "the world through the back door of an example. Writing a section without a tag "
        "does not make it exempt from being true: a page that summarised itself as "
        "\"we have seen methods for 2, 3, 4, 5, 6, 8, 9, 10 and 11\" had covered five of "
        "those and invented the eleventh.",
        "",
        "  The line between the two: an example you construct is yours to write; a "
        "statement about the world is not. \"If a ribbon is 4,521 cm long, is that "
        "divisible by 3?\" is yours. \"Jupiter is 778 million km from the Sun\" is not, "
        "unless an extract says so.",
        "",
        "EXPLAINING WHY — THE ONE THING YOU MAY NOT INVENT:",
        "  Explain WHY something is true only where an extract gives the reason. If the "
        "extracts state a rule but not its reason, state the rule, show how to use it, "
        "and STOP. Do not supply a derivation, a proof, a mechanism or a cause of your "
        "own, however confident you are of it.",
        "  This is not a matter of style. Every error in this project that could not be "
        "defended came from exactly here. One page explained the r^2 in the area of a "
        "circle as \"the area of a square that perfectly fits inside the circle's "
        "diameter\", which is false. Another gave an invalid proof of the angle sum "
        "property. Another explained why stars twinkle by saying where planets get their "
        "energy. In each case the topic was taught through diagrams, the extracts "
        "carried no reasoning, and the page filled the gap from memory. An invented "
        "reason reads exactly like a sourced one, so nobody downstream can catch it.",
        "  \"The rule is X [S1]. Here is how to use it: <your own example>.\" is a "
        "complete and correct section. It is BETTER than the same section with a reason "
        "you had to invent. A Grade 6 book states the area of a circle without proving "
        "it; so may you.",
        "  Before writing \"this is because\", \"the reason is\", \"this happens "
        "because\" or \"we can see why\", check that an extract says so. If none does, "
        "cut the clause and keep the rule.",
        "  This does not forbid saying why something MATTERS or where it is used — "
        "\"measuring length matters because we buy cloth by the metre\" is framing, and "
        "framing is yours to write. What is forbidden is inventing the mechanism or the "
        "proof behind a rule.",
        "",
        "ALWAYS",
        "  - TEACH THE TOPIC, do not explore it. Every rule, law or method the page "
        "raises must be STATED plainly in the section that raises it. The books often "
        "pose a rule as a question for the student to discover — \"can you see a pattern "
        "in the last two digits?\" — and leave the answer out on purpose. This page is a "
        "reference, not a worksheet: give the answer. A section that shows why the last "
        "digit fails for 4, and then never says to look at the last two digits, has "
        "taught nothing.",
        "  - Write in statements, not questions. Explaining is not quizzing. Rhetorical "
        "questions copied from the extracts should become the answers to those questions.",
        "  - Name a section after the ONE thing it explains, and explain that thing. Do "
        "not put a list in a heading: \"Divisibility by 2, 4, 5, 8 and 10\" promises five "
        "rules, and a section that then states two has misled the reader three times. "
        "Prefer several short sections, each named for a single rule, over one heading "
        "that collects them. Where two cases genuinely share one explanation, say both "
        "rules in full inside that section.",
        "  - An everyday comparison must be true. If you are not certain how something "
        "actually works, use a plain numerical example instead — a page claiming these "
        "rules validate barcodes is worse than one with no analogy at all.",
        "  - If the extracts say a topic is covered in later classes, mention that in one "
        "sentence. Do not give it a section. A heading you cannot fill from the extracts "
        "becomes a paragraph saying the rules \"are a bit different\" without giving them.",
        "  - The page has no diagrams. If an extract refers to labelled points from a "
        "figure — BC, AE, angle POQ, \"as shown in Fig. 10.4\" — do not copy it. Say the "
        "relationship in words and symbols the reader can follow without the picture, or "
        "leave it out.",
        "  - Even a one-line definition is a claim about the world and needs its tag.",
        "  - A blank like ____ in an extract is an exercise for the student. Never fill "
        "one in and never copy it.",
        "  - Continuous prose under the headings. No question sets, no exercises.",
        "  - WRITE ALL MATHEMATICS IN LaTeX, between single dollars: $\\frac{3}{4}$, "
        "$2 \\times 5 = 10$, $8560$, $\\frac{1}{2} = \\frac{2}{4}$. Never write a fraction "
        "as 3/4 in plain text and never leave a space inside the braces. The site renders "
        "LaTeX, and when pages disagree they look like two different books: of 38 Grade 6 "
        "maths pages only 8 used LaTeX, so one fractions page read $\\frac{4}{5}$ while the "
        "next read 2/10.",
        "  - USE THE INDIAN SCHOOL TERMS. HCF, or Highest Common Factor — not GCD and not "
        "greatest common divisor. LCM for the least common multiple. Lakh and crore for "
        "large numbers. If a source uses the other name, give the Indian one and you may "
        "put the other in brackets once.",
        "  - NEVER POINT AT SOMETHING THE READER CANNOT SEE. This page has no figures, no "
        "diagrams, no colours, and nothing above or below it. Do not write \"the figure "
        "above\", \"this blue line\", \"here, a unit is divided into 5 equal parts\", \"as "
        "shown\", \"observe the following\", \"the table below\" or \"as we have seen "
        "earlier\". If an extract explains something through a picture, say the idea in "
        "words and numbers, or leave it out. A sentence that only makes sense beside a "
        "diagram is worse than no sentence.",
        "  - NEVER TELL THE READER WHAT THEY DID IN ANOTHER CLASS, and never call this page "
        "a chapter. \"In Grade 6, you learned...\" is wrong on a Grade 6 page, and \"in this "
        "chapter you will learn\" is wrong everywhere. If you must lean on earlier work, "
        "write \"you may already know\".",
        "  - ANSWER EVERY QUESTION YOU RAISE, in the same section, in the same breath. If "
        "you write that you can check whether 682 is divisible by 2, check it and say yes. "
        "If you mention the numbers between 330 and 340 that are divisible by 4, name them: "
        "332, 336 and 340. Never write \"you will observe a pattern\" without stating the "
        "pattern, and never leave a lettered list of cases with only the first one worked. "
        "A question left hanging turns this page into a worksheet.",
        "  - Indian context and spellings.",
        "  - Start directly with the # heading. No preamble, no closing remarks.",
    ]

    # Asked of the English page only. This list is what holds Hindi, Telugu and Odia to one
    # rendering per term: without it each localised page invents its own vocabulary, which
    # is how one Odia page said ରିଫ୍ରାକ୍ସନ୍ (the English word in Odia letters) while another
    # said ପ୍ରତିସରଣ (the real term) for the same idea.
    if lang == "en":
        lines += [
            "",
            "THE LAST LINE OF YOUR REPLY — after the Key points, on its own line, list the "
            "technical terms this page uses, in this exact form:",
            "      <!-- TERMS: refraction, normal, angle of incidence, refractive index -->",
            "  Include the subject vocabulary a student would have to look up: the concept "
            "itself, the terms used in its definitions, and the names of quantities, rules, "
            "properties and units. Leave out ordinary words, numbers and your own examples. "
            "Lower case, comma separated, English, one line, and nothing after it.",
            "  This page will also be written in other languages, and that list is what "
            "keeps one term reading the same way on every one of them.",
        ]
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description="Assemble the generation prompt")
    ap.add_argument("--concept")
    ap.add_argument("--grade", type=int)
    ap.add_argument("--subject", choices=list(GRAPHS))
    ap.add_argument("--sample", type=int, help="show N prompts spread across grades")
    ap.add_argument("--json", action="store_true", help="print the context, not the prompt")
    args = ap.parse_args()

    graphs, passages, evidence = load()
    levels = level_profile(passages)

    targets: list[tuple[str, str, int]] = []
    if args.concept:
        subject = args.subject
        if subject is None:
            subject = next((s for s in GRAPHS if args.concept in graphs[s]["concepts"]), None)
            if subject is None:
                raise SystemExit(f"{args.concept} is in neither graph")
        grade = args.grade or min(graphs[subject]["concepts"][args.concept]["grades"])
        targets = [(subject, args.concept, grade)]
    elif args.sample:
        by_grade: dict[int, tuple] = {}
        for (subject, slug, grade), r in sorted(evidence.items()):
            if r["evidence"] == "strong" and grade not in by_grade:
                by_grade[grade] = (subject, slug, grade)
        targets = list(by_grade.values())[:args.sample]
    else:
        raise SystemExit("give --concept or --sample")

    for i, (subject, slug, grade) in enumerate(targets):
        ctx = build(subject, slug, grade, graphs, passages, evidence, levels)
        if args.json:
            print(json.dumps(ctx, indent=2, ensure_ascii=False))
            continue
        prompt = render(ctx)
        if i:
            print("\n" + "=" * 78 + "\n")
        print(prompt)
        print(f"\n--- {len(prompt)} chars, ~{len(prompt) // 4} tokens, "
              f"{len(ctx['anchors'])} anchors, evidence={ctx['evidence']}, "
              f"grade_delta={ctx['grade_delta']}")


if __name__ == "__main__":
    main()
