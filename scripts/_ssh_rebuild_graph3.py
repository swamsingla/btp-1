"""Launch graph_builder with LLAMA_MODEL_PATH env var (not --model-path flag)."""
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
KG   = f"{BASE_PATH}/data/knowledge_graph"

# Launch — env var set BEFORE python starts so llm_local.py picks it up at import
print("=== Launching (LLAMA_MODEL_PATH set in env) ===")
cmd = (
    f"cd {BASE_PATH} && "
    f"export LLAMA_MODEL_PATH={MODEL_PATH} && "
    f"nohup python3 scripts/graph_builder.py "
    f"--subject maths "
    f"--no-skip-existing "
    f"> {LOG} 2>&1 & echo $!"
)
o, e = run(inner, cmd, timeout=10)
pid = o.strip()
print(f"Launched. PID: {pid}")

# Give it 20s to start loading the model (takes ~13s)
time.sleep(20)
o_alive, _ = run(inner, "pgrep -f graph_builder.py")
o_log, _ = run(inner, f"tail -8 {LOG} 2>/dev/null")
status = "RUNNING ✓" if o_alive.strip() else "STOPPED ✗"
print(f"Status: {status}")
print(f"Log:\n{o_log}")

if not o_alive.strip():
    print("\nFailed to start. Full log:")
    o_full, _ = run(inner, f"cat {LOG}")
    print(o_full)
    inner.close(); jump.close()
    exit(1)

# Monitor 30 minutes
print(f"\n=== Monitoring for 30 min (nohup persists) ===\n")
prev_tail = ""
for i in range(360):
    time.sleep(5)
    o_log, _ = run(inner, f"tail -8 {LOG} 2>/dev/null")
    o_pid, _ = run(inner, "pgrep -f graph_builder.py")
    elapsed = (i + 1) * 5
    mins, secs = divmod(elapsed, 60)
    status = "RUNNING ✓" if o_pid.strip() else "STOPPED"

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
