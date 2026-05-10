#!/usr/bin/env python3
"""Quick check of graph quality on the server. Run on the compute node."""
import json
from pathlib import Path

KG_DIR = Path("/ssd_scratch/btp-1/data/knowledge_graph")
CKPT_DIR = KG_DIR / ".checkpoints"

# Check graph file
gf = KG_DIR / "graph_by_subject" / "maths.json"
if gf.exists():
    d = json.loads(gf.read_text())
    print(f"=== MATHS GRAPH ===")
    print(f"  Concepts: {d['total_concepts']}")
    print(f"  Edges: {d['total_edges']}")
    with_prereqs = sum(1 for c in d['concepts'].values() if c.get('prerequisites'))
    print(f"  With prerequisites: {with_prereqs}/{d['total_concepts']}")
    isolated = sum(1 for c in d['concepts'].values() if not c.get('prerequisites') and not c.get('leads_to'))
    print(f"  Isolated (no edges): {isolated}")
    # Sample
    for slug, c in list(d['concepts'].items())[:3]:
        print(f"\n  [{c.get('domain','?')} > {c.get('area','?')}] {c['canonical_name']}")
        print(f"    grades={c.get('grades',[])} prereqs={c.get('prerequisites',[])} leads_to={c.get('leads_to',[])}")
else:
    print(f"Graph file not found: {gf}")

# Check edge checkpoints
print(f"\n=== EDGE CHECKPOINTS ===")
for grade in range(6, 13):
    ckpt = CKPT_DIR / f"maths_edges_grade{grade}.json"
    if ckpt.exists():
        edges = json.loads(ckpt.read_text())
        total_prereqs = sum(len(e.get('prerequisites', [])) for e in edges)
        non_empty = sum(1 for e in edges if e.get('prerequisites'))
        print(f"  Grade {grade}: {len(edges)} records, {non_empty} with prereqs, {total_prereqs} total prereq links")
    else:
        print(f"  Grade {grade}: (no checkpoint)")
