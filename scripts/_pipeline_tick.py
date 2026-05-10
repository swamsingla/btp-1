"""
State machine: grade7 → grade12 → graph_builder.
NO sleeps inside — PowerShell loop handles timing.
Run once per poll cycle. Exits with:
  0 = still in progress (rerun next cycle)
  1 = error
  2 = graph_builder launched (done)
"""
import paramiko, time, os, sys, json

JUMP_HOST = "ada.iiit.ac.in"; USER = "shubhamcvit"; PW = "0410@Shubham"
INNER_HOST = "gnode048"; BASE = "/ssd_scratch/btp-1"
SCRIPTS = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(SCRIPTS, "_pipeline_state.json")

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

def upload_file(inner, local, remote):
    sftp = inner.open_sftp(); sftp.put(local, remote); sftp.close()

def ingestion_running(inner):
    return run(inner, "ps aux | grep 'python3.*topic_ingestion' | grep -v grep | awk '{print $2}'").strip()

def graph_builder_running(inner):
    return run(inner, "ps aux | grep 'python3.*graph_builder' | grep -v grep | awk '{print $2}'").strip()

def get_count(inner, grade):
    f = f"{BASE}/data/intermediate/raw_topics/grade{grade}_maths.json"
    out = run(inner, f"[ -f {f} ] && python3 -c \"import json; d=json.load(open('{f}')); print(len(d.get('topics',[])))\" 2>/dev/null || echo -1").strip()
    try: return int(out)
    except: return -1

def load_state():
    if os.path.exists(STATE_FILE):
        try:
            return json.loads(open(STATE_FILE, encoding="utf-8-sig").read().strip())
        except Exception:
            pass
    return {"phase": "grade7"}  # start with grade7

def save_state(s):
    json.dump(s, open(STATE_FILE, "w"))

# ── main ──────────────────────────────────────────────────────────────────────
state = load_state()
phase = state["phase"]
print(f"[{time.strftime('%H:%M:%S')}] Phase: {phase}")

jump, inner = connect()

if phase == "grade7":
    c7 = get_count(inner, 7)
    ing = ingestion_running(inner)
    log_tail = run(inner, f"tail -3 {BASE}/logs/stage1_maths_grade7_v2.log 2>/dev/null").strip()
    print(f"  grade7 topics={c7}  ingestion_pids={ing or 'none'}")
    print(f"  Log: {log_tail.splitlines()[-1] if log_tail else '(no log)'}")
    if c7 > 0:
        print("  grade7 DONE -> launching grade8")
        log8 = f"{BASE}/logs/stage1_maths_grade8_v2.log"
        run(inner, f"rm -f {BASE}/data/intermediate/raw_topics/grade8_maths.json")
        cmd = (f"cd {BASE} && export LLAMA_MODEL_PATH=/ssd_scratch/models/llama-8b && "
               f"nohup python3 scripts/topic_ingestion.py --subject maths --grade 8 --no-skip-existing "
               f"> {log8} 2>&1 & echo $!")
        pid = run(inner, cmd, t=10).strip()
        print(f"  grade8 PID: {pid}")
        save_state({"phase": "grade8"})
    elif not ing:
        print("  ERROR: ingestion not running and grade7 has 0 topics -- check log")
        print(run(inner, f"tail -15 {BASE}/logs/stage1_maths_grade7_v2.log 2>/dev/null"))
        inner.close(); jump.close(); sys.exit(1)
    else:
        print("  Still running...")

elif phase == "grade8":
    c8 = get_count(inner, 8)
    ing = ingestion_running(inner)
    log_tail = run(inner, f"tail -3 {BASE}/logs/stage1_maths_grade8_v2.log 2>/dev/null").strip()
    print(f"  grade8 topics={c8}  ingestion_pids={ing or 'none'}")
    print(f"  Log: {log_tail.splitlines()[-1] if log_tail else '(no log)'}")
    if c8 > 0:
        print("  grade8 DONE -> launching grade12")
        log12 = f"{BASE}/logs/stage1_maths_grade12_v2.log"
        run(inner, f"rm -f {BASE}/data/intermediate/raw_topics/grade12_maths.json")
        cmd = (f"cd {BASE} && export LLAMA_MODEL_PATH=/ssd_scratch/models/llama-8b && "
               f"nohup python3 scripts/topic_ingestion.py --subject maths --grade 12 --no-skip-existing "
               f"> {log12} 2>&1 & echo $!")
        pid = run(inner, cmd, t=10).strip()
        print(f"  grade12 PID: {pid}")
        save_state({"phase": "grade12"})
    elif not ing:
        print("  ERROR: grade8 not running and 0 topics -- check log")
        print(run(inner, f"tail -15 {BASE}/logs/stage1_maths_grade8_v2.log 2>/dev/null"))
        inner.close(); jump.close(); sys.exit(1)
    else:
        print("  Still running...")

