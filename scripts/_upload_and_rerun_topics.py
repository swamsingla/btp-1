"""
Upload fixed topic_ingestion.py and graph_builder.py, then:
- Re-run grade 7 with --no-skip-existing (only 23 topics, suspicious)
- Re-run grades 10, 11, 12 (failed previously)
- Delete grade 12 empty file so it gets regenerated
"""
import paramiko, time, os

JUMP_HOST = "ada.iiit.ac.in"; USER = "shubhamcvit"; PW = "0410@Shubham"
INNER = "gnode048"; BASE = "/ssd_scratch/btp-1"
SCRIPTS = os.path.join(os.path.dirname(__file__))

def run(c, cmd, t=30):
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
    jump.connect(JUMP_HOST, username=USER, password=PW, look_for_keys=False, allow_agent=False, timeout=15)
    ch = jump.get_transport().open_channel("direct-tcpip", (INNER, 22), ("127.0.0.1", 0))
    inner = paramiko.SSHClient(); inner.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    inner.connect(INNER, username=USER, password=PW, sock=ch, look_for_keys=False, allow_agent=False, timeout=15)
    return jump, inner

def upload(inner, local, remote):
    sftp = inner.open_sftp(); sftp.put(local, remote); sftp.close()

jump, inner = connect()
print("Connected")

# Upload fixed scripts
print("\n--- Upload fixed scripts ---")
upload(inner, os.path.join(SCRIPTS, "topic_ingestion.py"), BASE + "/scripts/topic_ingestion.py")
print("topic_ingestion.py uploaded ✓")
upload(inner, os.path.join(SCRIPTS, "graph_builder.py"), BASE + "/scripts/graph_builder.py")
print("graph_builder.py uploaded ✓")

# Verify fix landed
print("\nVerify fix:")
print(run(inner, "grep -n 'raw_name.*get\\|name_key.*get\\|Normalise\\|cleaned' " + BASE + "/scripts/topic_ingestion.py | head -10"))

# Delete bad/empty output files so they get regenerated
print("\n--- Delete bad output files ---")
print(run(inner, "rm -f " + BASE + "/data/intermediate/raw_topics/grade12_maths.json && echo deleted grade12"))
print(run(inner, "rm -f " + BASE + "/data/intermediate/raw_topics/grade7_maths.json && echo deleted grade7"))
# Keep grade 10, 11 (they don't exist, so no action needed)

# Run topic ingestion: grades 7, 10, 11, 12 for maths
# Since grade7 and grade12 are deleted and grade10/11 were never written, --skip-existing will process all 4
print("\n--- Start topic ingestion for grades 7, 10, 11, 12 ---")
cmd = (
    "cd " + BASE + " && "
    "export LLAMA_MODEL_PATH=/ssd_scratch/models/llama-8b && "
    "nohup python3 scripts/topic_ingestion.py --subject maths "
    "> " + BASE + "/logs/stage1_maths_v2.log 2>&1 & echo $!"
)
pid = run(inner, cmd, t=10).strip()
print("PID:", pid)
time.sleep(8)

# Confirm running
print("Running:", run(inner, "ps aux | grep topic_ingestion | grep -v grep | awk '{print $2,$3,$11,$12}'").strip())

# Show start of log
print("\nLog start:")
print(run(inner, "tail -15 " + BASE + "/logs/stage1_maths_v2.log 2>/dev/null"))

inner.close(); jump.close()
print("\nDone. Use _chk.py to monitor.")
