"""
Patch llm_local.py on remote: increase timeout cap from 180s to 600s
"""
import paramiko, time

JUMP_HOST = "ada.iiit.ac.in"; JUMP_USER = "shubhamcvit"; PASSWORD = "0410@Shubham"
INNER_HOST = "gnode048"; BASE = "/ssd_scratch/btp-1"

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

def connect():
    jump = paramiko.SSHClient()
    jump.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    jump.connect(JUMP_HOST, username=JUMP_USER, password=PASSWORD,
                 look_for_keys=False, allow_agent=False, timeout=20)
    ch = jump.get_transport().open_channel("direct-tcpip", (INNER_HOST, 22), ("127.0.0.1", 0))
    inner = paramiko.SSHClient()
    inner.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    inner.connect(INNER_HOST, username=JUMP_USER, password=PASSWORD,
                  sock=ch, look_for_keys=False, allow_agent=False, timeout=20)
    return jump, inner

jump, inner = connect()
print("Connected")

patch = r"""
path = '/ssd_scratch/btp-1/scripts/llm_local.py'
with open(path) as f:
    src = f.read()

old = 'timeout_secs = min(max(max_new_tokens // 10, 60), 180)'
new = 'timeout_secs = min(max(max_new_tokens // 5, 120), 600)'

if old in src:
    src = src.replace(old, new, 1)
    with open(path, 'w') as f:
        f.write(src)
    print('PATCHED: timeout cap raised to 600s')
else:
    print('Pattern not found - checking current line:')
    for i, line in enumerate(src.splitlines(), 1):
        if 'timeout_secs' in line:
            print(f'  line {i}: {line}')
"""

cmd = "python3 << 'PYEOF'\n" + patch + "\nPYEOF"
o, e = run(inner, cmd, timeout=15)
print(o, e)

# Verify
o, e = run(inner, "grep -n 'timeout_secs' " + BASE + "/scripts/llm_local.py")
print("Verification:", o)

inner.close(); jump.close()