elif phase == "grade12":
    c12 = get_count(inner, 12)
    ing = ingestion_running(inner)
    log_tail = run(inner, f"tail -3 {BASE}/logs/stage1_maths_grade12_v2.log 2>/dev/null").strip()
    print(f"  grade12 topics={c12}  ingestion_pids={ing or 'none'}")
    print(f"  Log: {log_tail.splitlines()[-1] if log_tail else '(no log)'}")
    if c12 > 0:
        print("  grade12 DONE -> launching graph_builder")
        # Clear ckpts and start graph_builder
        run(inner, f"rm -f {BASE}/data/intermediate/concept_ckpt_*.jsonl {BASE}/data/intermediate/edge_ckpt_*.jsonl")
        upload_file(inner, os.path.join(SCRIPTS, "graph_builder.py"), BASE + "/scripts/graph_builder.py")
        gb_log = f"{BASE}/logs/stage2_maths_v3.log"
        cmd = (f"cd {BASE} && export LLAMA_MODEL_PATH=/ssd_scratch/models/llama-8b && "
               f"nohup python3 scripts/graph_builder.py --subject maths --no-skip-existing "
               f"> {gb_log} 2>&1 & echo $!")
        gb_pid = run(inner, cmd, t=10).strip()
        print(f"  graph_builder PID: {gb_pid}")
        save_state({"phase": "graph_builder"})
    elif not ing:
        print("  ERROR: ingestion not running and grade12 has 0 topics -- check log")
        print(run(inner, f"tail -15 {BASE}/logs/stage1_maths_grade12_v2.log 2>/dev/null"))
        # Retry
        log12 = f"{BASE}/logs/stage1_maths_grade12_retry.log"
        run(inner, f"rm -f {BASE}/data/intermediate/raw_topics/grade12_maths.json")
        cmd = (f"cd {BASE} && export LLAMA_MODEL_PATH=/ssd_scratch/models/llama-8b && "
               f"nohup python3 scripts/topic_ingestion.py --subject maths --grade 12 --no-skip-existing "
               f"> {log12} 2>&1 & echo $!")
        pid = run(inner, cmd, t=10).strip()
        print(f"  Retrying grade12 PID: {pid}")
    else:
        print("  Still running...")

elif phase == "graph_builder":
    gb = graph_builder_running(inner)
    ckpts = run(inner, f"ls {BASE}/data/knowledge_graph/.checkpoints/maths_concepts_batch*.json 2>/dev/null | wc -l").strip()
    edge_ckpts = run(inner, f"ls {BASE}/data/knowledge_graph/.checkpoints/maths_edges_grade*.json 2>/dev/null | wc -l").strip()
    # Try v5 log first, fall back to v4, then v3
    log_tail = run(inner, f"tail -8 {BASE}/logs/stage2_maths_v5.log 2>/dev/null").strip()
    if not log_tail:
        log_tail = run(inner, f"tail -8 {BASE}/logs/stage2_maths_v4.log 2>/dev/null").strip()
    if not log_tail:
        log_tail = run(inner, f"tail -8 {BASE}/logs/stage2_maths_v3.log 2>/dev/null").strip()
    output = run(inner, f"[ -f {BASE}/data/knowledge_graph/graph_by_subject/maths.json ] && echo EXISTS || echo NOT_YET").strip()
    print(f"  graph_builder PIDs={gb or 'none'}  concept_ckpts={ckpts}  edge_ckpts={edge_ckpts}  output={output}")
    print(f"  Log:\n    " + log_tail.replace("\n", "\n    "))
    if output == "EXISTS":
        print("  GRAPH BUILDER DONE ✓")
        save_state({"phase": "done"})
        inner.close(); jump.close(); sys.exit(2)

elif phase == "done":
    print("  Pipeline complete!")
    inner.close(); jump.close(); sys.exit(2)

inner.close(); jump.close()
sys.exit(0)
