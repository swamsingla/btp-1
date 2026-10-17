#!/usr/bin/env python3
"""
Knowledge Graph Sync — one master file per subject
===================================================
Masters (the ONLY graph files you should edit):
  data/knowledge_graph/maths/graph.json
  data/knowledge_graph/science/graph.json

For each subject this script:
  1. Validates the master: slug keys, broken prerequisites, leads_to and
     edges consistent with prerequisites, totals, cycles.
     If any check fails, nothing is written.
  2. Regenerates the derived files from the master:
       data/knowledge_graph/{subject}/graph_by_grade/grade{N}_{subject}.json
       data/knowledge_graph/{subject}/{subject}_visual.html
  3. Copies the master unchanged to the frontends:
       webapp/public/{subject}.json
       graph-viz/public/{subject}.json

Usage:
  python scripts/sync_graphs.py                   # validate + sync both subjects
  python scripts/sync_graphs.py --check           # validate only, write nothing
  python scripts/sync_graphs.py --subject maths   # one subject
  python scripts/sync_graphs.py --prune           # also delete stale graph_by_grade files
"""

import argparse
import json
import sys
from collections import defaultdict, deque
from pathlib import Path

from generate_visuals import build_html

BASE_DIR = Path(__file__).resolve().parent.parent
KG_DIR = BASE_DIR / "data" / "knowledge_graph"

SUBJECTS = {
    "maths": "Mathematics",
    "science": "Science",
}

FRONTEND_DIRS = [
    BASE_DIR / "webapp" / "public",
    BASE_DIR / "graph-viz" / "public",
]

VALID_GRADES = range(6, 13)
MAX_ERRORS_SHOWN = 10


def master_path(subject: str) -> Path:
    return KG_DIR / subject / "graph.json"


# ══════════════════════════════════════════════════════════════════════════════
# Validation
# ══════════════════════════════════════════════════════════════════════════════

def late_prerequisites(graph: dict) -> list[str]:
    """Prerequisites first taught later than the concept that lists them.

    Reported rather than rejected, because every instance of this found so far is a
    real relation that simply binds at the higher grade: types of mixtures really is a
    prerequisite for separation techniques, but at Grade 9, while the Grade 6 treatment
    of separation stands on its own. The graph cannot say "this edge applies from Grade
    9", so the edge is kept and the frontend hides a prerequisite the reader could not
    have met yet.

    This exists because editing a concept's grades silently breaks other concepts'
    chains. Removing Grade 6 from eight science concepts that the corpus has no Grade 6
    source for left five concepts depending on prerequisites taught two to three years
    later, and nothing said so -- the Grade 6 separation techniques page simply started
    showing "you should know this first: Mixtures, Grade 9".
    """
    concepts = graph["concepts"]
    out = []
    for slug, c in sorted(concepts.items()):
        first = min(c["grades"])
        for pre in c.get("prerequisites", []):
            if pre not in concepts:
                continue
            pre_first = min(concepts[pre]["grades"])
            if pre_first > first:
                out.append(f"{slug} {c['grades']} needs {pre} "
                           f"{concepts[pre]['grades']} — {pre_first - first} grade(s) later")
    return out


