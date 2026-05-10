"""Check logs, edge checkpoints, and graph output quality on gnode048."""
import paramiko, json, glob

HOST_JUMP = "ada.iiit.ac.in"
HOST_INNER = "gnode048"
USER = "shubhamcvit"
PASS = "0410@Shubham"
BASE = "/ssd_scratch/btp-1"

j = paramiko.SSHClient(); j.set_missing_host_key_policy(paramiko.AutoAddPolicy())
j.connect(HOST_JUMP, username=USER, password=PASS)
t = j.get_transport().open_channel("direct-tcpip", (HOST_INNER, 22), ("localhost", 0))
inner = paramiko.SSHClient(); inner.set_missing_host_key_policy(paramiko.AutoAddPolicy())
inner.connect(HOST_INNER, username=USER, password=PASS, sock=t)

def run(cmd, timeout=30):
    _, o, _ = inner.exec_command(cmd, timeout=timeout)
    return o.read().decode(errors="replace").strip()

# 1. Processes
print("=== PROCESSES ===")
print(run("pgrep -a -f graph_builder 2>/dev/null || echo none"))

# 2. Log files available
print("\n=== LOG FILES (recent) ===")
print(run(f"ls -lt {BASE}/logs/ | head -8"))

# 3. Full v5 log tail
print("\n=== stage2_maths_v5.log (last 60 lines) ===")
print(run(f"tail -60 {BASE}/logs/stage2_maths_v5.log 2>/dev/null || echo '(no v5 log)'"))

# 4. Edge checkpoint summary
print("\n=== EDGE CHECKPOINTS ===")
ckpt_script = """
import json, glob, sys
files = sorted(glob.glob('/ssd_scratch/btp-1/data/knowledge_graph/.checkpoints/maths_edges_grade*.json'))
if not files:
    print('  No edge checkpoints found')
    sys.exit(0)
total_prereqs = 0
for f in files:
    d = json.load(open(f))
    n_prereqs = sum(len(e.get('prerequisites',[])) for e in d)
    total_prereqs += n_prereqs
    sample = next((e for e in d if e.get('prerequisites')), None)
    sample_str = str(sample['prerequisites'][:2]) if sample else 'NONE'
    print(f'  {f.split(\"/\")[-1]}: {len(d)} records, {n_prereqs} prereq links, sample={sample_str}')
print(f'  TOTAL PREREQ LINKS: {total_prereqs}')
"""
print(run(f"python3 -c \"{ckpt_script}\" 2>&1"))

# 5. maths.json if it exists
print("\n=== maths.json OUTPUT ===")
check_script = """
import json, sys
try:
    d = json.load(open('/ssd_scratch/btp-1/data/knowledge_graph/graph_by_subject/maths.json'))
    print(f'concepts={d[\"total_concepts\"]}  edges={d[\"total_edges\"]}')
    views = d.get('grade_views', {})
    for g in sorted(views, key=lambda x: int(x)):
        v = views[g]
        n_with_prereqs = sum(1 for s in v['concepts'] if d['concepts'].get(s,{}).get('prerequisites'))
        print(f'  grade {g}: {v[\"count\"]} concepts, {n_with_prereqs} with prereqs, {len(v[\"entry_points\"])} entry points')
    samples = [(s,c) for s,c in d['concepts'].items() if c.get('prerequisites')]
    print(f'  Total concepts with prerequisites: {len(samples)}')
    for s,c in samples[:3]:
        print(f'    {c[\"canonical_name\"]} -> {c[\"prerequisites\"]}')
except FileNotFoundError:
    print('NOT_YET (maths.json does not exist)')
except Exception as e:
    print(f'ERROR: {e}')
"""
print(run(f"python3 -c \"{check_script}\" 2>&1"))

inner.close(); j.close()
