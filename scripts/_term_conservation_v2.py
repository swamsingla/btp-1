# Term Conservation Extractor v2 - Programmatic + Validated
#
# Extracts technical terms that MUST be translated consistently across all
# Grade 9 Maths topic pages. Every term is validated to exist in source text.
#
# Strategy:
#   1. Parse **bold terms** - author-emphasized vocabulary definitions
#   2. Match against curated math vocabulary list
#   3. Extract named theorems/laws/identities
#   4. Cross-reference to find terms appearing in multiple pages
#
# Runs locally, no GPU, deterministic, zero failures.
# Output: data/intermediate/grade9_conservation_terms_v2.json

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent.parent
MD_ROOT = ROOT / "data" / "output" / "grade9" / "maths"
INTERMEDIATE = ROOT / "data" / "intermediate"
CHAPTERS = [1, 2, 3]
OUTPUT_FILE = INTERMEDIATE / "grade9_conservation_terms_v2.json"

# Curated math vocabulary for Grade 9 Ch1-3
MATH_VOCABULARY = {
    # Number systems (Ch1)
    "rational number", "irrational number", "real number", "natural number",
    "whole number", "integer", "rational numbers", "irrational numbers",
    "real numbers", "natural numbers", "whole numbers", "integers",
    "number line", "number system", "number systems",
    "square root", "cube root", "prime factorization",
    "numerator", "denominator", "fraction", "decimal expansion",
    "terminating decimal", "recurring decimal",
    "repeating block", "coprime", "coprime integers",
    "closure property", "commutative", "associative", "distributive",
    "radical", "radicand", "rationalize", "rationalisation",
    # Exponents (Ch1.5)
    "exponent", "base", "power", "rational exponent", "negative exponent",
    "laws of exponents",
    # Polynomials (Ch2)
    "polynomial", "polynomials", "monomial", "binomial", "trinomial",
    "monomials", "binomials", "trinomials",
    "variable", "constant", "coefficient", "coefficients",
    "degree", "leading coefficient", "algebraic expression",
    "algebraic expressions", "algebraic identity", "algebraic identities",
    "zero of a polynomial", "zeroes of a polynomial", "zero polynomial",
    "linear polynomial", "quadratic polynomial", "cubic polynomial",
    "factorisation", "factorization", "factor",
    # Coordinate geometry (Ch3)
    "cartesian system", "cartesian plane", "coordinate geometry",
    "coordinate plane", "perpendicular lines", "ordered pair",
    "x-axis", "y-axis", "x-coordinate", "y-coordinate",
    "origin", "quadrant", "quadrants", "abscissa", "ordinate", "axes",
}

# Blocklist - never count these as technical terms
BLOCKLIST = {
    "example", "example 1", "example 2", "example 3", "example 4", "example 5",
    "solution", "answer", "answers", "proof", "note", "hint", "warning", "tip",
    "grade", "grade 9", "chapter", "easy", "medium", "hard", "important", "key",
    "remember", "recall", "definition", "correction", "fix", "correct",
    "common mistakes", "exam tips", "exam tip", "memory aid", "student corner",
    "problem", "problem 1", "problem 2", "problem 3", "problem 4", "problem 5",
    "practice", "practice problems", "summary", "prerequisites", "introduction",
    "explanation", "key concepts", "related topics", "conclusion",
    "have you", "ever wondered", "this", "here", "the", "by the end",
    "always", "never", "substitution", "case", "case 1", "case 2", "step",
    "no", "yes", "rules", "terms", "examples", "memorize", "mistake",
    "result", "positive", "negative", "classification", "equations",
    "simplifying expressions", "all real numbers",
    "i", "ii", "iii", "iv", "v", "(i)", "(ii)", "(iii)",
    "irrational", "rational", "zero", "terminating", "non-terminating",
    "repeating", "lines", "points", "planes", "grid", "rhyme",
    "addition/subtraction", "multiplication", "division",
    "cannot be expressed", "always irrational", "always simplify radicals",
}


def read_all_topics():
    files = {}
    for ch in CHAPTERS:
        ch_dir = MD_ROOT / f"chapter{ch}"
        if not ch_dir.exists():
            continue
        for md_file in sorted(ch_dir.glob("*.md")):
            key = f"chapter{ch}/{md_file.name}"
            files[key] = md_file.read_text(encoding="utf-8")
    return files


def strip_latex(text):
    text = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.DOTALL)
    text = re.sub(r"\$[^\$\n]+?\$", " ", text)
    return text


def normalize(term):
    return re.sub(r"\s+", " ", term.lower().strip())


