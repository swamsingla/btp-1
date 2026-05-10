"""
Monitor the running graph_builder process - tail the rebuild log
"""
import paramiko, time

JUMP_HOST = "ada.iiit.ac.in"; JUMP_USER = "shubhamcvit"; PASSWORD = "0410@Shubham"
INNER_HOST = "gnode048"; BASE_PATH = "/ssd_scratch/btp-1"

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

jump = make_client(JUMP_HOST, JUMP_USER, PASSWORD)
ch = jump.get_transport().open_channel("direct-tcpip", (INNER_HOST, 22), ("127.0.0.1", 0))
inner = make_client(INNER_HOST, JUMP_USER, PASSWORD, sock=ch)
print("Connected to gnode048\n")

# Check if process still running
print("="*60)
print("PROCESS STATUS")
print("="*60)
o, e = run(inner, "ps aux | grep graph_builder | grep -v grep")
if o.strip():
    print("RUNNING:")
    print(o)
else:
    print("NOT RUNNING - process has finished or crashed")

# GPU usage
print("\n" + "="*60)
print("GPU MEMORY")
print("="*60)
o, e = run(inner, "nvidia-smi --query-gpu=index,name,memory.used,memory.free --format=csv,noheader")
print(o)

# Full rebuild log
print("\n" + "="*60)
print("REBUILD LOG (full / last 100 lines)")
print("="*60)
o, e = run(inner, f"tail -100 {BASE_PATH}/logs/stage2_maths_rebuild.log 2>/dev/null || echo 'rebuild log not found'")
print(o)

# Checkpoint status
print("\n" + "="*60)
print("CHECKPOINTS")
print("="*60)
o, e = run(inner, f"ls -lah {BASE_PATH}/data/knowledge_graph/.checkpoints/ 2>/dev/null")
print(o)

# Check output files
print("\n" + "="*60)
print("OUTPUT FILES")
print("="*60)
o, e = run(inner, f"ls -lah {BASE_PATH}/data/knowledge_graph/graph_by_grade/ 2>/dev/null && ls -lah {BASE_PATH}/data/knowledge_graph/graph_by_subject/ 2>/dev/null")
print(o)

inner.close(); jump.close()
print("\nDone.")
