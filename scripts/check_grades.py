#!/usr/bin/env python3
"""
Check every concept's grade tags against the books, by term presence
=====================================================================
`audit_graph.py` compares embedding similarity across grades. That is biased:
Grades 11-12 hold 3-4x more prose than 6-10, so a deeper treatment always outscores
the grade where a topic is introduced, and the audit proposes moving concepts up
that are correctly placed (it wanted Friction moved from Grade 8 to Grade 11).

Counting the concept's own distinctive word per grade does not have that bias. If
"parallelogram" appears 0 times in Grade 7 and 25 times in Grade 8, the topic is in
Grade 8 whatever the cosine says.

The word is the rarest content word of the concept name, since that is the most
specific one ("parallelogram" out of "Area of Parallelogram"). Concepts whose rarest
word is still common in the corpus cannot be judged this way and are reported
separately rather than guessed at.

Verdicts:
  wrong_grade   term never appears in any assigned grade, but is solid elsewhere
  not_in_corpus term appears nowhere at all -> ghost concept, candidate for removal
  thin          barely present where assigned, far stronger in another grade
  generic       the name has no word specific enough to test
  ok            term is present where the graph says it is taught

Usage:
  python scripts/check_grades.py
  python scripts/check_grades.py --show wrong_grade
  python scripts/check_grades.py --subject science --show thin --limit 40
"""

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PASSAGE_DIR = BASE_DIR / "data" / "intermediate" / "passages"
GRAPHS = {
    "maths": BASE_DIR / "data" / "knowledge_graph" / "maths" / "graph.json",
    "science": BASE_DIR / "data" / "knowledge_graph" / "science" / "graph.json",
}
OUT_PATH = BASE_DIR / "data" / "intermediate" / "concept_evidence" / "grade_check.json"

WORD = re.compile(r"[a-z]+")
GENERIC_DF = 0.03        # a word in >3% of passages cannot identify a topic
MIN_ELSEWHERE = 3        # passages needed elsewhere before calling a tag wrong
THIN_RATIO = 5           # another grade must have this many times more to call it thin
THIN_FLOOR = 8           # ...and at least this many passages

# Words that carry no topic information in a concept name.
STOP = {
    "the", "and", "of", "in", "a", "an", "to", "for", "with", "from", "its", "by",
    "or", "on", "as", "at", "its", "their", "using", "based", "types", "type",
    "basic", "concepts", "concept", "introduction", "intro", "properties",
    "property", "law", "laws", "rule", "rules", "theorem", "formula", "formulae",
    "method", "methods", "system", "systems", "form", "forms", "part", "parts",
    "kind", "kinds", "other", "more", "some", "general", "simple", "problems",
}


def stem(word: str) -> str:
    if word.endswith("ies") and len(word) > 4:
        return word[:-3] + "y"
    if word.endswith("es") and len(word) > 4:
        return word[:-2]
    if word.endswith("s") and not word.endswith("ss") and len(word) > 3:
        return word[:-1]
    return word


def load_passages() -> tuple[dict, Counter, int]:
    """stems present per (family, grade), plus corpus-wide document frequency."""
    per_slot: dict[tuple[str, int], Counter] = defaultdict(Counter)
    corpus = Counter()
    total = 0
    for path in sorted(PASSAGE_DIR.glob("*.jsonl")):
        for line in path.open(encoding="utf-8"):
            p = json.loads(line)
            fam = "maths" if p["subject"] == "maths" else "science"
            stems = {stem(w) for w in WORD.findall(p["text"].lower())}
            per_slot[(fam, p["grade"])].update(stems)
            corpus.update(stems)
            total += 1
    return per_slot, corpus, total


def pick_term(name: str, corpus: Counter, total: int) -> str | None:
    """The rarest content word of the name — the most specific thing to look for."""
    words = {stem(w) for w in WORD.findall(name.lower())
             if w not in STOP and len(w) > 3}
    words = {w for w in words if corpus.get(w)}
    if not words:
        return None
    term = min(words, key=lambda w: corpus[w])
    return term if corpus[term] <= GENERIC_DF * total else None


def check(subject: str, per_slot: dict, corpus: Counter, total: int) -> list[dict]:
    graph = json.loads(GRAPHS[subject].read_text(encoding="utf-8"))
    grades = sorted({g for (fam, g) in per_slot if fam == subject})
    rows = []
    for slug, c in graph["concepts"].items():
        assigned = sorted(c["grades"])
        term = pick_term(c["canonical_name"], corpus, total)
        if term is None:
            rows.append({"slug": slug, "name": c["canonical_name"], "grades": assigned,
                         "term": None, "verdict": "generic", "per_grade": {}})
            continue

        per_grade = {g: per_slot[(subject, g)].get(term, 0) for g in grades}
        here = max((per_grade[g] for g in assigned if g in per_grade), default=0)
        others = {g: n for g, n in per_grade.items() if g not in assigned}
        best_other_grade, best_other = max(others.items(), key=lambda kv: kv[1],
                                           default=(None, 0))

        if here == 0 and best_other == 0:
            verdict = "not_in_corpus"
        elif here == 0 and best_other >= MIN_ELSEWHERE:
            verdict = "wrong_grade"
        elif here == 0:
            verdict = "thin"
        elif best_other >= THIN_FLOOR and best_other >= THIN_RATIO * here:
            verdict = "thin"
        else:
            verdict = "ok"

        rows.append({"slug": slug, "name": c["canonical_name"], "grades": assigned,
                     "term": term, "verdict": verdict, "here": here,
                     "best_other_grade": best_other_grade, "best_other": best_other,
                     "per_grade": per_grade})
    return rows


def main() -> None:
    p = argparse.ArgumentParser(description="Check grade tags by term presence")
    p.add_argument("--subject", choices=list(GRAPHS))
    p.add_argument("--show", choices=["wrong_grade", "not_in_corpus", "thin", "generic", "ok"])
    p.add_argument("--limit", type=int, default=30)
    args = p.parse_args()

    per_slot, corpus, total = load_passages()
    print(f"indexed {total} passages\n")

    report = {}
    for subject in ([args.subject] if args.subject else list(GRAPHS)):
        rows = check(subject, per_slot, corpus, total)
        report[subject] = rows
        counts = Counter(r["verdict"] for r in rows)
        print(f"=== {subject}: {len(rows)} concepts")
        for v in ("ok", "wrong_grade", "thin", "not_in_corpus", "generic"):
            print(f"   {v:15}{counts.get(v, 0):>5}")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(report, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"\nwritten to {OUT_PATH.relative_to(BASE_DIR).as_posix()}")

    if args.show:
        for subject, rows in report.items():
            picked = [r for r in rows if r["verdict"] == args.show]
            print(f"\n--- {subject}: {args.show} ({len(picked)})")
            for r in sorted(picked, key=lambda r: -r.get("best_other", 0))[:args.limit]:
                spread = " ".join(f"{g}:{n}" for g, n in r["per_grade"].items() if n)
                print(f"   {r['name'][:34]:36} {str(r['grades']):10} "
                      f"'{r['term']}'  here={r.get('here')}  {spread}")


if __name__ == "__main__":
    main()
