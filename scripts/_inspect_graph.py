"""Inspect graph quality: check concepts, edges, and edge checkpoint contents."""
import paramiko, json, sys

HOST_JUMP = "ada.iiit.ac.in"
HOST_INNER = "gnode048"
USER = "shubhamcvit"
PASS = "0410@Shubham"
BASE = "/ssd_scratch/btp-1"

j = paramiko.SSHClient()
j.set_missing_host_key_policy(paramiko.AutoAddPolicy())
j.connect(HOST_JUMP, username=USER, password=PASS)
t = j.get_transport().open_channel("direct-tcpip", (HOST_INNER, 22), ("localhost", 0))
inner = paramiko.SSHClient()
inner.set_missing_host_key_policy(paramiko.AutoAddPolicy())
inner.connect(HOST_INNER, username=USER, password=PASS, sock=t)

def run(cmd, t=20):
    _, o, e = inner.exec_command(cmd, timeout=t)
    return o.read().decode()

# 1. Check edge checkpoints
print("=== EDGE CHECKPOINTS ===")
for grade in [6, 7, 8, 9, 10, 11, 12]:
    raw = run(f"cat {BASE}/data/knowledge_graph/.checkpoints/maths_edges_grade{grade}.json 2>/dev/null")
    if raw.strip():
        try:
            data = json.loads(raw)
            print(f"  grade{grade}: {len(data)} records")
            if data:
                print(f"    sample: {json.dumps(data[0])}")
        except Exception as ex:
            print(f"  grade{grade}: PARSE ERROR - {ex}")
            print(f"    raw[:200]: {raw[:200]}")
    else:
        print(f"  grade{grade}: EMPTY FILE")

# 2. Check maths.json
print("\n=== MATHS.JSON SUMMARY ===")
raw2 = run(f"cat {BASE}/data/knowledge_graph/graph_by_subject/maths.json 2>/dev/null", t=30)
if raw2.strip():
    try:
        d = json.loads(raw2)
        print(f"  Keys: {list(d.keys())}")
        concepts = d.get("concepts", {})
        print(f"  Total concepts: {len(concepts)}")
        edges = d.get("edges", [])
        print(f"  Total edges: {len(edges)}")
        grade_views = d.get("grade_views", {})
        print(f"  Grade views: {list(grade_views.keys())}")
        for g, v in grade_views.items():
            print(f"    grade {g}: {v.get('count',0)} concepts, {len(v.get('entry_points',[]))} entry points")
        # Sample a concept
        if concepts:
            slug, c = next(iter(concepts.items()))
            print(f"\n  Sample concept [{slug}]:")
            print(f"    {json.dumps(c, indent=4)[:500]}")
    except Exception as ex:
        print(f"  PARSE ERROR: {ex}")
        print(f"  raw[:300]: {raw2[:300]}")
else:
    print("  FILE NOT FOUND OR EMPTY")

# 3. Check the v4 log for any edge-related lines
print("\n=== EDGE LOG LINES (v4 log) ===")
log = run(f"grep -i 'edge\\|prerequisite\\|records' {BASE}/logs/stage2_maths_v4.log 2>/dev/null | tail -40")
print(log)

inner.close()
j.close()
