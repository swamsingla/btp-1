"""Read graph_builder.py and llm_local.py to understand model path handling."""
import paramiko, time

JUMP_HOST  = "ada.iiit.ac.in"; JUMP_USER = "shubhamcvit"; PASSWORD = "0410@Shubham"
INNER_HOST = "gnode048"

def run(client, cmd, timeout=30):
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

jump  = make_client(JUMP_HOST, JUMP_USER, PASSWORD)
ch    = jump.get_transport().open_channel("direct-tcpip", (INNER_HOST, 22), ("127.0.0.1", 0))
inner = make_client(INNER_HOST, JUMP_USER, PASSWORD, sock=ch)

BASE = "/ssd_scratch/btp-1"

print("=== graph_builder.py: model-path related lines ===")
o, _ = run(inner, f"grep -n 'model.path\\|model_path\\|llm_local\\|set_model\\|LLAMA_MODEL\\|env\\|environ' {BASE}/scripts/graph_builder.py | head -30")
print(o)

print("\n=== llm_local.py: model path loading lines ===")
o, _ = run(inner, f"grep -n 'model.path\\|DEFAULT\\|home2\\|ssd_scratch\\|environ\\|getenv\\|LLAMA' {BASE}/scripts/llm_local.py | head -30")
print(o)

print("\n=== llm_local.py lines 55-75 ===")
o, _ = run(inner, f"sed -n '55,75p' {BASE}/scripts/llm_local.py")
print(o)

print("\n=== graph_builder.py: argparse and main() section ===")
o, _ = run(inner, f"grep -n 'add_argument\\|args\\.' {BASE}/scripts/graph_builder.py | head -30")
print(o)

inner.close(); jump.close()
