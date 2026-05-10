import json
g = json.load(open('data/output/knowledge_graph/maths_v2.json', encoding='utf-8'))
print('total_concepts:', g['total_concepts'])
print('total_edges:', g['total_edges'])
print('version:', g.get('version','?'))
print()
for grade, v in g['grade_views'].items():
    ep = len(v.get('entry_points', []))
    print(f"  Grade {grade}: {v['count']} concepts, {ep} entry points")
