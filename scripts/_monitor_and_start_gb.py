"""
Monitor topic ingestion (PID 10531). After it finishes:
  1. Check each grade 6-12 has > 0 topics
  2. For any grade with MISSING or 0 topics, re-run topic_ingestion for that grade
     (uploads latest topic_ingestion.py first each time)
  3. Repeat until ALL grades 6,7,8,9,10,11,12 have topics
  4. Only then start graph_builder --subject maths --no-skip-existing

Polls every 3 min while waiting.
"""
import paramiko, time, os, sys

JUMP_HOST = "ada.iiit.ac.in"; USER = "shubhamcvit"; PW = "0410@Shubham"
INNER_HOST = "gnode048"; BASE = "/ssd_scratch/btp-1"
SCRIPTS = os.path.dirname(os.path.abspath(__file__))
INGESTION_PID = 10531
POLL_SEC = 180
REQUIRED_GRADES = [6, 7, 8, 9, 10, 11, 12]
# Grades where LLM must carry (0 NCERT headings) — needs patience
LLM_ONLY_GRADES = [7, 12]

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

def upload(inner, local, remote):
    sftp = inner.open_sftp(); sftp.put(local, remote); sftp.close()
    print(f"  Uploaded {os.path.basename(local)} → {remote}")

def is_pid_running(inner, pid):
    return bool(run(inner, f"ps -p {pid} -o pid= 2>/dev/null").strip())

def any_ingestion_running(inner):
    out = run(inner, "pgrep -f 'topic_ingestion' | head -5").strip()
    return out  # returns PIDs if running

def get_grade_topic_count(inner, grade):
    f = f"{BASE}/data/intermediate/raw_topics/grade{grade}_maths.json"
    out = run(inner, f"[ -f {f} ] && python3 -c \"import json; d=json.load(open('{f}')); print(len(d.get('topics',[])))\" 2>/dev/null || echo MISSING").strip()
    try:
        return int(out)
    except ValueError:
        return -1  # MISSING

def check_all_grades(inner):
    """Returns dict grade->count, -1 means file missing."""
    status = {}
    for g in REQUIRED_GRADES:
        status[g] = get_grade_topic_count(inner, g)
    return status

def print_status(status):
    for g, n in status.items():
        mark = "✓" if n > 0 else ("MISSING" if n < 0 else "EMPTY (0)")
        print(f"    grade{g}: {n if n >= 0 else '---'} topics  {mark}")

def rerun_grade(inner, grade, log_suffix):
    """Re-run topic ingestion for a single grade, blocking until done."""
    log_file = f"{BASE}/logs/stage1_maths_grade{grade}_rerun{log_suffix}.log"
    cmd = (
        f"cd {BASE} && "
        "export LLAMA_MODEL_PATH=/ssd_scratch/models/llama-8b && "
        f"nohup python3 scripts/topic_ingestion.py --subject maths --grade {grade} --no-skip-existing "
        f"> {log_file} 2>&1 & echo $!"
    )
    pid = run(inner, cmd, t=10).strip()
    print(f"  Started grade {grade} re-run, PID={pid}, log={log_file}")
    return pid, log_file

def start_graph_builder(inner):
    log_file = f"{BASE}/logs/stage2_maths_v3.log"
    cmd = (
        f"cd {BASE} && "
        "export LLAMA_MODEL_PATH=/ssd_scratch/models/llama-8b && "
        f"nohup python3 scripts/graph_builder.py --subject maths --no-skip-existing "
        f"> {log_file} 2>&1 & echo $!"
    )
    pid = run(inner, cmd, t=10).strip()
    return pid, log_file

# ─── Main loop ────────────────────────────────────────────────────────────────
jump, inner = connect()
poll = 0
rerun_attempt = 0

print(f"Monitoring topic_ingestion PID={INGESTION_PID} + auto-handling missing grades")
print(f"Required grades: {REQUIRED_GRADES}\n")

while True:
    poll += 1
    now = time.strftime("%H:%M:%S")
    print(f"[{now}] Poll #{poll}")

    # Check if original ingestion process is still running
    if is_pid_running(inner, INGESTION_PID):
        log_tail = run(inner, f"tail -6 {BASE}/logs/stage1_maths_v2.log 2>/dev/null").strip()
        print(f"  PID {INGESTION_PID} RUNNING | log tail:")
        for ln in log_tail.splitlines():
            print(f"    {ln}")
        print(f"  Sleeping {POLL_SEC}s...\n")
        inner.close(); jump.close()
        time.sleep(POLL_SEC)
        jump, inner = connect()
        continue

    # --- Original process done (or never was running) ---
    # Check if any re-run ingestion is still running
    active_pids = any_ingestion_running(inner)
    if active_pids:
        log_tail = run(inner, f"tail -6 {BASE}/logs/stage1_maths_v2.log 2>/dev/null || tail -6 $(ls -t {BASE}/logs/stage1_maths_grade*.log 2>/dev/null | head -1) 2>/dev/null").strip()
        print(f"  Re-run ingestion still running (PIDs: {active_pids.strip()}) | log tail:")
        for ln in log_tail.splitlines():
            print(f"    {ln}")
        print(f"  Sleeping {POLL_SEC}s...\n")
        inner.close(); jump.close()
        time.sleep(POLL_SEC)
        jump, inner = connect()
        continue

    # --- No ingestion running — check grade status ---
    print(f"\n  No ingestion running. Checking grade files...")
    status = check_all_grades(inner)
    print_status(status)

    bad_grades = [g for g, n in status.items() if n <= 0]

    if not bad_grades:
        print("\n  ALL grades have topics! Proceeding to graph builder...\n")
        break

    print(f"\n  Grades still bad: {bad_grades}")
    rerun_attempt += 1

    if rerun_attempt > 3:
        print("  Too many re-run attempts. Moving to graph builder with available data.")
        break

    # Upload latest topic_ingestion.py before re-running
    upload(inner, os.path.join(SCRIPTS, "topic_ingestion.py"), BASE + "/scripts/topic_ingestion.py")

    # Re-run each bad grade sequentially (start first one; poll loop will wait for it)
    g = bad_grades[0]
    print(f"  Re-running grade {g} (attempt {rerun_attempt})...")

    # Delete the empty file first so --no-skip-existing isn't even needed
    run(inner, f"rm -f {BASE}/data/intermediate/raw_topics/grade{g}_maths.json")

    _, log_file = rerun_grade(inner, g, rerun_attempt)
    time.sleep(5)
    log_start = run(inner, f"tail -3 {log_file} 2>/dev/null").strip()
    print(f"  Log start: {log_start}")

    print(f"  Sleeping {POLL_SEC}s...\n")
    inner.close(); jump.close()
    time.sleep(POLL_SEC)
    jump, inner = connect()

# ─── Start graph builder ───────────────────────────────────────────────────────
print("Starting graph_builder (stage 2)...")
upload(inner, os.path.join(SCRIPTS, "graph_builder.py"), BASE + "/scripts/graph_builder.py")

gb_pid, gb_log = start_graph_builder(inner)
print(f"graph_builder PID: {gb_pid} | log: {gb_log}")

time.sleep(10)
gb_check = run(inner, "ps aux | grep graph_builder | grep -v grep | awk '{print $2,$3,$11,$12}'").strip()
print(f"Running: {gb_check}")
log_start = run(inner, f"tail -8 {gb_log} 2>/dev/null").strip()
print(f"Stage 2 log start:\n{log_start}")

inner.close(); jump.close()
print("\nDone. Use _chk.py to monitor graph building.")

