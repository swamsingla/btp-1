"""
Delete all maths concept checkpoints (they're corrupt/empty), force full rebuild.
Then launch with --no-skip-existing and monitor.
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

CKPT  = f"{BASE_PATH}/data/knowledge_graph/.checkpoints"
KG    = f"{BASE_PATH}/data/knowledge_graph"
LOG   = f"{BASE_PATH}/logs/stage2_maths_rebuild.log"

# ── Step 1: Remove ALL maths checkpoints and the existing maths graph ─────────
print("=== Step 1: Removing stale maths checkpoints and outputs ===")
o, _ = run(inner, f"""
rm -f {CKPT}/maths_*.json
rm -f {KG}/graph_by_subject/maths.json
rm -f {KG}/graph.json
rm -f {KG}/graph_by_grade/grade*_maths.json
echo "Removed. Remaining checkpoints:"
ls {CKPT}/
""")
print(o)

# ── Step 2: Launch with --no-skip-existing ────────────────────────────────────
print("=== Step 2: Launching full rebuild ===")
cmd = (
    f"cd {BASE_PATH} && "
    f"nohup python3 scripts/graph_builder.py --subject maths --no-skip-existing --validate "
    f"> {LOG} 2>&1 & echo $!"
)
o, e = run(inner, cmd, timeout=10)
pid = o.strip()
print(f"Launched. PID: {pid}")

time.sleep(5)

o, _ = run(inner, "pgrep -fa graph_builder")
print(f"Process alive: {o.strip() if o.strip() else '??? - checking log'}")
if not o.strip():
    o, _ = run(inner, f"head -10 {LOG}")
    print("Early log:", o)

# ── Step 3: Monitor for 30 minutes ───────────────────────────────────────────
print(f"\n=== Monitoring {LOG} (nohup keeps running even if this stops) ===\n")

for i in range(360):  # 360 × 5s = 30 minutes
    time.sleep(5)
    o_log, _ = run(inner, f"tail -10 {LOG} 2>/dev/null")
    o_pid, _ = run(inner, "pgrep -f graph_builder.py")
    elapsed  = (i + 1) * 5
    mins, secs = divmod(elapsed, 60)
    status = "RUNNING ✓" if o_pid.strip() else "STOPPED"
    print(f"[{mins:02d}:{secs:02d} | {status}]")
    print(o_log)
    print()

    if not o_pid.strip():
        print("=== Process finished. Final 50 lines: ===")
        o_final, _ = run(inner, f"tail -50 {LOG}")
        print(o_final)

        print("\n=== Output graph stats: ===")
        o_stats, _ = run(inner, f"""
python3 -c "
import json, pathlib, sys
kg = pathlib.Path('{KG}')
for f in sorted(kg.glob('**/*.json')):
    if '.checkpoints' in str(f): continue
    try:
        d = json.loads(f.read_text())
        c = len(d.get('concepts', {{}}))
        e = len(d.get('edges', []))
        print(f'  {{f.relative_to(kg)}}: {{c}} concepts, {{e}} edges')
    except: pass
" 2>&1
""")
        print(o_stats)
        break

inner.close(); jump.close()
print(f"\n=== Done. Log: gnode048:{LOG} ===")
