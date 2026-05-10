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

def connect():
    jump = paramiko.SSHClient(); jump.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    jump.connect("ada.iiit.ac.in", username="shubhamcvit", password="0410@Shubham", look_for_keys=False, allow_agent=False, timeout=15)
    ch = jump.get_transport().open_channel("direct-tcpip", ("gnode048", 22), ("127.0.0.1", 0))
    inner = paramiko.SSHClient(); inner.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    inner.connect("gnode048", username="shubhamcvit", password="0410@Shubham", sock=ch, look_for_keys=False, allow_agent=False, timeout=15)
    return jump, inner

BASE = "/ssd_scratch/btp-1"
jump, inner = connect()
print("Connected")

# Kill any running graph_builder or topic_ingestion
print("\n--- Kill any running pipelines ---")
print(run(inner, "kill $(pgrep -f 'graph_builder\\|topic_ingestion') 2>/dev/null; echo ok"))
time.sleep(2)

# Check existing raw_topics files for maths
print("\n--- Existing raw_topics for maths ---")
print(run(inner, "ls -lh " + BASE + "/data/intermediate/raw_topics/ 2>/dev/null | grep maths || echo NONE"))

# Count topics in each maths file
print("\n--- Topic counts per grade ---")
check_script = """
import json, glob, os
base = '/ssd_scratch/btp-1/data/intermediate/raw_topics'
for grade in range(6, 13):
    path = f'{base}/grade{grade}_maths.json'
    if os.path.exists(path):
        d = json.load(open(path))
        topics = d.get('topics', [])
        print(f'grade{grade}_maths.json : {len(topics)} topics')
    else:
        print(f'grade{grade}_maths.json : MISSING')
"""
cmd = "python3 << 'PYEOF'\n" + check_script + "\nPYEOF"
print(run(inner, cmd, t=15))

inner.close(); jump.close()
