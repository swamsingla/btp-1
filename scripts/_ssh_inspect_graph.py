"""
Read and display the current state of grade6 maths knowledge graph
"""
import paramiko
import json
import time

JUMP_HOST = "ada.iiit.ac.in"
JUMP_USER = "shubhamcvit"
PASSWORD  = "0410@Shubham"
INNER_HOST = "gnode048"
BASE_PATH  = "/ssd_scratch/btp-1"

def run(client, cmd, timeout=30):
    session = client.get_transport().open_session()
    session.exec_command(cmd)
    stdout, stderr = b"", b""
    deadline = time.time() + timeout
    while time.time() < deadline:
        if session.recv_ready():
            stdout += session.recv(65536)
        if session.recv_stderr_ready():
            stderr += session.recv_stderr(65536)
        if session.exit_status_ready():
            while session.recv_ready(): stdout += session.recv(65536)
            while session.recv_stderr_ready(): stderr += session.recv_stderr(65536)
            break
        time.sleep(0.1)
    return stdout.decode(errors="replace"), stderr.decode(errors="replace")

def make_client(hostname, username, password, sock=None):
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    kwargs = dict(hostname=hostname, username=username, password=password,
                  look_for_keys=False, allow_agent=False, timeout=20)
    if sock: kwargs["sock"] = sock
    c.connect(**kwargs)
    return c

jump = make_client(JUMP_HOST, JUMP_USER, PASSWORD)
ch = jump.get_transport().open_channel("direct-tcpip", (INNER_HOST, 22), ("127.0.0.1", 0))
inner = make_client(INNER_HOST, JUMP_USER, PASSWORD, sock=ch)
print("Connected to gnode048\n")

# 1. Read raw_topics for grade6 maths
print("="*60)
print("STAGE 1 OUTPUT: raw_topics/grade6_maths.json")
print("="*60)
o, e = run(inner, f"cat {BASE_PATH}/data/intermediate/raw_topics/grade6_maths.json")
try:
    data = json.loads(o)
    print(f"Grade: {data.get('grade')}, Subject: {data.get('subject')}")
    topics = data.get('topics', [])
    print(f"Total topics: {len(topics)}")
    for t in topics[:10]:
        name = t.get('raw_name', t.get('name', str(t)))
        subs = t.get('subtopics', [])
        print(f"  - {name} ({len(subs)} subtopics)")
    if len(topics) > 10:
        print(f"  ... and {len(topics)-10} more")
except Exception as ex:
    print(f"Parse error: {ex}")
    print(o[:2000])

# 2. Read existing grade6 knowledge graph
print("\n" + "="*60)
print("STAGE 2 OUTPUT: knowledge_graph/graph_by_grade/grade6_maths.json")
print("="*60)
o, e = run(inner, f"cat {BASE_PATH}/data/knowledge_graph/graph_by_grade/grade6_maths.json")
try:
    g = json.loads(o)
    concepts = g.get('concepts', {})
    edges = g.get('edges', [])
    entry_pts = g.get('entry_points', [])
    print(f"Concepts: {len(concepts)}")
    print(f"Edges: {len(edges)}")
    print(f"Entry points: {entry_pts}")
    print("\nSample concepts (first 8):")
    for slug, data in list(concepts.items())[:8]:
        prereqs = data.get('prerequisites', [])
        grades = data.get('grades', [])
        print(f"  [{slug}]")
        print(f"    name: {data.get('canonical_name', slug)}")
        print(f"    grades: {grades}, prereqs: {prereqs}")
    print("\nSample edges (first 10):")
    for e in edges[:10]:
        print(f"  {e.get('from')} --[{e.get('type')}]--> {e.get('to')}")
except Exception as ex:
    print(f"Parse error: {ex}")
    print(o[:3000])

# 3. Check the stage 2 log
print("\n" + "="*60)
print("STAGE 2 LOG (last 40 lines)")
print("="*60)
o, e = run(inner, f"tail -40 {BASE_PATH}/logs/stage2_maths.log 2>/dev/null || tail -40 {BASE_PATH}/logs/stage2.log 2>/dev/null")
print(o)

# 4. Check graph_by_subject/maths.json size
print("\n" + "="*60)
print("GLOBAL MATHS GRAPH stats")
print("="*60)
o, e = run(inner, f"python3 -c \"import json; g=json.load(open('{BASE_PATH}/data/knowledge_graph/graph_by_subject/maths.json')); print('concepts:', len(g.get('concepts',{{}})), 'edges:', len(g.get('edges',[])))\" 2>&1")
print(o, e)

# 5. Check if graph_builder.py has any errors / what scripts exist
print("\n" + "="*60)
print("graph_builder.py - head 80 lines")
print("="*60)
o, e = run(inner, f"head -80 {BASE_PATH}/scripts/graph_builder.py")
print(o)

inner.close()
jump.close()