def validate(graph: dict) -> list[str]:
    """Return a list of problems with the graph (empty list = valid)."""
    errors: list[str] = []
    concepts = graph.get("concepts")
    edges = graph.get("edges")
    if not isinstance(concepts, dict) or not isinstance(edges, list):
        return ["graph must have a 'concepts' object and an 'edges' list"]

    # Per-concept fields and prerequisite references
    for slug, c in concepts.items():
        if c.get("slug") != slug:
            errors.append(f"{slug}: 'slug' field is {c.get('slug')!r}, expected key {slug!r}")
        if not c.get("canonical_name"):
            errors.append(f"{slug}: missing canonical_name")
        if not c.get("area"):
            errors.append(f"{slug}: missing area")
        grades = c.get("grades")
        if not grades or any(g not in VALID_GRADES for g in grades):
            errors.append(f"{slug}: grades must be a non-empty list within 6-12, got {grades!r}")
        prereqs = c.get("prerequisites", [])
        if len(prereqs) != len(set(prereqs)):
            errors.append(f"{slug}: duplicate prerequisites")
        for p in prereqs:
            if p == slug:
                errors.append(f"{slug}: lists itself as a prerequisite")
            elif p not in concepts:
                errors.append(f"{slug}: prerequisite {p!r} does not exist")

    prereq_pairs = {
        (p, slug)
        for slug, c in concepts.items()
        for p in c.get("prerequisites", [])
        if p in concepts
    }

    # leads_to must be exactly the reverse of prerequisites
    expected_leads: dict[str, set[str]] = defaultdict(set)
    for p, slug in prereq_pairs:
        expected_leads[p].add(slug)
    for slug, c in concepts.items():
        actual = set(c.get("leads_to", []))
        expected = expected_leads.get(slug, set())
        if actual != expected:
            missing = sorted(expected - actual)
            extra = sorted(actual - expected)
            errors.append(f"{slug}: leads_to out of sync (missing {missing}, extra {extra})")

    # edges list must match prerequisites exactly
    edge_pairs = [(e.get("from"), e.get("to")) for e in edges]
    if len(edge_pairs) != len(set(edge_pairs)):
        errors.append("edges: duplicate entries")
    bad_type = [e for e in edges if e.get("type") != "prerequisite"]
    if bad_type:
        errors.append(f"edges: {len(bad_type)} edge(s) with type other than 'prerequisite'")
    for f, t in sorted(set(edge_pairs) - prereq_pairs):
        errors.append(f"edges: {f} -> {t} is not in {t}'s prerequisites")
    for f, t in sorted(prereq_pairs - set(edge_pairs)):
        errors.append(f"edges: {f} -> {t} is missing from the edges list")

    # Totals
    if graph.get("total_concepts") != len(concepts):
        errors.append(f"total_concepts is {graph.get('total_concepts')}, actual {len(concepts)}")
    if graph.get("total_edges") != len(edges):
        errors.append(f"total_edges is {graph.get('total_edges')}, actual {len(edges)}")

    # Cycles (Kahn's algorithm: whatever cannot be ordered sits on a cycle)
    indegree = {slug: 0 for slug in concepts}
    children: dict[str, list[str]] = defaultdict(list)
    for p, slug in prereq_pairs:
        children[p].append(slug)
        indegree[slug] += 1
    queue = deque(s for s, d in indegree.items() if d == 0)
    ordered = 0
    while queue:
        node = queue.popleft()
        ordered += 1
        for child in children[node]:
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)
    if ordered != len(concepts):
        stuck = {s for s, d in indegree.items() if d > 0}
        errors.append("cycle: " + " -> ".join(find_cycle(stuck, prereq_pairs)))

    return errors


def find_cycle(stuck: set[str], prereq_pairs: set[tuple[str, str]]) -> list[str]:
    """Return one prerequisite cycle as [a, b, ..., a] (a -> b means a is needed for b).

    Every node left over by Kahn's algorithm has a leftover parent, so walking
    parent links from any leftover node must eventually repeat a node.
    """
    parents: dict[str, list[str]] = defaultdict(list)
    for p, slug in prereq_pairs:
        if p in stuck and slug in stuck:
            parents[slug].append(p)
    node = min(stuck)
    seen: dict[str, int] = {}
    path: list[str] = []
    while node not in seen:
        seen[node] = len(path)
        path.append(node)
        node = min(parents[node])
    cycle = path[seen[node]:] + [node]
    return cycle[::-1]


# ══════════════════════════════════════════════════════════════════════════════
# Writing derived files
# ══════════════════════════════════════════════════════════════════════════════

def write_if_changed(path: Path, text: str) -> bool:
    """Write text to path only if it differs. Returns True if written."""
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return True


def report(path: Path, changed: bool) -> None:
    status = "updated  " if changed else "unchanged"
    print(f"  {status} {path.relative_to(BASE_DIR).as_posix()}")


def sync_grade_views(subject: str, graph: dict, prune: bool) -> None:
    """Rebuild graph_by_grade/ from the master; list (or with prune, delete) stale files."""
    grade_dir = KG_DIR / subject / "graph_by_grade"
    concepts = graph["concepts"]
    grades = sorted({g for c in concepts.values() for g in c["grades"]})

    written: set[Path] = set()
    for grade in grades:
        view_concepts = {s: c for s, c in concepts.items() if grade in c["grades"]}
        view = {
            "grade": grade,
            "subject": subject,
            "total_concepts": len(view_concepts),
            "concepts": view_concepts,
        }
        path = grade_dir / f"grade{grade}_{subject}.json"
        report(path, write_if_changed(path, json.dumps(view, indent=2, ensure_ascii=False)))
        written.add(path)

    stale_files = [f for f in sorted(grade_dir.glob("*.json")) if f not in written]
    for stale in stale_files:
        rel = stale.relative_to(BASE_DIR).as_posix()
        if prune:
            stale.unlink()
            print(f"  removed   {rel} (not derived from master)")
        else:
            print(f"  STALE     {rel} (not derived from master — rerun with --prune to delete)")


