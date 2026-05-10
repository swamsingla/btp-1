"""
Check checkpoint contents, get main() args, then nohup launch.
"""
import paramiko, time, json, sys

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
print("Connected\n")

CKPT = f"{BASE_PATH}/data/knowledge_graph/.checkpoints"

# Check every checkpoint
for fname in ["maths_concepts_batch20.json", "maths_concepts_batch40.json",
              "maths_edges_grade6.json", "maths_edges_grade7.json",
              "maths_edges_grade8.json", "maths_edges_grade9.json",
              "science_concepts_batch0.json"]:
    o, _ = run(inner, f"cat {CKPT}/{fname}")
    print(f"--- {fname} ---")
    print(o[:400])
    print()

# Get main() and argparse section
print("="*60)
print("main() and argparse section of graph_builder.py")
print("="*60)
o, _ = run(inner, f"grep -n '' {BASE_PATH}/scripts/graph_builder.py | tail -120")
print(o)

inner.close(); jump.close()
print("\nDone.")
