import json
g = json.load(open('data/output/knowledge_graph/maths_v2.json', encoding='utf-8'))

print('=== GRADE 12 concepts and prereqs ===')
for slug, c in g['concepts'].items():
    if 12 in c['grades']:
        names = [g['concepts'][p]['canonical_name'] for p in c['prerequisites']]
        print(f"  {c['canonical_name']}")
        for n in names:
            print(f"    <- {n}")

print()
print('=== Most connected (leads_to) ===')
ranked = sorted(g['concepts'].items(), key=lambda x: len(x[1]['leads_to']), reverse=True)
for slug, c in ranked[:12]:
    print(f"  {c['canonical_name']:<50}  leads_to={len(c['leads_to'])}  prereqs={len(c['prerequisites'])}")

print()
print('=== DAG check (cycle detection) ===')
# Simple DFS cycle detection
visited = set()
rec_stack = set()
def has_cycle(node, adj):
    visited.add(node)
    rec_stack.add(node)
    for nb in adj.get(node, []):
        if nb not in visited:
            if has_cycle(nb, adj):
                return True
        elif nb in rec_stack:
            print(f'  CYCLE: {node} -> {nb}')
            return True
    rec_stack.discard(node)
    return False

adj = {slug: c['leads_to'] for slug, c in g['concepts'].items()}
cycle_found = False
for n in adj:
    if n not in visited:
        if has_cycle(n, adj):
            cycle_found = True
if not cycle_found:
    print('  No cycles detected - valid DAG')
