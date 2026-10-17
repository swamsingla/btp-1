#!/usr/bin/env python3
"""
Check that the localised pages say the same thing as their English spec
======================================================================
The project's whole claim is that generating per language beats machine translation, so
these are the checks that claim has to survive. Two questions, both answered without
reading the language:

CONTENT PARITY  Numbers, formulas and citation tags are language-independent. If the
                English page works 8560 and the Odia page works 8650, the pages have
                diverged no matter how fluent the Odia is. Section count likewise.

TERMINOLOGY     The localisation prompt asks for the English term in brackets on first
                use, which leaves a machine-readable trail: "ପ୍ରତିସରଣ (refraction)".
                Collecting those across every page shows whether ONE English term gets
                ONE rendering per language, which is the defect the report calls out and
                the reason direct generation was chosen over translation.

Usage:
  python scripts/check_translations.py
  python scripts/check_translations.py --verbose     # also list every term pairing found
"""

import argparse
import json
import pathlib
import re
import unicodedata
from collections import Counter, defaultdict

BASE = pathlib.Path(__file__).resolve().parent.parent
PAGES = BASE / "data" / "generated_pages"
GLOSSARY = BASE / "data" / "knowledge_graph" / "glossary.json"
LANGS = ("hi", "te", "od")
NAMES = {"hi": "Hindi", "te": "Telugu", "od": "Odia"}

# Devanagari, Telugu and Odia digits. A page writing 8560 in its own digits has not
# diverged, so normalise before comparing.
DIGITS = str.maketrans({chr(base + i): str(i)
                        for base in (0x0966, 0x0C66, 0x0B66)
                        for i in range(10)})