def extract_bold_terms(content):
    cleaned = strip_latex(content)
    bolds = re.findall(r"\*\*([^*]+?)\*\*", cleaned)
    terms = []
    for m in bolds:
        m = m.strip().rstrip(":")
        if len(m) < 3 or len(m) > 50:
            continue
        if normalize(m) in BLOCKLIST:
            continue
        # skip sentence-like
        if re.match(r"^(Have|Ever|This|Here|The |By |In |It |An? |For |Let )", m):
            continue
        if re.match(r"^\d|^\(|^\[", m):
            continue
        if m.startswith("$") or m.startswith("\\"):
            continue
        # skip if contains sentence verbs and is long
        if len(m.split()) > 3:
            if re.search(r"\b(is|are|was|were|has|have|can|will|should|must|that|which)\b", m.lower()):
                continue
        if "chapter" in m.lower():
            continue
        terms.append(m)
    return terms


def extract_named_theorems(content):
    found = set()
    patterns = [
        r"Remainder\s+Theorem",
        r"Factor\s+Theorem",
        r"Euclid'?s?\s+division\s+lemma",
        r"Fundamental\s+Theorem\s+of\s+Arithmetic",
        r"Commutative\s+law(?:\s+(?:for|of)\s+\w+)?",
        r"Associative\s+law(?:\s+(?:for|of)\s+\w+)?",
        r"Distributive\s+law",
    ]
    for pat in patterns:
        for m in re.finditer(pat, content, re.IGNORECASE):
            found.add(m.group(0).strip())
    # Identity I, II, etc.
    for m in re.finditer(r"Identity\s+(?:\d+|[IVX]+)", content):
        found.add(m.group(0).strip())
    # Theorem N, Law N
    for m in re.finditer(r"Theorem\s+\d+", content):
        found.add(m.group(0).strip())
    for m in re.finditer(r"Law\s+\d+", content):
        found.add(m.group(0).strip())
    return sorted(found)


def find_vocab_in_text(content):
    text_lower = content.lower()
    found = []
    for term in sorted(MATH_VOCABULARY, key=lambda t: -len(t)):
        if " " in term:
            if term in text_lower:
                found.append(term)
        else:
            if re.search(r"\b" + re.escape(term) + r"\b", text_lower):
                found.append(term)
    return found


def extract_notation(content):
    notations = set()
    for m in re.finditer(r"\\mathbb\{(\w)\}", content):
        notations.add(f"\\mathbb{{{m.group(1)}}}")
    for m in re.finditer(r"\b([a-zA-Z])\(([a-zA-Z])\)", content):
        notations.add(f"{m.group(1)}({m.group(2)})")
    text_lower = content.lower()
    for sym in ["x-axis", "y-axis", "x-coordinate", "y-coordinate"]:
        if sym in text_lower:
            notations.add(sym)
    return sorted(notations)


def count_in_text(term, content):
    return len(re.findall(re.escape(term), content, re.IGNORECASE))


def extract_page_terms(content):
    bold_terms = extract_bold_terms(content)
    theorems = extract_named_theorems(content)
    vocab = find_vocab_in_text(content)
    notation = extract_notation(content)

    seen = set()
    math_terms = []
    domain_phrases = []

    # Vocab matches first (curated, reliable)
    for t in vocab:
        n = normalize(t)
        if n not in seen:
            seen.add(n)
            if " " in t:
                domain_phrases.append(t)
            else:
                math_terms.append(t)

    # Bold terms that are genuinely new (not already in vocab)
    for t in bold_terms:
        n = normalize(t)
        if n not in seen and n not in BLOCKLIST:
            seen.add(n)
            if t.lower() in content.lower():
                if " " in t:
                    domain_phrases.append(t)
                else:
                    math_terms.append(t)

    # Conserve in English: notation + specific coordinate terms
    conserve = list(notation)
    for t in math_terms + domain_phrases:
        low = t.lower()
        if low in {"x-axis", "y-axis", "cartesian system", "cartesian plane"}:
            if t not in conserve:
                conserve.append(t)

    # Frequency for ranking
    freq = {}
    for t in math_terms + domain_phrases:
        freq[t] = count_in_text(t, content)

    return {
        "mathematical_terms": sorted(math_terms),
        "theorems_and_laws": theorems,
        "notation_terms": notation,
        "domain_phrases": sorted(domain_phrases),
        "conserve_in_english": sorted(set(conserve)),
        "term_frequency": dict(sorted(freq.items(), key=lambda x: -x[1])),
    }


