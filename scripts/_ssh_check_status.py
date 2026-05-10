"""
Check if graph_builder is running, read logs, report status
"""
import paramiko, json, time

JUMP_HOST = "ada.iiit.ac.in"; JUMP_USER = "shubhamcvit"; PASSWORD = "0410@Shubham"
INNER_HOST = "gnode048"; BASE_PATH = "/ssd_scratch/btp-1"

def run(client, cmd, timeout=30):
    s = client.get_transport().open_session()
    s.exec_command(cmd)
    out, err = b"", b""
    dl = time.time() + timeout
    while time.time() < dl:
        if s.recv_ready(): out += s.recv(65536)
        if s.recv_stderr_ready(): err += s.recv_stderr(65536)
        if s.exit_status_ready():
            while s.recv_ready(): out += s.recv(65536)
            while s.recv_stderr_ready(): err += s.recv_stderr(65536)
            break
        time.sleep(0.1)
    return out.decode(errors="replace"), err.decode(errors="replace")

def make_client(hostname, username, password, sock=None):
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    kw = dict(hostname=hostname, username=username, password=password,
              look_for_keys=False, allow_agent=False, timeout=20)
    if sock: kw["sock"] = sock
    c.connect(**kw)
    return c

jump = make_client(JUMP_HOST, JUMP_USER, PASSWORD)
ch = jump.get_transport().open_channel("direct-tcpip", (INNER_HOST, 22), ("127.0.0.1", 0))
inner = make_client(INNER_HOST, JUMP_USER, PASSWORD, sock=ch)
print("Connected to gnode048\n")

# 1. Check running processes
print("="*60)
print("RUNNING PYTHON PROCESSES")
print("="*60)
o, e = run(inner, "ps aux | grep python | grep -v grep")
print(o if o.strip() else "No python processes running")

# 2. GPU status
print("\n" + "="*60)
print("GPU STATUS")
print("="*60)
o, e = run(inner, "nvidia-smi --query-gpu=name,memory.total,memory.free,memory.used --format=csv,noheader 2>/dev/null")
print(o if o.strip() else "No GPU info")

# 3. Full stage2 log
print("\n" + "="*60)
print("STAGE 2 MATHS LOG (last 80 lines)")
print("="*60)
o, e = run(inner, f"tail -80 {BASE_PATH}/logs/stage2_maths.log 2>/dev/null || echo 'log not found'")
print(o)

# 4. Stage2 general log
print("\n" + "="*60)
print("STAGE 2 GENERAL LOG (last 30 lines)")
print("="*60)
o, e = run(inner, f"tail -30 {BASE_PATH}/logs/stage2.log 2>/dev/null || echo 'log not found'")
print(o)

# 5. Check checkpoints to see progress
print("\n" + "="*60)
print("CHECKPOINT STATUS")
print("="*60)
o, e = run(inner, f"ls -lah {BASE_PATH}/data/knowledge_graph/.checkpoints/")
print(o)

# 6. Check current graph state
print("\n" + "="*60)
print("CURRENT GRADE6_MATHS GRAPH STATE")
print("="*60)
o, e = run(inner, f"""python3 -c "
import json
g = json.load(open('{BASE_PATH}/data/knowledge_graph/graph_by_grade/grade6_maths.json'))
concepts = g.get('concepts', {{}})
edges = g.get('edges', [])
print(f'Concepts: {{len(concepts)}}')
print(f'Edges: {{len(edges)}}')
edge_types = {{}}
for e in edges:
    t = e.get('type','unknown')
    edge_types[t] = edge_types.get(t, 0) + 1
print(f'Edge types: {{edge_types}}')
" 2>&1""")
print(o, e)

# 7. Read full graph_builder.py
print("\n" + "="*60)
print("graph_builder.py (FULL)")
print("="*60)
o, e = run(inner, f"cat {BASE_PATH}/scripts/graph_builder.py", timeout=15)
print(o)

# 8. llm_local.py
print("\n" + "="*60)
print("llm_local.py (FULL)")
print("="*60)
o, e = run(inner, f"cat {BASE_PATH}/scripts/llm_local.py", timeout=15)
print(o)

inner.close(); jump.close()
print("\nDone.")
