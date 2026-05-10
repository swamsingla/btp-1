"""
Launch graph_builder correctly: --subject maths with nohup, monitor.
"""
import paramiko, time

JUMP_HOST  = "ada.iiit.ac.in"; JUMP_USER = "shubhamcvit"; PASSWORD = "0410@Shubham"
INNER_HOST = "gnode048";       BASE_PATH = "/ssd_scratch/btp-1"

def run(client, cmd, timeout=60):
    s = client.get_transport().open_session()
    s.exec_command(cmd)
    out, err = b"", b""
    dl = time.time() + timeout
    while time.time() < dl:
        if s.recv_ready():        out += s.recv(65536)
        if s.recv_stderr_ready(): err += s.recv_stderr(65536)
        if s.exit_status_ready():
            while s.recv_ready():        out += s.recv(65536)
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

print("Connecting...")
jump  = make_client(JUMP_HOST, JUMP_USER, PASSWORD)
ch    = jump.get_transport().open_channel("direct-tcpip", (INNER_HOST, 22), ("127.0.0.1", 0))
inner = make_client(INNER_HOST, JUMP_USER, PASSWORD, sock=ch)
print("Connected to gnode048\n")

LOG = f"{BASE_PATH}/logs/stage2_maths_run2.log"

# Launch with correct flag
print("=== Launching: python3 graph_builder.py --subject maths ===")
cmd = (
    f"cd {BASE_PATH} && "
    f"nohup python3 scripts/graph_builder.py --subject maths --skip-existing "
    f"> {LOG} 2>&1 & echo $!"
)
o, e = run(inner, cmd, timeout=10)
pid = o.strip()
print(f"Launched. PID: {pid}")
if e.strip():
    print(f"stderr: {e}")

time.sleep(4)

# Confirm it's running
o, _ = run(inner, "pgrep -fa graph_builder")
print(f"Process check: {o.strip() if o.strip() else 'NOT running - check log'}")
if not o.strip():
    o, _ = run(inner, f"head -20 {LOG}")
    print("Log head:\n", o)

# Monitor for 8 minutes (process runs long due to LLM loading)
print(f"\n=== Monitoring {LOG} for 8 minutes ===")
print("(Job runs on server via nohup — safe even if this script stops)\n")

for i in range(96):  # 96 × 5s = 8 minutes
    time.sleep(5)
    o_log, _ = run(inner, f"tail -12 {LOG} 2>/dev/null")
    o_pid, _ = run(inner, "pgrep -f graph_builder.py")
    status = "RUNNING ✓" if o_pid.strip() else "STOPPED"
    elapsed = (i + 1) * 5
    mins, secs = divmod(elapsed, 60)
    print(f"[{mins:02d}:{secs:02d} | {status}]")
    print(o_log)
    print()
    if not o_pid.strip():
        print("=== Process ended. Final 40 lines of log: ===")
        o_final, _ = run(inner, f"tail -40 {LOG}")
        print(o_final)
        # Check output files
        print("=== Output files generated: ===")
        o_out, _ = run(inner, f"ls -lh {BASE_PATH}/data/knowledge_graph/graph_by_grade/ {BASE_PATH}/data/knowledge_graph/graph_by_subject/ 2>/dev/null")
        print(o_out)
        break

inner.close(); jump.close()
print("\n=== Monitoring complete ===")
print(f"Log is at: gnode048:{LOG}")
print("Process runs independently via nohup even if this script was closed.")