def analyze_cross_page(all_pages, all_files):
    term_pages = defaultdict(set)

    for page_key, terms_dict in all_pages.items():
        combined = (
            terms_dict["mathematical_terms"]
            + terms_dict["domain_phrases"]
            + terms_dict["theorems_and_laws"]
        )
        for term in combined:
            n = normalize(term)
            if n in BLOCKLIST or len(n) < 3:
                continue
            term_pages[n].add(page_key)

    # Expand: check if term appears in pages where it was not boldly extracted
    for term_n, pages in list(term_pages.items()):
        for page_key, content in all_files.items():
            if page_key not in pages:
                if len(term_n) < 8:
                    if re.search(r"\b" + re.escape(term_n) + r"\b", content, re.IGNORECASE):
                        pages.add(page_key)
                elif term_n in content.lower():
                    pages.add(page_key)

    high = {}
    medium = {}
    for term, pages in sorted(term_pages.items(), key=lambda x: -len(x[1])):
        entry = {"term": term, "pages": sorted(pages), "count": len(pages)}
        if len(pages) >= 4:
            high[term] = entry
        elif len(pages) >= 2:
            medium[term] = entry

    return {"high_priority": high, "medium_priority": medium}


def gap_analysis(all_pages):
    glossary_file = INTERMEDIATE / "grade9_glossary.json"
    if not glossary_file.exists():
        return {"status": "no_glossary_found"}

    with open(glossary_file, encoding="utf-8") as f:
        glossary = json.load(f)

    glossary_norms = {normalize(t) for t in glossary}
    conservation_norms = set()
    for terms_dict in all_pages.values():
        for t in terms_dict["mathematical_terms"] + terms_dict["domain_phrases"]:
            conservation_norms.add(normalize(t))

    covered = conservation_norms & glossary_norms
    missing = conservation_norms - glossary_norms

    return {
        "glossary_size": len(glossary),
        "conservation_terms": len(conservation_norms),
        "covered_by_glossary": len(covered),
        "missing_from_glossary": sorted(missing),
    }


def main():
    print("=" * 60)
    print("Term Conservation v2 - Programmatic Extraction")
    print("=" * 60)

    files = read_all_topics()
    print(f"Found {len(files)} topic pages\n")

    all_pages = {}

    for key, content in files.items():
        topic_name = Path(key).stem
        terms = extract_page_terms(content)
        all_pages[key] = terms

        n_m = len(terms["mathematical_terms"])
        n_p = len(terms["domain_phrases"])
        n_t = len(terms["theorems_and_laws"])
        n_n = len(terms["notation_terms"])
        total = n_m + n_p + n_t + n_n

        print(f"  [{topic_name}] {total} terms (math={n_m} phrases={n_p} thm={n_t} notn={n_n})")
        freq = terms["term_frequency"]
        top5 = list(freq.items())[:5]
        if top5:
            print(f"    top: {', '.join(f'{t}({c})' for t,c in top5)}")

    # Cross-page
    print(f"\n{'='*60}")
    print("Cross-Page Consistency Analysis")
    print("=" * 60)

    cross = analyze_cross_page(all_pages, files)
    high = cross["high_priority"]
    med = cross["medium_priority"]

    print(f"\n  CRITICAL (4+ pages) - {len(high)} terms:")
    for term, info in high.items():
        print(f"    * {term} -> {info['count']} pages")

    print(f"\n  IMPORTANT (2-3 pages) - {len(med)} terms:")
    for term, info in med.items():
        print(f"    - {term} -> {info['count']} pages")

    # Gap analysis
    print(f"\n{'='*60}")
    print("Glossary Gap Analysis")
    print("=" * 60)

    gaps = gap_analysis(all_pages)
    if "missing_from_glossary" in gaps:
        print(f"  Glossary: {gaps['glossary_size']} terms")
        print(f"  Conservation: {gaps['conservation_terms']} terms")
        print(f"  Covered: {gaps['covered_by_glossary']}")
        missing = gaps["missing_from_glossary"]
        print(f"  Missing: {len(missing)}")
        for t in missing[:20]:
            print(f"    x {t}")
        if len(missing) > 20:
            print(f"    ... +{len(missing)-20} more")

    # Build output (strip frequency from per_page)
    clean_pages = {}
    for k, v in all_pages.items():
        clean_pages[k] = {
            "mathematical_terms": v["mathematical_terms"],
            "theorems_and_laws": v["theorems_and_laws"],
            "notation_terms": v["notation_terms"],
            "domain_phrases": v["domain_phrases"],
            "conserve_in_english": v["conserve_in_english"],
        }

    all_unique = set()
    for v in clean_pages.values():
        for cat_terms in v.values():
            all_unique.update(cat_terms)

    output = {
        "per_page": clean_pages,
        "cross_page": cross,
        "gap_analysis": gaps,
        "all_unique_terms": sorted(all_unique),
        "total_unique": len(all_unique),
        "pages_processed": len(clean_pages),
    }

    INTERMEDIATE.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}")
    print(f"Total unique conservation terms: {len(all_unique)}")
    print(f"Saved to: {OUTPUT_FILE}")
    print("=" * 60)


if __name__ == "__main__":
    main()
