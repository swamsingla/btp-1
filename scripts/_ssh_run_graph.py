"""
All-in-one: check args, clean bad checkpoints, launch graph_builder with nohup, monitor.
"""
import paramiko, time, sys

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

# ── 1. Get exact CLI args ────────────────────────────────────────────────────
print("=== Step 1: Get graph_builder.py CLI args ===")
o, _ = run(inner, f"cd {BASE_PATH} && python3 scripts/graph_builder.py --help 2>&1")
print(o)

# ── 2. Kill any stale process ────────────────────────────────────────────────
print("=== Step 2: Kill any stale graph_builder process ===")
o, _ = run(inner, "pkill -f graph_builder.py 2>/dev/null; echo 'done'")
print(o)

# ── 3. Delete empty/bad checkpoints (2-byte = empty list '[]') ──────────────
print("=== Step 3: Delete empty/corrupted checkpoints ===")
CKPT = f"{BASE_PATH}/data/knowledge_graph/.checkpoints"
o, _ = run(inner, f"""
python3 -c "
import os, json, pathlib
ckpt = pathlib.Path('{CKPT}')
removed = []
for f in ckpt.glob('*.json'):
    try:
        data = json.loads(f.read_text())
        if isinstance(data, list) and len(data) == 0:
            f.unlink()
            removed.append(f.name)
        elif isinstance(data, list) and len(data) < 2 and 'edge' in f.name:
            f.unlink()
            removed.append(f.name)
    except:
        f.unlink()
        removed.append(f.name + ' (corrupt)')
print('Removed:', removed if removed else 'none')
"
""")
print(o)

# ── 4. Remaining checkpoints ─────────────────────────────────────────────────
print("=== Step 4: Remaining checkpoints (will be skipped/reused) ===")
o, _ = run(inner, f"ls -lh {CKPT}/")
print(o)

# ── 5. Launch with nohup ─────────────────────────────────────────────────────
print("=== Step 5: Launching graph_builder.py with nohup ===")
LOG = f"{BASE_PATH}/logs/stage2_maths_run2.log"
# Try --subjects first (common pattern), fallback handled by --help output
LAUNCH_CMD = f"cd {BASE_PATH} && nohup python3 scripts/graph_builder.py --subjects maths > {LOG} 2>&1 &"
o, e = run(inner, LAUNCH_CMD)
print("Launch stdout:", o)
print("Launch stderr:", e)

time.sleep(3)

# Get PID
o, _ = run(inner, "pgrep -f graph_builder.py")
pid = o.strip()
print(f"PID: {pid if pid else 'NOT FOUND - checking log for errors'}")

if not pid:
    # Maybe the arg is different - try without --subjects
    print("\n--- Trying without --subjects flag ---")
    o, _ = run(inner, f"tail -5 {LOG} 2>/dev/null")
    print("Log tail:", o)
    # Try alternate invocation
    LAUNCH_CMD2 = f"cd {BASE_PATH} && nohup python3 scripts/graph_builder.py maths > {LOG} 2>&1 &"
    run(inner, LAUNCH_CMD2)
    time.sleep(3)
    o, _ = run(inner, "pgrep -f graph_builder.py")
    pid = o.strip()
    print(f"PID (attempt 2): {pid}")

# ── 6. Monitor for 4 minutes ─────────────────────────────────────────────────
print(f"\n=== Step 6: Monitoring {LOG} for 4 minutes ===")
print("(Ctrl+C to stop monitoring — process will keep running on server)\n")

last_pos = 0
for i in range(48):  # 48 × 5s = 4 minutes
    time.sleep(5)
    # Read new log lines
    o, _ = run(inner, f"tail -15 {LOG} 2>/dev/null")
    # Check process still alive
    o2, _ = run(inner, f"pgrep -f graph_builder.py")
    alive = "RUNNING" if o2.strip() else "STOPPED"
    print(f"[{(i+1)*5:3d}s | {alive}] --- log tail ---")
    print(o)
    if not o2.strip():
        print("\nProcess finished (or crashed). Final log:")
        o3, _ = run(inner, f"tail -30 {LOG}")
        print(o3)
        break

inner.close(); jump.close()
print("\n=== Done monitoring ===")
