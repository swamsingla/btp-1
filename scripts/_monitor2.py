"""
Continuous monitor for graph_builder on gnode048.
Polls every 3 minutes until process finishes or crashes.
"""
import paramiko
import time
import sys
import datetime

JUMP_HOST = "ada.iiit.ac.in"
JUMP_USER = "shubhamcvit"
PASSWORD = "0410@Shubham"
INNER_HOST = "gnode048"
BASE = "/ssd_scratch/btp-1"
LOG = BASE + "/logs/stage2_maths_v2.log"
POLL = 180


def run(client, cmd, timeout=30):
    s = client.get_transport().open_session()
    s.exec_command(cmd)
    out = b""
    err = b""
    deadline = time.time() + timeout
    while time.time() < deadline:
        if s.recv_ready():
            out += s.recv(65536)
        if s.recv_stderr_ready():
            err += s.recv_stderr(65536)
        if s.exit_status_ready():
            while s.recv_ready():
                out += s.recv(65536)
            while s.recv_stderr_ready():
                err += s.recv_stderr(65536)
            break
        time.sleep(0.1)
    return out.decode(errors="replace"), err.decode(errors="replace")


def connect():
    jump = paramiko.SSHClient()
    jump.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    jump.connect(JUMP_HOST, username=JUMP_USER, password=PASSWORD,
                 look_for_keys=False, allow_agent=False, timeout=20)
    ch = jump.get_transport().open_channel(
        "direct-tcpip", (INNER_HOST, 22), ("127.0.0.1", 0))
    inner = paramiko.SSHClient()
    inner.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    inner.connect(INNER_HOST, username=JUMP_USER, password=PASSWORD,
                  sock=ch, look_for_keys=False, allow_agent=False, timeout=20)
    return jump, inner


def ts():
    return datetime.datetime.now().strftime("%H:%M:%S")


def poll_once(inner):
    proc, _ = run(inner, "ps aux | grep graph_builder | grep -v grep")
    alive = bool(proc.strip())

    log_tail, _ = run(inner, "tail -35 " + LOG + " 2>/dev/null", timeout=15)

    ckpt_concepts, _ = run(inner,
        "ls " + BASE + "/data/knowledge_graph/.checkpoints/maths_concepts_batch*.json 2>/dev/null | wc -l")
    ckpt_edges, _ = run(inner,
        "ls " + BASE + "/data/knowledge_graph/.checkpoints/maths_edges_grade*.json 2>/dev/null | wc -l")

    out_file, _ = run(inner,
        "ls -lh " + BASE + "/data/knowledge_graph/graph_by_subject/maths.json 2>/dev/null || echo NOT_YET")

    print("")
    print("=" * 65)
    print("[" + ts() + "] POLL RESULT")
    print("=" * 65)
    print("Process running  : " + ("YES" if alive else "NO - finished or crashed"))
    print("Concept ckpts    : " + ckpt_concepts.strip())
    print("Edge ckpts       : " + ckpt_edges.strip())
    print("Output file      : " + out_file.strip())
    print("")
    print("--- Last 35 log lines ---")
    print(log_tail.strip() if log_tail.strip() else "(empty)")
    sys.stdout.flush()

    done = ("Subject graph saved" in log_tail or "Global graph saved" in log_tail)
    crashed = (not alive) and ("Traceback" in log_tail or "Error" in log_tail)
    return alive, done, crashed


print("[" + ts() + "] Monitor started — polling every " + str(POLL) + "s. Ctrl+C to stop.")
sys.stdout.flush()

poll_num = 0
while True:
    poll_num += 1
    print("\n[" + ts() + "] Poll #" + str(poll_num) + " — connecting ...")
    sys.stdout.flush()

    try:
        jump, inner = connect()
        alive, done, crashed = poll_once(inner)
        inner.close()
        jump.close()
    except Exception as ex:
        print("[" + ts() + "] Connection error: " + str(ex) + " — will retry in 30s")
        sys.stdout.flush()
        time.sleep(30)
        continue

    if done:
        print("\n[" + ts() + "] GRAPH BUILD COMPLETE!")
        break
    if crashed:
        print("\n[" + ts() + "] PROCESS CRASHED — see log above.")
        break
    if not alive:
        print("\n[" + ts() + "] Process gone — checking output file ...")
        try:
            jump2, inner2 = connect()
            verify_cmd = (
                "python3 -c \""
                "import json; "
                "g=json.load(open('" + BASE + "/data/knowledge_graph/graph_by_subject/maths.json')); "
                "print('concepts:', len(g.get('concepts', {})), 'edges:', len(g.get('edges', [])))"
                "\" 2>/dev/null || echo FILE_MISSING"
            )
            o, _ = run(inner2, verify_cmd, timeout=20)
            print("Result: " + o.strip())
            inner2.close()
            jump2.close()
        except Exception as ex2:
            print("Verify failed: " + str(ex2))
        break

    print("\n[" + ts() + "] Still running — sleeping " + str(POLL) + "s ...")
    sys.stdout.flush()
    time.sleep(POLL)
