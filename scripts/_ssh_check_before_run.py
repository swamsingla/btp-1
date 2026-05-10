"""
Read graph_builder.py args, then launch with nohup and monitor.
"""
import paramiko, time, sys

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

# Read argparse section of graph_builder.py to know CLI args
print("=== graph_builder.py argparse / main section ===")
o, _ = run(inner, f"grep -n 'argparse\\|add_argument\\|def main\\|subject\\|grade\\|--' {BASE_PATH}/scripts/graph_builder.py | head -60")
print(o)

# Check if a graph build process is already running
print("\n=== Any graph_builder process already running? ===")
o, _ = run(inner, "ps aux | grep graph_builder | grep -v grep")
print(o if o.strip() else "None running.")

# Check Python path
print("\n=== Python executable ===")
o, _ = run(inner, "which python3; python3 --version")
print(o)

# Check GPU
print("\n=== GPU ===")
o, _ = run(inner, "nvidia-smi --query-gpu=name,memory.total,memory.free --format=csv,noheader 2>/dev/null || echo 'no nvidia-smi'")
print(o)

# Check existing checkpoints
print("\n=== Existing checkpoints ===")
o, _ = run(inner, f"ls -lh {BASE_PATH}/data/knowledge_graph/.checkpoints/")
print(o)

# Check tail of stage2 log
print("\n=== Last 30 lines of stage2_maths.log ===")
o, _ = run(inner, f"tail -30 {BASE_PATH}/logs/stage2_maths.log 2>/dev/null || echo 'no log'")
print(o)

inner.close(); jump.close()
print("\nDone.")