def sync_stream_views(subject: str, graph: dict, prune: bool) -> None:
    """Rebuild graph_by_subject/ for a graph whose concepts carry a `subject` tag.

    Science is one master graph across seven grades, but from grade 11 the books split
    into physics, chemistry and biology, and a learner browsing chemistry should not be
    shown mechanics. Each concept's tag is hand-assigned (scripts/tag_science_subjects.py);
    this only slices by it. Edges are kept when both ends are in the slice, so each view
    is a valid graph on its own rather than a bag of concepts with dangling references.
    """
    streams = sorted({c["subject"] for c in graph["concepts"].values() if c.get("subject")})
    out_dir = KG_DIR / subject / "graph_by_subject"
    if not streams:
        return

    written: set[Path] = set()
    for stream in streams:
        view_concepts = {s: c for s, c in graph["concepts"].items()
                         if c.get("subject") == stream}
        view_edges = [e for e in graph["edges"]
                      if e["from"] in view_concepts and e["to"] in view_concepts]
        view = {
            "subject": stream,
            "parent": subject,
            "total_concepts": len(view_concepts),
            "total_edges": len(view_edges),
            "concepts": view_concepts,
            "edges": view_edges,
        }
        path = out_dir / f"{stream}.json"
        report(path, write_if_changed(path, json.dumps(view, indent=2, ensure_ascii=False)))
        written.add(path)

    for stale in [f for f in sorted(out_dir.glob("*.json")) if f not in written]:
        rel = stale.relative_to(BASE_DIR).as_posix()
        if prune:
            stale.unlink()
            print(f"  removed   {rel} (not derived from master)")
        else:
            print(f"  STALE     {rel} (not derived from master — rerun with --prune to delete)")


def sync_subject(subject: str, check_only: bool, prune: bool) -> bool:
    path = master_path(subject)
    print(f"\n{SUBJECTS[subject]} — {path.relative_to(BASE_DIR).as_posix()}")
    if not path.exists():
        print("  ERROR: master file not found")
        return False

    master_text = path.read_text(encoding="utf-8")
    graph = json.loads(master_text)

    errors = validate(graph)
    if errors:
        print(f"  INVALID — {len(errors)} problem(s):")
        for e in errors[:MAX_ERRORS_SHOWN]:
            print(f"    - {e}")
        if len(errors) > MAX_ERRORS_SHOWN:
            print(f"    … and {len(errors) - MAX_ERRORS_SHOWN} more")
        print("  Nothing written for this subject.")
        return False
    print(f"  valid: {graph['total_concepts']} concepts, {graph['total_edges']} edges, no cycles")
    late = late_prerequisites(graph)
    if late:
        print(f"  note: {len(late)} prerequisite(s) are taught later than the concept "
              f"that lists them (kept; the frontend hides these per grade)")
        for line in late[:MAX_ERRORS_SHOWN]:
            print(f"        {line}")

    if check_only:
        return True

    sync_grade_views(subject, graph, prune)
    sync_stream_views(subject, graph, prune)

    visual = KG_DIR / subject / f"{subject}_visual.html"
    report(visual, write_if_changed(visual, build_html(graph, SUBJECTS[subject])))

    for frontend in FRONTEND_DIRS:
        target = frontend / f"{subject}.json"
        report(target, write_if_changed(target, master_text))

    return True


def main() -> None:
    p = argparse.ArgumentParser(description="Validate master knowledge graphs and sync all copies")
    p.add_argument("--subject", choices=list(SUBJECTS), help="Only this subject")
    p.add_argument("--check", action="store_true", help="Validate only; write nothing")
    p.add_argument("--prune", action="store_true",
                   help="Delete files in graph_by_grade/ that are not derived from the master")
    args = p.parse_args()

    subjects = [args.subject] if args.subject else list(SUBJECTS)
    ok = all([sync_subject(s, args.check, args.prune) for s in subjects])
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
