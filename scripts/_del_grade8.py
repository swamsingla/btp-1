"""Delete grade8_maths.json on remote so it regenerates."""
import paramiko, time

JUMP_HOST = "ada.iiit.ac.in"; USER = "shubhamcvit"; PW = "0410@Shubham"
INNER_HOST = "gnode048"; BASE = "/ssd_scratch/btp-1"

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

print("Delete grade8:", run(inner, f"rm -f {BASE}/data/intermediate/raw_topics/grade8_maths.json && echo DELETED"))
print("File gone?  :", run(inner, f"ls {BASE}/data/intermediate/raw_topics/grade8_maths.json 2>/dev/null || echo CONFIRMED_GONE"))
print("Grade8 NCERT files:", run(inner, f"find {BASE}/data/intermediate/headings/grade8 -name 'chapter*.json' | wc -l"))

inner.close(); jump.close()
print("Done.")
