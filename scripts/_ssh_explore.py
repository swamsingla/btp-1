"""
SSH into ada.iiit.ac.in -> gnode048, inspect /ssd_scratch/btp-1
"""
import paramiko
import sys
import time

JUMP_HOST = "ada.iiit.ac.in"
JUMP_USER = "shubhamcvit"
PASSWORD  = "0410@Shubham"
INNER_HOST = "gnode048"
BASE_PATH  = "/ssd_scratch/btp-1"

def run(chan, cmd, timeout=30):
    chan.exec_command(cmd)
    stdout, stderr = b"", b""
    deadline = time.time() + timeout
    while time.time() < deadline:
        if chan.recv_ready():
            stdout += chan.recv(65536)
        if chan.recv_stderr_ready():
            stderr += chan.recv_stderr(65536)
        if chan.exit_status_ready():
            while chan.recv_ready():
                stdout += chan.recv(65536)
            while chan.recv_stderr_ready():
                stderr += chan.recv_stderr(65536)
            break
        time.sleep(0.1)
    return stdout.decode(errors="replace"), stderr.decode(errors="replace"), chan.recv_exit_status()

def make_client(hostname, username, password, sock=None):
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    kwargs = dict(hostname=hostname, username=username, password=password,
                  look_for_keys=False, allow_agent=False, timeout=20)
    if sock:
        kwargs["sock"] = sock
    c.connect(**kwargs)
    return c

print("=== Connecting to jump host ===")
jump = make_client(JUMP_HOST, JUMP_USER, PASSWORD)
print("Connected to ada.iiit.ac.in")

print("=== Opening tunnel to gnode048 ===")
transport = jump.get_transport()
dest_addr  = (INNER_HOST, 22)
src_addr   = ("127.0.0.1", 0)
channel    = transport.open_channel("direct-tcpip", dest_addr, src_addr)

inner = make_client(INNER_HOST, JUMP_USER, PASSWORD, sock=channel)
print("Connected to gnode048")

print("\n=== Directory structure ===")
o, e, _ = run(inner.get_transport().open_session(), f"find {BASE_PATH} -maxdepth 4 | sort")
print(o if o else f"ERROR: {e}")

print("\n=== Stage 1 output for grade6/maths ===")
o, e, _ = run(inner.get_transport().open_session(),
              f"ls -la {BASE_PATH}/data/intermediate/raw_topics/ 2>/dev/null || echo 'raw_topics dir not found'")
print(o, e)

print("\n=== Check for any JSON files related to grade6 ===")
o, e, _ = run(inner.get_transport().open_session(),
              f"find {BASE_PATH} -name '*grade6*' -o -name '*grade_6*' 2>/dev/null | sort")
print(o if o else "No grade6 files found")

print("\n=== Check Python/conda environments available ===")
o, e, _ = run(inner.get_transport().open_session(),
              "which python3; python3 --version; conda info --envs 2>/dev/null || echo 'no conda'")
print(o, e)

print("\n=== Scripts present ===")
o, e, _ = run(inner.get_transport().open_session(),
              f"ls -la {BASE_PATH}/scripts/ 2>/dev/null || echo 'no scripts dir'")
print(o, e)

inner.close()
jump.close()
print("\n=== Done exploring ===")