def body_of(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8").split("---", 2)[2]


def numbers(text: str) -> list[str]:
    """Multi-digit numbers, which carry the worked examples. Single digits are excluded:
    they appear incidentally in every sentence and would swamp the comparison."""
    return sorted(re.findall(r"\d{2,}", text.translate(DIGITS)))


# A parenthesis holding at least two Latin letters: the English gloss the localisation
# prompt asks for on a term's first appearance, as in "(COVID-19)" or "(non-contact)".
LATIN_GLOSS = re.compile(r"\((?=[^)]*[A-Za-z]{2})[^)]*\)")


def maths(text: str) -> list[str]:
    """Inline and display LaTeX, whitespace-collapsed. Latin either way, so comparable.

    Citation tags are stripped out of each span. The model sometimes closes a tagged
    sentence inside the dollars — "$\\frac{10}{15}+\\frac{3}{15}=\\frac{13}{15}.[S1]$" —
    and since a localised page is compared against the TAGGED English copy, an identical
    equation then compared unequal because only one side carried the tag. That held all
    three languages of Addition and Subtraction of Fractions with the nonsensical message
    "35 formulas, English has 35".
    """
    spans = re.findall(r"\$\$(.+?)\$\$|\$([^$\n]+)\$", text, flags=re.S)
    out = []
    for a, b in spans:
        span = re.sub(r"\[[^\]]*?S\s*\d[^\]]*\]", "", a or b)
        span = re.sub(r"\s+", "", span)
        # The WORDS inside 	ext{} are prose, not maths, and a localised page is supposed
        # to translate them: a Hindi reader should not meet "length" and "cm" inside the
        # one formula on the page. Their contents are normalised to a placeholder so the
        # comparison still does its real job -- that the formula was carried across with
        # its numbers, operators and structure intact -- without demanding that the prose
        # inside it stay English. Localised by hand across 18 pages on 2026-10-09.
        span = re.sub(r"\\text\{[^}]*\}", r"\\text{}", span)
        # Trailing sentence punctuation is not part of the formula. The model often closes
        # the sentence inside the dollars, so English held "$\\frac{3}{12}.$" while the
        # localised page wrote "$\\frac{3}{12}$" and the two compared unequal over a
        # full stop.
        out.append(span.rstrip(".,;:"))
    return sorted(out)


def tags(text: str) -> set[str]:
    return set(re.findall(r"\[S\d+", text))


def heads(text: str) -> list[str]:
    return re.findall(r"^##\s+(.+)$", text, flags=re.M)


def term_pairs(text: str) -> list[tuple[str, str]]:
    """(english_term, native_rendering) from "native (english)" on first use.

    The native side is the run of non-Latin words immediately before the bracket. An
    Indic sentence contains no Latin, so walking back until Latin appears swallows the
    whole sentence and then two renderings of the SAME term look different because they
    carry different lead-ins — that produced three false "inconsistent" flags. Stop at
    sentence and clause boundaries, and take no more words than the English term has.
    """
    out = []
    for m in re.finditer(r"([^\s(][^()]{0,60}?)\s*\(([A-Za-z][A-Za-z \-]{2,40})\)", text):
        native, eng = m.group(1).strip(), m.group(2).strip().lower()
        if len(eng.split()) > 4:
            continue
        # cut at the last boundary before the bracket: danda, full stop, heading mark
        native = re.split(r"[।॥.!?#\n]", native)[-1]
        # The ASCII hyphen is deliberately NOT a separator here. Indic renderings of a
        # single English word are often hyphenated compounds, and splitting them kept only
        # the last piece, which inverted the meaning on exactly the prefixes that matter:
        # ସହ-ମୌଳିକ (co-prime) was harvested as ମୌଳିକ, which means prime, and गैर-शून्य
        # (non-zero) as शून्य, which means zero. Both pages were correct; the extraction
        # was not. Em and en dashes still separate, since those are punctuation rather
        # than part of a word.
        toks = [t for t in re.split(r"[\s,;:—–]+", native) if t and not re.fullmatch(r"[-–—]+", t)]
        native_toks: list[str] = []
        for t in reversed(toks):
            if re.search(r"[A-Za-z0-9$\\]", t):
                break
            native_toks.insert(0, t)
            # an n-word English term maps to at most n+1 words of Indic text
            if len(native_toks) >= len(eng.split()) + 1:
                break
        if not native_toks:
            continue
        # The term core is the LAST n tokens for an n-word English term; the extra token
        # was only kept so a boundary could be found. Without this trim, "drawn normal"
        # and "which is normal" count as two renderings of one word.
        core = native_toks[-max(1, len(eng.split())):]
        nat = " ".join(core).strip(" .,:;–—")
        if nat and not re.fullmatch(r"[\W_]+", nat, flags=re.U):
            out.append((eng, nat))
    return out


# Indic consonants that carry the sound of an English consonant, enough to tell a
# sound-spelled English word from a real translation. Vowels are ignored: Indic scripts
# write them as marks and they vary by speaker.
ECHO = {
    "k": "कखकখକଖకఖ", "g": "गघগଗଘగఘ", "ch": "चछচଚଛచఛ", "j": "जझজଜଝజఝ",
    "t": "तथटठতথଟଠତଥటఠతథ", "d": "दधडढদধଡଢଦଧడఢదధ", "n": "नणनণନଣనణ",
    "p": "पफপফପଫపఫ", "b": "बभবভବଭబభ", "m": "मমମమ", "y": "यযଯయ",
    "r": "रরରర", "l": "लলଲలళ", "v": "वভୱవ", "w": "वୱవ",
    "s": "सशषসশষସଶଷసశష", "h": "हহହహ", "f": "फফଫఫ",
}
LATIN_TO_ECHO = {c: k for k, chars in ECHO.items() for c in chars}


def skeleton(text: str) -> str:
    """Consonant skeleton of Indic text, in Latin, for comparison with an English word."""
    return "".join(LATIN_TO_ECHO.get(c, "") for c in text)


def eng_skeleton(word: str) -> str:
    out, i = [], 0
    w = word.lower()
    while i < len(w):
        if w[i:i + 2] in ("ch", "sh", "th", "ph"):
            out.append({"ch": "ch", "sh": "s", "th": "t", "ph": "f"}[w[i:i + 2]])
            i += 2
            continue
        if w[i] in "kgjtdnpbmyrlvwshfcqxz":
            out.append({"c": "k", "q": "k", "x": "ks", "z": "j"}.get(w[i], w[i]))
        i += 1
    return "".join(out)


def looks_transliterated(eng: str, native: str) -> bool:
    """Is the native rendering the English word sound-spelled rather than translated?

    This is the defect the report names: Odia wrote ରିଫ୍ରାକ୍ସନ୍ for refraction instead of
    ପ୍ରତିସରଣ. Reported, never failed outright — some transliterations are the established
    term (there is no Hindi word for sine; साइन is what the textbooks print).
    """
    for e in eng.split():
        if len(e) < 4:
            continue
        es = eng_skeleton(e)
        if len(es) < 3:
            continue
        for n in native.split():
            ns = skeleton(n)
            if len(ns) >= 3 and (es in ns or ns in es):
                return True
    return False


def collapse(variants: set[str]) -> set[str]:
    """Drop renderings that are only a longer lead-in to another one.

    Indic languages put the head noun last and the bracket follows the term, so the term
    itself is a SUFFIX of whatever was captured. "drawn normal" and "which is normal" are
    the same term with different participles in front; only a genuinely different word is
    a terminology defect. Keeping the shortest of each suffix chain removes three flags
    that were grammar, not vocabulary.

    Inflection and lead-in words both have to be absorbed. Odia writes ଶୂନ୍ୟସ୍ଥାନ in one
    place and ଶୂନ୍ୟସ୍ଥାନରେ ("in a vacuum") in another — one word with a case suffix — and
    captures the same term behind different particles ("ଏବଂ ଆପତନ କୋଣ" / "ହେଉଛି ଆପତନ କୋଣ").
    Neither is a suffix of the other, so compare the shared TOKEN suffix instead, and for
    single words the shared stem.
    """
    def same(a: str, b: str) -> bool:
        if a in b or b in a:
            return True
        ta, tb = a.split(), b.split()
        shared = 0
        for x, y in zip(reversed(ta), reversed(tb)):
            if x != y:
                break
            shared += 1
        if shared and shared * 2 >= min(len(ta), len(tb)):
            return True
        if len(ta) == len(tb) == 1:
            stem = min(len(a), len(b))
            common = 0
            for x, y in zip(a, b):
                if x != y:
                    break
                common += 1
            return stem >= 4 and common >= 0.6 * stem
        return False

    kept: list[str] = []
    for v in sorted(variants, key=len):
        if not any(same(v, k) for k in kept):
            kept.append(v)
    return set(kept)


# Genitive and linking particles, which a pinned term omits but running prose needs.
PARTICLES = {"की", "के", "का", "को", "में", "से", "ର", "ରେ", "ଏବଂ", "ଯୋଗୁଁ",
             "యొక్క", "మరియు", "నుండి"}


def destem(s: str) -> str:
    return " ".join(w for w in s.split() if w not in PARTICLES)


def overlaps(a: str, b: str) -> bool:
    """Is the pinned term present in what the page wrote, grammar aside?

    Two kinds of grammar have to be seen through. Hindi and Odia insert separate particles
    (प्रकाश की किरण for the pinned प्रकाश किरण), which `destem` removes. Telugu is
    agglutinative, so case endings fuse onto the word itself — the pinned విరళ యానకం
    appears as విరళ యానకానికి in the dative, and కాంతిశాస్త్రం as కాంతిశాస్త్రానికి. Those
    are the right term correctly declined, so compare on the shared stem.

    The threshold has to leave real defects visible, and it does: సందీగ్ధ vs సందిగ్ధ (a
    mistyped vowel length) and क्राउन ग्लास vs क्राउन काँच (a transliteration where a real
    word exists) both diverge too early to pass.
    """
    x, y = destem(a), destem(b)
    if not x or not y:
        return False
    if x in y or y in x:
        return True
    common = 0
    for p, q in zip(x, y):
        if p != q:
            break
        common += 1
    return common >= 0.7 * min(len(x), len(y))


def latin_ratio(s: str) -> float:
    letters = [c for c in s if c.isalpha()]
    if not letters:
        return 0.0
    return sum("LATIN" in unicodedata.name(c, "") for c in letters) / len(letters)


INFLECTION = r"(?:s|es|ed|ing|ise|ises|ised|ising|ize|izes|ized|izing)?"


def pinned_for(lang: str, subject: str | None = None) -> dict[str, str]:
    """The glossary terms pinned for one language, or {} if there is no glossary yet.

    `subject` keeps a pin to the subject whose pages it was harvested from. It has to
    match build_context.glossary_for, which has the reasoning: several pinned terms are
    ordinary English words too, and demanding the maths rendering of "product" on a
    biology page about milk products held 8 good pages.
    """
    if not GLOSSARY.exists():
        return {}
    doc = json.loads(GLOSSARY.read_text(encoding="utf-8"))
    from_subject = doc.get("subjects", {})
    return {en.lower(): langs[lang]
            for en, langs in doc.get("terms", {}).items()
            if lang in langs
            and (subject is None or subject in from_subject.get(en, [subject]))}


def pin_present(want: str, page: str) -> bool:
    """Is the pinned rendering on the page, allowing for inflection?

    An exact substring test looks right and is wrong, because these languages fuse case
    endings onto the noun. Measured against the pins already in the glossary: Telugu wrote
    భాజ్యత for pinned భాజ్యం, కారణాంకాలను for కారణాంకం, యానకానికి for the యానకం in
    విరళ యానకం, గొట్టాన్ని for గొట్టం and కాంతిశాస్త్రానికి for కాంతిశాస్త్రం -- five
    correct pages out of twelve, every one of which an exact test would have sent back for
    a paid retry. Match a stem prefix of each word instead, which still exposes the real
    deviations: సందీగ్ధ for సందిగ్ధ (a mistyped vowel), गति where चाल is pinned, and
    क्राउन ग्लास where क्राउन काँच is pinned.
    """
    if want in page:
        return True
    return all(w[:max(3, int(len(w) * 0.7))] in page for w in want.split())


def localisation_problems(page: str, english: str, lang: str,
                          declared: list[str] | None = None,
                          subject: str | None = None) -> list[str]:
    """Faults in a localised page, checked against the English page it was written from.

    This exists to be a RETRY CONDITION, not a report. Until it was wired in,
    structural_problems() was gated behind `if lang == "en"`, so a Hindi, Telugu or Odia
    page was published on one test alone -- that its source tags survived. Everything a
    reader would notice about a bad localisation (half the sections, a changed number, a
    term spelled out in Indic letters instead of translated) went unchecked at generation
    time, and was only ever caught afterwards by a human running this script by hand.

    Every test here is language-independent on purpose. Numbers, formulas and section
    counts are the same glyphs in every script, so they prove the two pages say the same
    thing without the checker needing to read the language.
    """
    problems = []

    en_heads, my_heads = heads(english), heads(page)
    if len(en_heads) != len(my_heads):
        problems.append(f"sections: {len(my_heads)} sections, English has {len(en_heads)}")

    en_nums, my_nums = numbers(english), numbers(page)
    if my_nums != en_nums:
        # The bracket convention duplicates any number inside a glossed term. The Odia
        # temperature page wrote କୋଭିଡ୍-୧୯ (COVID-19) -- the name once in Odia digits and
        # once in Latin -- so "19" counted twice against the English page's once and the
        # page was held with nothing wrong on it, under an empty reason ("counts differ",
        # because the sets are equal and only the multiplicity differs). The prompt ASKS
        # for that gloss, so it is not evidence about the numbers.
        #
        # The retry is only ACCEPTED when it reconciles exactly, and that condition is
        # the whole point: dropping every Latin bracket outright also drops legitimately
        # parenthesised numbers, which broke 9 already-published pages -- the Hindi
        # divisibility rules page lost "(99, 999)" and Snell's law lost "(30 degrees)",
        # turning a page that agreed with its English into one missing four numbers.
        # Allowing the stripped view to win only on an exact match means this can forgive
        # a duplicate but can never manufacture a shortfall.
        without_gloss = numbers(LATIN_GLOSS.sub("", page))
        if Counter(without_gloss) == Counter(en_nums):
            my_nums = without_gloss
    if en_nums != my_nums:
        lost = sorted(set(en_nums) - set(my_nums))
        added = sorted(set(my_nums) - set(en_nums))
        detail = (f"dropped {lost[:4]}" if lost else "") + \
                 (" " if lost and added else "") + (f"invented {added[:4]}" if added else "")
        problems.append(f"numbers: {detail or 'counts differ'}")

    # Compared as SETS of distinct formulas. The point of this test is that a formula must
    # be carried across rather than dropped or invented, and comparing multisets measured
    # formatting instead: Divisibility Rules te had the identical 39 distinct formulas but
    # wrote "$2$" four times where English wrote it five, and Addition and Subtraction te
    # differed only by a comma falling inside one span rather than outside it. Both were
    # held with nothing actually wrong on the page.
    en_math, my_math = set(maths(english)), set(maths(page))
    if en_math != my_math:
        # Name a formula that actually differs. Reporting only the counts produced
        # "35 formulas, English has 35", which tells the reader nothing and looks like a
        # bug in the checker rather than a fault on the page.
        lost = [m for m in en_math if m not in my_math]
        added = [m for m in my_math if m not in en_math]
        detail = (f"missing {lost[0][:40]!r}" if lost else
                  f"invented {added[0][:40]!r}" if added else
                  f"{len(my_math)} vs {len(en_math)}")
        problems.append(f"formulas: {detail} -- a formula must be copied, not rewritten")

    # The pins are the whole point of the glossary, and before this they were injected into
    # the prompt and then never verified on output. A pin is only required when the English
    # page really uses the term, matched the same way build_context.glossary_for matches it.
    pins = pinned_for(lang, subject)
    low_en = english.lower()
    for en, want in pins.items():
        if not re.search(rf"\b{re.escape(en)}{INFLECTION}\b", low_en):
            continue
        if not pin_present(want, page):
            problems.append(f"glossary: '{en}' should read '{want}' but that does not "
                            f"appear on the page")

    # Bracketing is what makes the rendering harvestable into the glossary. A term the
    # model declared but never bracketed cannot be pinned, so the NEXT page is free to
    # render it differently. Tolerated below a threshold: the list is model-made and may
    # name something the page mentions only in passing.
    if declared:
        got = {e for e, _ in term_pairs(page)}
        missed = [d for d in declared if d not in got]
        if len(missed) > max(2, len(declared) * 0.4):
            problems.append(f"brackets: {len(missed)}/{len(declared)} declared terms are "
                            f"not bracketed with their English word ({missed[:4]})")

    return problems


def main() -> None:
    ap = argparse.ArgumentParser(description="Audit localised pages against English")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    glossary = json.loads(GLOSSARY.read_text(encoding="utf-8")) if GLOSSARY.exists() else {}

    en_pages = [p for p in sorted(PAGES.glob("**/*.md"))
                if not re.search(r"\.(hi|te|od)\.md$", p.name)]
    renderings: dict[str, defaultdict] = {
        lang: defaultdict(lambda: defaultdict(set)) for lang in LANGS}
    rows: list[tuple[str, str, list[str]]] = []
    missing: list[pathlib.Path] = []

    print("CONTENT PARITY - numbers, formulas, tags and sections vs the English page\n")
    for en in en_pages:
        locs = [(lang, en.with_name(en.name.replace(".md", f".{lang}.md")))
                for lang in LANGS]
        if not any(p.exists() for _, p in locs):
            missing.append(en)
            continue
        eb = body_of(en)
        en_n, en_m, en_t, en_h = numbers(eb), maths(eb), tags(eb), heads(eb)
        label = f"{en.parent.parent.name}/{en.parent.name}/{en.stem}"
        print(f"  {label}   (en: {len(en_h)} sections, {len(set(en_n))} numbers, "
              f"{len(en_m)} formulas, {len(en_t)} tags)")
        for lang, p in locs:
            if not p.exists():
                print(f"      {lang}: MISSING")
                continue
            lb = body_of(p)
            ln, lm, lt, lh = numbers(lb), maths(lb), tags(lb), heads(lb)
            faults = []
            if len(lh) != len(en_h):
                faults.append(f"{len(lh)} sections vs {len(en_h)}")
            lost = sorted(set(en_n) - set(ln))
            added = sorted(set(ln) - set(en_n))
            if lost:
                faults.append(f"numbers missing {lost[:6]}")
            if added:
                faults.append(f"numbers invented {added[:6]}")
            fm_lost = len(set(en_m) - set(lm))
            if fm_lost:
                faults.append(f"{fm_lost}/{len(en_m)} formulas differ")
            if en_t and not lt:
                faults.append("ALL citation tags lost")
            elif en_t and len(lt) < 0.7 * len(en_t):
                faults.append(f"only {len(lt)}/{len(en_t)} tags kept")
            if latin_ratio(lb) > 0.5:
                faults.append(f"{latin_ratio(lb):.0%} Latin letters - not in script")
            rows.append((label, lang, faults))
            print(f"      {lang}: {'; '.join(faults) if faults else 'parity ok'}")
            for eng, nat in term_pairs(lb):
                renderings[lang][eng][label].add(nat)

    print("\nTERMINOLOGY - does one English term get one rendering per language?\n")
    inconsistent = 0
    for lang in LANGS:
        print(f"  {NAMES[lang]}:")
        shown = False
        for eng, per_page in sorted(renderings[lang].items()):
            variants = collapse(set().union(*per_page.values()))
            if len(variants) > 1:
                inconsistent += 1
                shown = True
                print(f"      INCONSISTENT  '{eng}' -> {sorted(variants)}")
                for pg, v in sorted(per_page.items()):
                    print(f"                      {pg}: {sorted(v)}")
            elif args.verbose:
                shown = True
                plural = "s" if len(per_page) > 1 else ""
                print(f"      ok  '{eng}' -> {sorted(variants)[0]}  "
                      f"({len(per_page)} page{plural})")
        if not shown:
            print("      no term pairings found" if not renderings[lang]
                  else "      all terms consistent")

    print("\nTRANSLITERATION - is the term sound-spelled instead of translated?\n")
    echoes = 0
    for lang in LANGS:
        hits = []
        pinned_for = glossary.get("terms", {})
        for eng, per_page in sorted(renderings[lang].items()):
            ok = (pinned_for.get(eng) or {}).get(lang)
            for nat in collapse(set().union(*per_page.values())):
                if ok and (ok in nat or nat in ok):
                    continue          # human-approved in the glossary
                if looks_transliterated(eng, nat):
                    hits.append(f"'{eng}' -> {nat}")
        echoes += len(hits)
        print(f"  {NAMES[lang]}: {'; '.join(hits) if hits else 'none'}")
    print("  (judge each by hand: 'sine' is साइन in Hindi textbooks and that is correct)")

    # The file nests everything under "terms"; iterating the top level only ever saw
    # "_comment" and "terms", so this check silently passed everything before.
    terms = glossary.get("terms", glossary) if isinstance(glossary, dict) else {}
    if terms:
        print("\nGLOSSARY COMPLIANCE - pinned terms, where a page names them\n")
        for lang in LANGS:
            bad = []
            for eng, per_lang in terms.items():
                pinned = per_lang.get(lang) if isinstance(per_lang, dict) else None
                if not pinned:
                    continue
                seen = renderings[lang].get(eng.lower())
                used = collapse(set().union(*seen.values())) if seen else set()
                for u in used:
                    # Genitive particles sit INSIDE the term: "light ray" is correctly
                    # प्रकाश की किरण, and the glossary pins प्रकाश किरण. Compare with the
                    # particles removed, or every such term reads as a deviation.
                    if not overlaps(u, pinned):
                        bad.append(f"'{eng}': page says {u!r}, glossary pins {pinned!r}")
            print(f"  {NAMES[lang]}: {'; '.join(bad) if bad else 'no conflicts'}")

    clean = sum(1 for _, _, f in rows if not f)
    print(f"\n{clean}/{len(rows)} localised pages at full parity with English")
    print(f"{inconsistent} English term(s) with more than one rendering in a language")
    print(f"{echoes} term(s) that may be sound-spelled rather than translated")
    if missing:
        print(f"{len(missing)} English pages have NO localisation yet:")
        for m in missing:
            print(f"    {m.parent.parent.name}/{m.parent.name}/{m.stem}")


if __name__ == "__main__":
    main()
