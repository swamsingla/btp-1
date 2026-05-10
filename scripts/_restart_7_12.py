"""
Kill current grade12 ingestion, upload fixed topic_ingestion.py (** glob fix),
delete grade7 and grade12 output files, re-run both from scratch.
"""
import paramiko, time, os, json

JUMP_HOST = "ada.iiit.ac.in"; USER = "shubhamcvit"; PW = "0410@Shubham"
INNER_HOST = "gnode048"; BASE = "/ssd_scratch/btp-1"
SCRIPTS = os.path.dirname(os.path.abspath(__file__))

def run(c, cmd, t=25):
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
    ch = jump.get_transport().open_channel("direct-tcpip", (INNER_HOST, 22), ("127.0.0.1", 0))
    inner = paramiko.SSHClient(); inner.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    inner.connect(INNER_HOST, username=USER, password=PW, sock=ch, look_for_keys=False, allow_agent=False, timeout=15)
    return jump, inner

def upload_file(inner, local, remote):
    sftp = inner.open_sftp(); sftp.put(local, remote); sftp.close()
    print(f"  Uploaded {os.path.basename(local)} OK")

jump, inner = connect()

# Kill all topic_ingestion processes
print("Killing any topic_ingestion processes...")
print(run(inner, "pkill -f 'topic_ingestion' 2>/dev/null; echo done"))
time.sleep(2)

# Upload fixed topic_ingestion.py (** glob fix)
print("Uploading topic_ingestion.py with ** glob fix...")
upload_file(inner, os.path.join(SCRIPTS, "topic_ingestion.py"), BASE + "/scripts/topic_ingestion.py")

# Verify the glob fix
print("Verify glob fix:")
print(run(inner, f"grep -n 'glob' {BASE}/scripts/topic_ingestion.py").strip())

# Verify NCERT headings exist for grade7 and grade12
print("\nNCERT heading files on remote:")
print(run(inner, f"find {BASE}/data/intermediate/headings/grade7 -name 'chapter*.json' | wc -l"))
print(run(inner, f"find {BASE}/data/intermediate/headings/grade12 -name 'chapter*.json' | wc -l"))

# Delete current (bad) output files for 7 and 12
print("Deleting grade7 and grade12 output files...")
print(run(inner, f"rm -f {BASE}/data/intermediate/raw_topics/grade7_maths.json && echo deleted7"))
print(run(inner, f"rm -f {BASE}/data/intermediate/raw_topics/grade12_maths.json && echo deleted12"))

# Start grade 7
log7 = f"{BASE}/logs/stage1_maths_grade7_v2.log"
cmd7 = (f"cd {BASE} && export LLAMA_MODEL_PATH=/ssd_scratch/models/llama-8b && "
        f"nohup python3 scripts/topic_ingestion.py --subject maths --grade 7 --no-skip-existing "
        f"> {log7} 2>&1 & echo $!")
pid7 = run(inner, cmd7, t=10).strip()
print(f"\nStarted grade 7, PID: {pid7}")

# Reset pipeline state so tick script knows we're back to grade7
state_file = os.path.join(SCRIPTS, "_pipeline_state.json")
json.dump({"phase": "grade7", "log7": log7}, open(state_file, "w"))
print(f"Pipeline state reset to grade7")

time.sleep(6)
print("Log start:")
print(run(inner, f"tail -6 {log7} 2>/dev/null"))

inner.close(); jump.close()
print("\nRestarted. Run the PS monitor loop now.")
