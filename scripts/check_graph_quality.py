#!/usr/bin/env python3
"""
Quality checker for Stage 2 knowledge graph output.
Usage:
  python3 scripts/check_graph_quality.py --subject maths
  python3 scripts/check_graph_quality.py          # checks all available
"""
import argparse
import json
from pathlib import Path
from collections import Counter

BASE_DIR = Path(__file__).resolve().parent.parent
KG_DIR = BASE_DIR / "data" / "knowledge_graph"


def check_subject(subject: str) -> None:
    path = KG_DIR / "graph_by_subject" / f"{subject}.json"
    if not path.exists():
        print(f"[{subject}] ❌ File not found: {path}")
        return

    g = json.load(open(path))
    concepts = g.get("concepts", {})
    edges = g.get("edges", [])
    grade_views = g.get("grade_views", {})

    print(f"\n{'='*60}")
    print(f"  SUBJECT: {subject.upper()}")
    print(f"{'='*60}")
    print(f"  Total concepts : {g.get('total_concepts', len(concepts))}")
    print(f"  Total edges    : {g.get('total_edges', len(edges))}")
    print(f"  Grades covered : {sorted(grade_views.keys())}")

    # ── Prerequisite coverage ──────────────────────────────────────────────
    with_prereqs = [c for c in concepts.values() if c.get("prerequisites")]
    no_prereqs   = [c for c in concepts.values() if not c.get("prerequisites")]
    leads_to     = [c for c in concepts.values() if c.get("leads_to")]
    print(f"\n  Prerequisite coverage:")
    print(f"    Concepts WITH prerequisites : {len(with_prereqs)}/{len(concepts)}")
    print(f"    Concepts with leads_to      : {len(leads_to)}/{len(concepts)}")
    print(f"    Isolated (no prereqs+leads) : {sum(1 for c in concepts.values() if not c.get('prerequisites') and not c.get('leads_to'))}")

    # ── Domain/Area distribution ───────────────────────────────────────────
    domains = Counter(c.get("domain", "?") for c in concepts.values())
    print(f"\n  Domains ({len(domains)} total):")
    for d, cnt in domains.most_common(8):
        print(f"    {cnt:3d}  {d}")

    # ── Grade view health ──────────────────────────────────────────────────
    print(f"\n  Grade views:")
    for grade in sorted(grade_views.keys(), key=lambda x: int(x)):
        gv = grade_views[grade]
        ep = gv.get("entry_points", [])
        print(f"    Grade {grade}: {gv.get('count', 0):3d} concepts, "
              f"{len(ep)} entry points  "
              f"{'✓' if ep else '⚠ NO ENTRY POINTS'}")

    # ── Sample concepts with full data ────────────────────────────────────
    print(f"\n  === SAMPLE CONCEPTS (3) ===")
    for slug, c in list(concepts.items())[:3]:
        print(f"\n  [{c.get('domain','?')} > {c.get('area','?')}]")
        print(f"  Name     : {c['canonical_name']}")
        print(f"  Grades   : {c.get('grades', [])}")
        print(f"  Prereqs  : {c.get('prerequisites', [])}")
        print(f"  Leads to : {c.get('leads_to', [])}")
        print(f"  Aliases  : {c.get('aliases', [])}")
        print(f"  Boards   : {c.get('source_boards', [])}")

    # ── Flag quality issues ───────────────────────────────────────────────
    issues = []
    no_domain = [c["canonical_name"] for c in concepts.values() if not c.get("domain")]
    no_grades = [c["canonical_name"] for c in concepts.values() if not c.get("grades")]
    empty_leads = sum(1 for c in concepts.values() if not c.get("leads_to"))

    if no_domain:
        issues.append(f"  ⚠  {len(no_domain)} concepts missing domain field")
    if no_grades:
        issues.append(f"  ⚠  {len(no_grades)} concepts missing grades field")
    if empty_leads > len(concepts) * 0.7:
        issues.append(f"  ⚠  {empty_leads}/{len(concepts)} concepts have no leads_to (poor edge coverage)")
    if len(with_prereqs) < len(concepts) * 0.3:
        issues.append(f"  ⚠  Only {len(with_prereqs)}/{len(concepts)} concepts have prerequisites (sparse graph)")

    if issues:
        print(f"\n  QUALITY ISSUES:")
        for i in issues:
            print(i)
    else:
        print(f"\n  ✅ No major quality issues detected")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--subject", help="Subject to check (default: all available)")
    args = p.parse_args()

    if args.subject:
        check_subject(args.subject)
    else:
        available = sorted((KG_DIR / "graph_by_subject").glob("*.json"))
        if not available:
            print("No graph files found in", KG_DIR / "graph_by_subject")
            return
        for f in available:
            check_subject(f.stem)


if __name__ == "__main__":
    main()
