"""
Continuous monitor for graph_builder on gnode048.
Polls every 3 minutes until process finishes.
"""
import paramiko, time, sys, datetime

JUMP_HOST = "ada.iiit.ac.in"; JUMP_USER = "shubhamcvit"; PASSWORD = "0410@Shubham"
INNER_HOST = "gnode048"; BASE_PATH = "/ssd_scratch/btp-1"
LOG_FILE = f"{BASE_PATH}/logs/stage2_maths_v2.log"
POLL_SECS = 180  # 3 minutes

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

def connect():
    jump = make_client(JUMP_HOST, JUMP_USER, PASSWORD)
    ch = jump.get_transport().open_channel("direct-tcpip", (INNER_HOST, 22), ("127.0.0.1", 0))
    inner = make_client(INNER_HOST, JUMP_USER, PASSWORD, sock=ch)
    return jump, inner

def ts():
    return datetime.datetime.now().strftime("%H:%M:%S")

def check(inner):
    # Is process alive?
    o, _ = run(inner, "ps aux | grep graph_builder | grep -v grep | awk '{print $1,$2,$3,$11,$12}'")
    alive = bool(o.strip())

    # Last 30 lines of log
    log_o, _ = run(inner, f"tail -30 {LOG_FILE} 2>/dev/null", timeout=15)

    # Checkpoint count
    ckpt_o, _ = run(inner, f"ls {BASE_PATH}/data/knowledge_graph/.checkpoints/maths_concepts_batch*.json 2>/dev/null | wc -l")
    edge_ckpt_o, _ = run(inner, f"ls {BASE_PATH}/data/knowledge_graph/.checkpoints/maths_edges_grade*.json 2>/dev/null | wc -l")

    # Output files done?
    out_o, _ = run(inner, f"ls -lah {BASE_PATH}/data/knowledge_graph/graph_by_subject/maths.json 2>/dev/null || echo 'NOT YET'")

    print(f"\n{'='*65}")
    print(f"[{ts()}] POLL RESULT")
    print(f"{'='*65}")
    print(f"Process running: {'YES ✓' if alive else 'NO - finished or crashed'}")
    print(f"Concept checkpoints done: {ckpt_o.strip()}")
    print(f"Edge checkpoints done:    {edge_ckpt_o.strip()}")
    print(f"Subject output file:      {out_o.strip()}")
    print(f"\n--- Last 30 log lines ---")
    print(log_o.strip() if log_o.strip() else "(log empty)")
    sys.stdout.flush()

    # Detect completion
    completed = "✓ Subject graph saved" in log_o or "Global graph saved" in log_o
    errored = ("Traceback" in log_o or "Error" in log_o.split("Extracting prerequisite")[-1]) and not alive

    return alive, completed, errored

print(f"[{ts()}] Starting monitor — polling every {POLL_SECS}s. Ctrl+C to stop.")
sys.stdout.flush()

poll = 0
while True:
    poll += 1
    print(f"\n[{ts()}] Poll #{poll} — connecting …")
    sys.stdout.flush()
    try:
        jump, inner = connect()
        alive, completed, errored = check(inner)
        inner.close(); jump.close()
    except Exception as ex:
        print(f"[{ts()}] Connection error: {ex} — will retry")
        sys.stdout.flush()
        time.sleep(30)
        continue

    if completed:
        print(f"\n[{ts()}] ✅ GRAPH BUILD COMPLETE! Check output files above.")
        break
    elif errored:
        print(f"\n[{ts()}] ❌ Process CRASHED. Check log above for errors.")
        break
    elif not alive:
        # Double-check — maybe it just finished
        print(f"\n[{ts()}] Process not found in ps. Checking if output exists …")
        try:
            jump2, inner2 = connect()
            verify_cmd = "cat {p}/data/knowledge_graph/graph_by_subject/maths.json 2>/dev/null | python3 -c \"import sys,json; g=json.load(sys.stdin); print('concepts:', len(g.get('concepts',dict())), 'edges:', len(g.get('edges',[])))\"".format(p=BASE_PATH)
        o, _ = run(inner2, verify_cmd, timeout=20)
            print("Output:", o.strip() if o.strip() else "File does not exist yet")
            inner2.close(); jump2.close()
        except Exception as ex2:
            print(f"Check failed: {ex2}")
        break

    print(f"\n[{ts()}] Still running — sleeping {POLL_SECS}s …")
    sys.stdout.flush()
    time.sleep(POLL_SECS)
