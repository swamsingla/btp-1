"""Upload fixed graph_builder.py and restart on remote (resumes from checkpoints)."""
import paramiko, time, os

JUMP_HOST = "ada.iiit.ac.in"; USER = "shubhamcvit"; PW = "0410@Shubham"
INNER_HOST = "gnode048"; BASE = "/ssd_scratch/btp-1"
SCRIPTS = os.path.dirname(os.path.abspath(__file__))

def run(c, cmd, t=15):
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

jump = paramiko.SSHClient(); jump.set_missing_host_key_policy(paramiko.AutoAddPolicy())
jump.connect(JUMP_HOST, username=USER, password=PW, look_for_keys=False, allow_agent=False, timeout=15)
ch = jump.get_transport().open_channel("direct-tcpip", (INNER_HOST, 22), ("127.0.0.1", 0))
inner = paramiko.SSHClient(); inner.set_missing_host_key_policy(paramiko.AutoAddPolicy())
inner.connect(INNER_HOST, username=USER, password=PW, sock=ch, look_for_keys=False, allow_agent=False, timeout=15)

# Upload fixed graph_builder.py
sftp = inner.open_sftp()
sftp.put(os.path.join(SCRIPTS, "graph_builder.py"), BASE + "/scripts/graph_builder.py")
sftp.close()
print("Uploaded graph_builder.py")

# Verify fix is on remote
out = run(inner, f"grep -n 'str(grade)' {BASE}/scripts/graph_builder.py")
print("Fix verified:", out)

# Checkpoint count
ckpts = run(inner, f"ls {BASE}/data/knowledge_graph/.checkpoints/maths_concepts_batch*.json 2>/dev/null | wc -l")
print(f"Concept checkpoints available: {ckpts}")

# Kill any stray graph_builder
run(inner, "pkill -f 'graph_builder' 2>/dev/null; sleep 1")

# Restart — append to same log so history is preserved
cmd = (f"cd {BASE} && export LLAMA_MODEL_PATH=/ssd_scratch/models/llama-8b && "
       f"nohup python3 scripts/graph_builder.py --subject maths --no-skip-existing "
       f">> {BASE}/logs/stage2_maths_v3.log 2>&1 & echo $!")
pid = run(inner, cmd, t=10)
print(f"graph_builder restarted, PID: {pid}")

time.sleep(6)
print("Log tail:")
print(run(inner, f"tail -8 {BASE}/logs/stage2_maths_v3.log"))

inner.close(); jump.close()
print("Done.")
