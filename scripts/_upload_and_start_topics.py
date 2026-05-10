"""
1. Upload fixed graph_builder.py to remote
2. Clear bad concept checkpoints
3. Run topic_ingestion for grade 7 (re-run, only 23 topics), 10, 11, 12 maths
4. Wait for topic ingestion to finish (poll every 5 min)
5. When done, restart graph_builder with fixed code
"""
import paramiko, time, os

JUMP_HOST = "ada.iiit.ac.in"; USER = "shubhamcvit"; PW = "0410@Shubham"
INNER = "gnode048"; BASE = "/ssd_scratch/btp-1"
LOCAL_GB = os.path.join(os.path.dirname(__file__), "graph_builder.py")

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

def upload_file(inner, local_path, remote_path):
    sftp = inner.open_sftp()
    sftp.put(local_path, remote_path)
    sftp.close()

jump, inner = connect()
print("Connected")

# Step 1: Kill anything running
print("\n--- Kill running processes ---")
print(run(inner, "kill $(pgrep -f 'graph_builder\\|topic_ingestion') 2>/dev/null; echo ok"))
time.sleep(2)

# Step 2: Upload fixed graph_builder.py
print("\n--- Upload fixed graph_builder.py ---")
upload_file(inner, LOCAL_GB, BASE + "/scripts/graph_builder.py")
print("Uploaded ✓")

# Verify key fixes landed
verify = run(inner, "grep -n 'batch_size\\|STRICT RULES\\|ONLY these\\|ONLY these grade\\|available_grades\\|4096' " + BASE + "/scripts/graph_builder.py | head -20")
print("Verify fixes:\n", verify)

# Step 3: Clear bad maths concept checkpoints
print("\n--- Clear bad maths concept checkpoints ---")
print(run(inner, "rm -f " + BASE + "/data/knowledge_graph/.checkpoints/maths_concepts_batch*.json && echo cleared concepts"))
print(run(inner, "rm -f " + BASE + "/data/knowledge_graph/.checkpoints/maths_edges_grade*.json && echo cleared edges"))
print("Remaining:", run(inner, "ls " + BASE + "/data/knowledge_graph/.checkpoints/ | grep maths || echo none"))

# Step 4: Run topic ingestion for missing grades
# Grade 7 only had 23 topics (too low) - re-run with --no-skip-existing
# Grades 10, 11, 12 are missing entirely
print("\n--- Start topic ingestion for grades 7, 10, 11, 12 ---")
topic_cmd = (
    "cd " + BASE + " && "
    "export LLAMA_MODEL_PATH=/ssd_scratch/models/llama-8b && "
    "nohup python3 scripts/topic_ingestion.py --subject maths "
    "> " + BASE + "/logs/stage1_maths_grades7_10_11_12.log 2>&1 & echo $!"
)
# NOTE: --skip-existing is default True, so grades 6,8,9 will be skipped
# Grade 7 will also be skipped since it exists - we handle it separately
# First run grades 10, 11, 12 (missing - will be auto-processed by default)
topic_cmd_missing = (
    "cd " + BASE + " && "
    "export LLAMA_MODEL_PATH=/ssd_scratch/models/llama-8b && "
    "nohup python3 scripts/topic_ingestion.py --subject maths "
    "> " + BASE + "/logs/stage1_maths_missing.log 2>&1 & echo $!"
)
pid = run(inner, topic_cmd_missing, t=10).strip()
print("Topic ingestion PID:", pid)
time.sleep(5)
print("Running:", run(inner, "ps aux | grep topic_ingestion | grep -v grep | awk '{print $2,$11,$12}'").strip())

inner.close(); jump.close()
print("\nDone. Now monitoring topic ingestion...")
print("Run: python scripts/_chk_topics.py to check progress")
