"""
Full reset script:
1. Download all maths topic files (grade 6-12) from remote → local
2. Upload fixed graph_builder.py + _instant_check.py
3. Kill old graph_builder
4. Restart graph_builder (will resume from edge-checkpoints if any exist)
5. Print live log tail to confirm it's running
"""
import paramiko, os, time, pathlib, json

JUMP_HOST = "ada.iiit.ac.in"; USER = "shubhamcvit"; PW = "0410@Shubham"
INNER_HOST = "gnode048"; BASE = "/ssd_scratch/btp-1"
LOCAL_ROOT = pathlib.Path(__file__).parent.parent  # btp-1 root
SCRIPTS = LOCAL_ROOT / "scripts"
LOCAL_TOPICS = LOCAL_ROOT / "data" / "intermediate" / "raw_topics"
LOCAL_TOPICS.mkdir(parents=True, exist_ok=True)

def run(c, cmd, t=20):
    s = c.get_transport().open_session(); s.exec_command(cmd)
    o = b""
    dl = time.time() + t
    while time.time() < dl:
        if s.recv_ready(): o += s.recv(65536)
        if s.exit_status_ready():
            while s.recv_ready(): o += s.recv(65536)
            break
        time.sleep(0.05)
    return o.decode(errors="replace").strip()

print("Connecting...")
jump = paramiko.SSHClient(); jump.set_missing_host_key_policy(paramiko.AutoAddPolicy())
jump.connect(JUMP_HOST, username=USER, password=PW, look_for_keys=False, allow_agent=False, timeout=15)
ch = jump.get_transport().open_channel("direct-tcpip", (INNER_HOST, 22), ("127.0.0.1", 0))
inner = paramiko.SSHClient(); inner.set_missing_host_key_policy(paramiko.AutoAddPolicy())
inner.connect(INNER_HOST, username=USER, password=PW, sock=ch, look_for_keys=False, allow_agent=False, timeout=15)
sftp = inner.open_sftp()
print("Connected.")

# ─── 1. Download all grade maths topic files ─────────────────────────────────
print("\n=== DOWNLOADING TOPIC FILES ===")
for grade in range(6, 13):
    remote_path = f"{BASE}/data/intermediate/raw_topics/grade{grade}_maths.json"
    local_path = LOCAL_TOPICS / f"grade{grade}_maths.json"
    try:
        sftp.stat(remote_path)  # check exists
        sftp.get(remote_path, str(local_path))
        data = json.loads(local_path.read_text(encoding="utf-8"))
        topic_count = len(data.get("topics", []))
        print(f"  grade{grade}: {topic_count} topics → {local_path.relative_to(LOCAL_ROOT)}")
    except FileNotFoundError:
        print(f"  grade{grade}: NOT FOUND on remote (skipped)")
    except Exception as e:
        print(f"  grade{grade}: ERROR — {e}")

# ─── 2. Upload fixed scripts ──────────────────────────────────────────────────
print("\n=== UPLOADING FIXED SCRIPTS ===")
for fname in ["graph_builder.py", "_instant_check.py", "_pipeline_tick.py"]:
    local_f = SCRIPTS / fname
    if local_f.exists():
        sftp.put(str(local_f), f"{BASE}/scripts/{fname}")
        print(f"  Uploaded: {fname}")
    else:
        print(f"  SKIP (not found locally): {fname}")

# Verify both fixes are on remote
fix1 = run(inner, f"grep -n 'str(grade)' {BASE}/scripts/graph_builder.py | head -5")
print(f"\nFix verification (str(grade) occurrences):\n{fix1}")

# ─── 3. Kill any stale graph_builder ────────────────────────────────────────
print("\n=== KILLING OLD PROCESS ===")
run(inner, "pkill -9 -f 'graph_builder' 2>/dev/null; sleep 2")
procs = run(inner, "pgrep -a -f graph_builder 2>/dev/null || echo none")
print(f"  After kill: {procs}")

# ─── 4. Restart graph_builder ────────────────────────────────────────────────
print("\n=== RESTARTING GRAPH BUILDER ===")
logfile = f"{BASE}/logs/stage2_maths_v4.log"
cmd = (
    f"cd {BASE} && "
    f"export LLAMA_MODEL_PATH=/ssd_scratch/models/llama-8b && "
    f"nohup python3 scripts/graph_builder.py --subject maths --no-skip-existing "
    f"> {logfile} 2>&1 & echo $!"
)
pid = run(inner, cmd, t=10)
print(f"  graph_builder started, PID: {pid}")
print(f"  Log: {logfile}")

# ─── 5. Wait 15s and tail log to confirm no crash ───────────────────────────
print("\n=== WAITING 15s TO CONFIRM STARTUP ===")
time.sleep(15)
tail = run(inner, f"tail -20 {logfile}", t=15)
print(tail)

# Also confirm process still alive
alive = run(inner, "pgrep -a -f graph_builder 2>/dev/null || echo DEAD")
print(f"\nProcess status: {alive}")

# Checkpoint counts
ckpt_concepts = run(inner, f"ls {BASE}/data/knowledge_graph/.checkpoints/maths_concepts_batch*.json 2>/dev/null | wc -l")
ckpt_edges = run(inner, f"ls {BASE}/data/knowledge_graph/.checkpoints/maths_edges_grade*.json 2>/dev/null | wc -l")
print(f"Concept checkpoints: {ckpt_concepts.strip()}  |  Edge checkpoints: {ckpt_edges.strip()}")

sftp.close(); inner.close(); jump.close()
print("\nDone. Start the monitor loop now.")
