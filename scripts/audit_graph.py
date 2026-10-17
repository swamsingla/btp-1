#!/usr/bin/env python3
"""
Audit the knowledge graphs against textbook evidence
=====================================================
Reads the graphs plus data/intermediate/concept_evidence/*.jsonl and produces the
lists that the graph fixes work from:

  A. no_evidence     — concept-grade pairs no passage supports
                       (wrong grade, or a genuine ICSE/state-board-only concept)
  B. grade_mismatch  — the books support the concept much better in another grade
  C. late_prereq     — prerequisite first taught later than the concept needs it,
                       now re-checked against the books
  D. unclaimed       — book sections no concept matched: candidate missing concepts

Output: data/intermediate/concept_evidence/audit.json  (+ a readable summary)

Nothing here edits the graph. The lists are evidence for a human/Claude pass.

Usage:
  python scripts/audit_graph.py
  python scripts/audit_graph.py --show no_evidence --limit 20
"""

import argparse
import json
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
EV_DIR = BASE_DIR / "data" / "intermediate" / "concept_evidence"
INDEX_PASSAGES = BASE_DIR / "data" / "intermediate" / "index" / "passages.jsonl"
GRAPHS = {
    "maths": BASE_DIR / "data" / "knowledge_graph" / "maths" / "graph.json",
    "science": BASE_DIR / "data" / "knowledge_graph" / "science" / "graph.json",
}
STRONG = 0.78
BETTER_BY = 0.06        # another grade must beat the assigned one by this much to count


def load_evidence(subject: str) -> list[dict]:
    path = EV_DIR / f"{subject}.jsonl"
    if not path.exists():
        raise SystemExit(f"missing {path} — run match_concepts.py first")
    return [json.loads(l) for l in path.open(encoding="utf-8")]


def audit_subject(subject: str) -> dict:
    graph = json.loads(GRAPHS[subject].read_text(encoding="utf-8"))
    concepts = graph["concepts"]
    evidence = load_evidence(subject)
    by_slug: dict[str, dict[int, dict]] = defaultdict(dict)
    for rec in evidence:
        by_slug[rec["slug"]][rec["grade"]] = rec

    # A. pairs with no textbook support
    no_evidence = [
        {"slug": r["slug"], "name": r["canonical_name"], "grade": r["grade"],
         "area": r["area"], "best_cosine": r["best_cosine"]}
        for r in evidence if r["evidence"] == "none"
    ]

    # B. supported far better in a grade the concept is not assigned to
    # (needs the every-grade matrix: match_concepts.py --all-grades)
    grade_mismatch = []
    matrix_path = EV_DIR / f"{subject}_grades.json"
    matrix = json.loads(matrix_path.read_text(encoding="utf-8")) if matrix_path.exists() else {}
    for slug, per_grade in matrix.items():
        if slug not in concepts:
            continue
        assigned = set(concepts[slug]["grades"])
        best_assigned = max((per_grade.get(str(g), 0.0) for g in assigned), default=0.0)
        best_other_grade, best_other = max(
            ((int(g), s) for g, s in per_grade.items() if int(g) not in assigned),
            key=lambda gs: gs[1], default=(None, 0.0),
        )
        if best_other_grade is not None and best_other > best_assigned + BETTER_BY:
            grade_mismatch.append({
                "slug": slug, "name": concepts[slug]["canonical_name"],
                "assigned_grades": sorted(assigned), "better_grade": best_other_grade,
                "assigned_cosine": round(best_assigned, 3), "other_cosine": round(best_other, 3),
            })
    grade_mismatch.sort(key=lambda d: d["assigned_cosine"] - d["other_cosine"])

    # C. prerequisites first taught after the concept that needs them
    late_prereq = []
    for slug, c in concepts.items():
        need = min(c["grades"])
        for pre in c.get("prerequisites", []):
            p = concepts.get(pre)
            if not p or min(p["grades"]) <= need:
                continue
            support = {g: r["best_cosine"] for g, r in by_slug.get(pre, {}).items()}
            earliest_supported = min((g for g, s in support.items() if s >= STRONG), default=None)
            late_prereq.append({
                "concept": slug, "concept_name": c["canonical_name"], "needed_by_grade": need,
                "prerequisite": pre, "prereq_name": p["canonical_name"],
                "prereq_grades": sorted(p["grades"]),
                "prereq_earliest_strong_grade": earliest_supported,
                "verdict": ("graph grade looks wrong" if earliest_supported and earliest_supported <= need
                            else "edge or grade needs a human decision"),
            })

    # D. book sections nothing matched
    # "covers" is every passage a concept reaches, not just the few kept as generation
    # context; counting coverage from the context list made large chapters look
    # unclaimed purely because one concept can only carry so many context passages.
    claimed = {pid for r in evidence for pid in r.get("covers") or
               [h["passage_id"] for h in r["hits"]]}
    subjects = {"maths"} if subject == "maths" else {"science", "physics", "chemistry", "biology"}
    by_section: dict[tuple, dict] = {}
    for line in INDEX_PASSAGES.open(encoding="utf-8"):
        p = json.loads(line)
        if p["subject"] not in subjects:
            continue
        key = (p["grade"], p["subject"], p["chapter"], p["section"])
        slot = by_section.setdefault(key, {"total": 0, "claimed": 0, "prose": 0})
        slot["total"] += 1
        slot["prose"] += p["kind"] == "text"
        slot["claimed"] += p["id"] in claimed

    # Exercises, summaries and question sets are not concept content, so they would only
    # add noise to a "missing concepts" list. Judged on the passages' own kind rather
    # than on words in the heading: build_passages now splits those blocks out and
    # labels them, and a heading like "The 'Why' Question for Adolescence" is prose.
    unclaimed = sorted(
        ({"grade": k[0], "subject": k[1], "chapter": k[2], "section": k[3],
          "passages": v["total"], "prose": v["prose"], "claimed": v["claimed"]}
         for k, v in by_section.items()
         if v["claimed"] == 0 and v["prose"] >= 2 and k[3]),
        key=lambda d: -d["passages"],
    )

    return {"no_evidence": no_evidence, "grade_mismatch": grade_mismatch,
            "late_prereq": late_prereq, "unclaimed": unclaimed}


def main() -> None:
    p = argparse.ArgumentParser(description="Audit graphs against textbook evidence")
    p.add_argument("--show", choices=["no_evidence", "grade_mismatch", "late_prereq", "unclaimed"])
    p.add_argument("--subject", choices=list(GRAPHS))
    p.add_argument("--limit", type=int, default=15)
    args = p.parse_args()

    report = {s: audit_subject(s) for s in ([args.subject] if args.subject else list(GRAPHS))}
    out = EV_DIR / "audit.json"
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    for subject, lists in report.items():
        print(f"\n=== {subject}")
        for name, items in lists.items():
            print(f"  {name:15} {len(items)}")
    print(f"\nfull report: {out.relative_to(BASE_DIR).as_posix()}")

    if args.show:
        for subject, lists in report.items():
            print(f"\n--- {subject}: {args.show}")
            for item in lists[args.show][:args.limit]:
                print("   ", json.dumps(item, ensure_ascii=False))


if __name__ == "__main__":
    main()
