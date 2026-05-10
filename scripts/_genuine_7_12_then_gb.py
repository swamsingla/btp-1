"""
1. Kill graph_builder PID 12026
2. Delete hardcoded injected files for grade 7 and 12
3. Upload fixed topic_ingestion.py (plain-string schema)
4. Run topic_ingestion for grade 7 then grade 12 (sequential)
5. Monitor until both done
6. Start graph_builder only after both have >0 topics
"""
import paramiko, time, os, sys

JUMP_HOST = "ada.iiit.ac.in"; USER = "shubhamcvit"; PW = "0410@Shubham"
INNER_HOST = "gnode048"; BASE = "/ssd_scratch/btp-1"
SCRIPTS = os.path.dirname(os.path.abspath(__file__))
GB_PID = 12026
POLL_SEC = 120

def run(c, cmd, t=45):
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

def upload_file(inner, local, remote):
    sftp = inner.open_sftp(); sftp.put(local, remote); sftp.close()
    print(f"  Uploaded {os.path.basename(local)} ✓")

def get_topic_count(inner, grade):
    f = f"{BASE}/data/intermediate/raw_topics/grade{grade}_maths.json"
    out = run(inner, f"[ -f {f} ] && python3 -c \"import json; d=json.load(open('{f}')); print(len(d.get('topics',[])))\" 2>/dev/null || echo MISSING").strip()
    try:
        return int(out)
    except ValueError:
        return -1

def any_ingestion_running(inner):
    # Check specifically for topic_ingestion python process (not just any pgrep)
    out = run(inner, "ps aux | grep 'python3.*topic_ingestion' | grep -v grep | awk '{print $2}'").strip()
    return out

def wait_for_ingestion(inner, jump, log_file, grade, poll_sec=120):
    """Poll until no topic_ingestion process running, return final topic count."""
    poll = 0
    while True:
        poll += 1
        pids = any_ingestion_running(inner)
        log_tail = run(inner, f"tail -4 {log_file} 2>/dev/null").strip()
        print(f"  [Poll {poll}] PIDs={pids or 'none'}")
        for ln in log_tail.splitlines():
            print(f"    {ln}")
        if not pids:
            count = get_topic_count(inner, grade)
            print(f"  → Ingestion done. grade{grade}: {count} topics")
            return count
        print(f"  Sleeping {poll_sec}s...\n")
        inner.close(); jump.close()
        time.sleep(poll_sec)
        jump, inner = connect()
    return inner, jump  # unreachable but keeps linter happy

jump, inner = connect()

# 1. Kill graph_builder
print(f"Killing graph_builder PID {GB_PID}...")
print(run(inner, f"kill {GB_PID} 2>/dev/null; pkill -f 'graph_builder' 2>/dev/null; pkill -f 'topic_ingestion' 2>/dev/null; echo done"))
time.sleep(2)

# 2. Delete hardcoded injected files for grades 7 and 12
print("Deleting injected grade 7 and 12 files...")
print(run(inner, f"rm -f {BASE}/data/intermediate/raw_topics/grade7_maths.json && echo deleted7"))
print(run(inner, f"rm -f {BASE}/data/intermediate/raw_topics/grade12_maths.json && echo deleted12"))

# 3. Upload fixed topic_ingestion.py
print("\nUploading fixed topic_ingestion.py (plain-string LLM schema)...")
upload_file(inner, os.path.join(SCRIPTS, "topic_ingestion.py"), BASE + "/scripts/topic_ingestion.py")

# Verify the key fix landed
print("Verify fix:")
print(run(inner, f"grep -n 'JSON array of strings\\|Return ONLY' {BASE}/scripts/topic_ingestion.py | head -5"))

# 4. Run grade 7 first
print("\n--- Running grade 7 ---")
log7 = f"{BASE}/logs/stage1_maths_grade7_genuine.log"
cmd7 = (f"cd {BASE} && export LLAMA_MODEL_PATH=/ssd_scratch/models/llama-8b && "
        f"nohup python3 scripts/topic_ingestion.py --subject maths --grade 7 --no-skip-existing "
        f"> {log7} 2>&1 & echo $!")
pid7 = run(inner, cmd7, t=10).strip()
print(f"PID: {pid7}")
time.sleep(8)
print(run(inner, f"tail -4 {log7} 2>/dev/null"))

count7 = wait_for_ingestion(inner, jump, log7, 7, POLL_SEC)

# Reconnect after wait
jump, inner = connect()

if count7 <= 0:
    print(f"\nERROR: grade 7 still has {count7} topics after genuine run!")
    print("Last log:")
    print(run(inner, f"tail -20 {log7} 2>/dev/null"))
    inner.close(); jump.close()
    sys.exit(1)

print(f"\ngrade 7 ✓ ({count7} topics). Moving to grade 12...\n")

# 5. Run grade 12
print("--- Running grade 12 ---")
log12 = f"{BASE}/logs/stage1_maths_grade12_genuine.log"
cmd12 = (f"cd {BASE} && export LLAMA_MODEL_PATH=/ssd_scratch/models/llama-8b && "
         f"nohup python3 scripts/topic_ingestion.py --subject maths --grade 12 --no-skip-existing "
         f"> {log12} 2>&1 & echo $!")
pid12 = run(inner, cmd12, t=10).strip()
print(f"PID: {pid12}")
time.sleep(8)
print(run(inner, f"tail -4 {log12} 2>/dev/null"))

count12 = wait_for_ingestion(inner, jump, log12, 12, POLL_SEC)
jump, inner = connect()

if count12 <= 0:
    print(f"\nERROR: grade 12 still has {count12} topics!")
    print("Last log:")
    print(run(inner, f"tail -20 {log12} 2>/dev/null"))
    inner.close(); jump.close()
    sys.exit(1)

print(f"\ngrade 12 ✓ ({count12} topics).\n")

# 6. Final status check
print("=== Final topic file status ===")
for g in [6, 7, 8, 9, 10, 11, 12]:
    n = get_topic_count(inner, g)
    print(f"  grade{g}: {n if n >= 0 else 'MISSING'} topics  {'✓' if n > 0 else 'PROBLEM'}")

# 7. Clear old concept checkpoints and start graph builder
print("\nClearing old checkpoints...")
print(run(inner, f"rm -f {BASE}/data/intermediate/concept_ckpt_*.jsonl {BASE}/data/intermediate/edge_ckpt_*.jsonl && echo done"))

print("Uploading graph_builder.py...")
upload_file(inner, os.path.join(SCRIPTS, "graph_builder.py"), BASE + "/scripts/graph_builder.py")

print("Starting graph_builder (Stage 2)...")
gb_log = f"{BASE}/logs/stage2_maths_v3.log"
gb_cmd = (f"cd {BASE} && export LLAMA_MODEL_PATH=/ssd_scratch/models/llama-8b && "
          f"nohup python3 scripts/graph_builder.py --subject maths --no-skip-existing "
          f"> {gb_log} 2>&1 & echo $!")
gb_pid = run(inner, gb_cmd, t=10).strip()
print(f"graph_builder PID: {gb_pid}")

time.sleep(10)
print(run(inner, f"tail -6 {gb_log} 2>/dev/null"))
print(run(inner, "ps aux | grep graph_builder | grep -v grep | awk '{print $2,$3,$11,$12}'").strip())

inner.close(); jump.close()
print("\nDone. Monitor with _chk.py")
