"""Full rebuild with correct --model-path /ssd_scratch/models/llama-8b."""
import paramiko, time

JUMP_HOST  = "ada.iiit.ac.in"; JUMP_USER = "shubhamcvit"; PASSWORD = "0410@Shubham"
INNER_HOST = "gnode048";       BASE_PATH = "/ssd_scratch/btp-1"
MODEL_PATH = "/ssd_scratch/models/llama-8b"

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

LOG  = f"{BASE_PATH}/logs/stage2_maths_rebuild.log"
CKPT = f"{BASE_PATH}/data/knowledge_graph/.checkpoints"
KG   = f"{BASE_PATH}/data/knowledge_graph"

# No need to re-delete — already cleaned. Just launch with correct model path.
print("=== Launching full rebuild with correct model path ===")
cmd = (
    f"cd {BASE_PATH} && "
    f"nohup python3 scripts/graph_builder.py "
    f"--subject maths "
    f"--model-path {MODEL_PATH} "
    f"--no-skip-existing "
    f"> {LOG} 2>&1 & echo $!"
)
o, e = run(inner, cmd, timeout=10)
pid = o.strip()
print(f"Launched. PID: {pid}")
if e.strip(): print(f"stderr: {e}")

time.sleep(5)
o_alive, _ = run(inner, "pgrep -f graph_builder.py")
print(f"Alive: {o_alive.strip() if o_alive.strip() else 'NOT running'}")
o_log, _ = run(inner, f"tail -5 {LOG} 2>/dev/null")
print(f"Early log:\n{o_log}")

# Monitor 30 minutes
print(f"\n=== Monitoring for 30 min (nohup keeps it running regardless) ===\n")
prev_tail = ""
for i in range(360):
    time.sleep(5)
    o_log, _ = run(inner, f"tail -8 {LOG} 2>/dev/null")
    o_pid, _ = run(inner, "pgrep -f graph_builder.py")
    elapsed  = (i + 1) * 5
    mins, secs = divmod(elapsed, 60)
    status = "RUNNING ✓" if o_pid.strip() else "STOPPED"

    # Only print if log changed to reduce noise
    if o_log != prev_tail or not o_pid.strip() or elapsed % 60 == 0:
        print(f"[{mins:02d}:{secs:02d} | {status}]")
        print(o_log)
        print()
        prev_tail = o_log

    if not o_pid.strip():
        print("=== Process ended. Final 60 lines: ===")
        o_final, _ = run(inner, f"tail -60 {LOG}")
        print(o_final)

        print("\n=== Output summary: ===")
        o_stats, _ = run(inner, f"""python3 -c "
import json, pathlib
kg = pathlib.Path('{KG}')
for f in sorted(kg.glob('**/*.json')):
    if '.checkpoints' in str(f): continue
    try:
        d = json.loads(f.read_text())
        c = len(d.get('concepts', {{}}))
        e = len(d.get('edges', []))
        ep = len(d.get('entry_points', []))
        print(f'  {{str(f.relative_to(kg))}}: {{c}} concepts, {{e}} edges, {{ep}} entry_points')
    except: pass
" 2>&1""")
        print(o_stats)
        break

inner.close(); jump.close()
print(f"\nLog: gnode048:{LOG}")
