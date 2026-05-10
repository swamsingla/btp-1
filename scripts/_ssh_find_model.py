"""Find the LLaMA model, then relaunch with correct --model-path."""
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

jump  = make_client(JUMP_HOST, JUMP_USER, PASSWORD)
ch    = jump.get_transport().open_channel("direct-tcpip", (INNER_HOST, 22), ("127.0.0.1", 0))
inner = make_client(INNER_HOST, JUMP_USER, PASSWORD, sock=ch)
print("Connected\n")

# Find model
print("=== Finding LLaMA model ===")
o, _ = run(inner, "find /ssd_scratch /home2/shubhamcvit /scratch -maxdepth 6 -name 'config.json' 2>/dev/null | grep -i llama | head -20")
print(o if o.strip() else "No config.json found, trying broader search...")

o2, _ = run(inner, "find /ssd_scratch /home2/shubhamcvit -maxdepth 5 -name '*.safetensors' 2>/dev/null | head -10")
print(o2)

o3, _ = run(inner, "find /ssd_scratch -maxdepth 4 -type d -name '*llama*' -o -type d -name '*models*' 2>/dev/null | head -20")
print(o3)

# Check the old log to see what path worked before
print("\n=== Old log model path ===")
o4, _ = run(inner, f"grep -i 'llama\\|model.*path\\|loading.*from' {BASE_PATH}/logs/stage2_maths.log | head -10")
print(o4)

inner.close(); jump.close()
