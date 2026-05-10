"""Instant SSH status check — no sleeps. Prints process state, log tail, grade counts."""
import paramiko, time, os, sys

JUMP_HOST = "ada.iiit.ac.in"; USER = "shubhamcvit"; PW = "0410@Shubham"
INNER_HOST = "gnode048"; BASE = "/ssd_scratch/btp-1"

def run(c, cmd, t=25):
    s = c.get_transport().open_session(); s.exec_command(cmd)
    o = b""
    dl = time.time() + t
    while time.time() < dl:
        if s.recv_ready(): o += s.recv(65536)
        if s.exit_status_ready():
            while s.recv_ready(): o += s.recv(65536)
            break
        time.sleep(0.05)
    return o.decode(errors="replace")

def connect():
    jump = paramiko.SSHClient(); jump.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    jump.connect(JUMP_HOST, username=USER, password=PW, look_for_keys=False, allow_agent=False, timeout=15)
    ch = jump.get_transport().open_channel("direct-tcpip", (INNER_HOST, 22), ("127.0.0.1", 0))
    inner = paramiko.SSHClient(); inner.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    inner.connect(INNER_HOST, username=USER, password=PW, sock=ch, look_for_keys=False, allow_agent=False, timeout=15)
    return jump, inner

jump, inner = connect()
now = time.strftime("%H:%M:%S")

# Processes
procs = run(inner, "ps aux | grep -E 'topic_ingestion|graph_builder' | grep -v grep | awk '{print $2,$3,$11,$12,$13}'").strip()

# Grade file counts
counts = {}
for g in [6,7,8,9,10,11,12]:
    f = f"{BASE}/data/intermediate/raw_topics/grade{g}_maths.json"
    out = run(inner, f"[ -f {f} ] && python3 -c \"import json; d=json.load(open('{f}')); print(len(d.get('topics',[])))\" 2>/dev/null || echo -1").strip()
    try: counts[g] = int(out)
    except: counts[g] = -1

# Active log — try v5 first, fall back to v4, then v3
log_out = run(inner,
    f"echo '=== stage2 (last 20 lines) ===' && "
    f"( tail -20 {BASE}/logs/stage2_maths_v5.log 2>/dev/null || "
    f"tail -20 {BASE}/logs/stage2_maths_v4.log 2>/dev/null || "
    f"tail -20 {BASE}/logs/stage2_maths_v3.log 2>/dev/null )", t=25
)

# Graph builder ckpts
ckpts = run(inner, f"ls {BASE}/data/knowledge_graph/.checkpoints/maths_concepts_batch*.json 2>/dev/null | wc -l").strip()
edge_ckpts = run(inner, f"ls {BASE}/data/knowledge_graph/.checkpoints/maths_edges_grade*.json 2>/dev/null | wc -l").strip()
gb_out = run(inner, f"[ -f {BASE}/data/knowledge_graph/graph_by_subject/maths.json ] && echo EXISTS || echo NOT_YET").strip()

inner.close(); jump.close()

print(f"\n{'='*60}")
print(f"[{now}] STATUS CHECK")
print(f"{'='*60}")
print(f"PROCESSES:\n  {procs or '(none)'}")
print(f"\nGRADE TOPIC FILES:")
for g, n in counts.items():
    mark = "✓" if n > 0 else ("MISSING" if n < 0 else "EMPTY")
    print(f"  grade{g}: {n if n >= 0 else '---'}  [{mark}]")
print(f"\nGRAPH BUILDER: concept_ckpts={ckpts}  edge_ckpts={edge_ckpts}  output={gb_out}")
print(f"\nLOG TAILS:")
print(log_out.strip())
