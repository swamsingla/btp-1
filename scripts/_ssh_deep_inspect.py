"""
Deep inspect: read edge checkpoints, full grade6 graph, and graph_builder.py fully
"""
import paramiko, json, time

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

# 1. Edge checkpoint for grade6 maths
print("="*60)
print("EDGE CHECKPOINT: maths_edges_grade6.json")
print("="*60)
o, e = run(inner, f"cat {BASE_PATH}/data/knowledge_graph/.checkpoints/maths_edges_grade6.json")
try:
    d = json.loads(o)
    if isinstance(d, list):
        print(f"Type: list, length: {len(d)}")
        for item in d[:5]: print(f"  {item}")
    elif isinstance(d, dict):
        print(f"Type: dict, keys: {list(d.keys())[:10]}")
        print(json.dumps(d, indent=2)[:2000])
    else:
        print(f"Type: {type(d)}, value: {str(d)[:500]}")
except Exception as ex:
    print(f"Parse error: {ex}")
    print(o[:2000])

# 2. Full stage2 log
print("\n" + "="*60)
print("FULL STAGE 2 LOG")
print("="*60)
o, e = run(inner, f"cat {BASE_PATH}/logs/stage2_maths.log 2>/dev/null")
print(o[:5000])

# 3. Full graph_builder.py
print("\n" + "="*60)
print("FULL graph_builder.py")
print("="*60)
o, e = run(inner, f"cat {BASE_PATH}/scripts/graph_builder.py")
print(o)

# 4. llm_local.py
print("\n" + "="*60)
print("llm_local.py")
print("="*60)
o, e = run(inner, f"cat {BASE_PATH}/scripts/llm_local.py")
print(o)

# 5. Available GPU
print("\n" + "="*60)
print("GPU STATUS")
print("="*60)
o, e = run(inner, "nvidia-smi --query-gpu=name,memory.total,memory.free --format=csv,noheader 2>/dev/null")
print(o if o else "No nvidia-smi")

# 6. Python packages
print("\n" + "="*60)
print("RELEVANT PACKAGES")
print("="*60)
o, e = run(inner, "python3 -c \"import transformers,torch; print('torch:', torch.__version__, 'cuda:', torch.cuda.is_available(), 'transformers:', transformers.__version__)\" 2>&1")
print(o, e)

inner.close(); jump.close()
print("\nDone.")
