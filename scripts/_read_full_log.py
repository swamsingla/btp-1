import paramiko, time

def run(c, cmd, t=20):
    s = c.get_transport().open_session(); s.exec_command(cmd)
    o = b""
    dl = time.time() + t
    while time.time() < dl:
        if s.recv_ready(): o += s.recv(65536)
        if s.exit_status_ready():
            while s.recv_ready(): o += s.recv(65536)
            break
        time.sleep(0.05)
    return o.decode(errors="replace")

jump = paramiko.SSHClient(); jump.set_missing_host_key_policy(paramiko.AutoAddPolicy())
jump.connect("ada.iiit.ac.in", username="shubhamcvit", password="0410@Shubham", look_for_keys=False, allow_agent=False)
ch = jump.get_transport().open_channel("direct-tcpip", ("gnode048", 22), ("127.0.0.1", 0))
inner = paramiko.SSHClient(); inner.set_missing_host_key_policy(paramiko.AutoAddPolicy())
inner.connect("gnode048", username="shubhamcvit", password="0410@Shubham", sock=ch, look_for_keys=False, allow_agent=False)

BASE = "/ssd_scratch/btp-1"

# Full topic ingestion log
print("=== FULL STAGE1 LOG ===")
print(run(inner, "cat " + BASE + "/logs/stage1_maths_missing.log 2>/dev/null", t=15))

# Check files
print("\n=== ALL MATHS TOPIC FILES ===")
check = """
import json, os
base = '/ssd_scratch/btp-1/data/intermediate/raw_topics'
for grade in range(6, 13):
    path = f'{base}/grade{grade}_maths.json'
    if os.path.exists(path):
        d = json.load(open(path))
        topics = d.get('topics', [])
        print(f'grade{grade}: {len(topics)} topics')
        # Show first 3 topic names
        for t in topics[:3]:
            print(f'  - {t[\"raw_name\"]}')
    else:
        print(f'grade{grade}: MISSING')
"""
cmd = "python3 << 'PYEOF'\n" + check + "\nPYEOF"
print(run(inner, cmd, t=10))

inner.close(); jump.close()
