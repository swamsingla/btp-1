"""Upload fixed graph_builder.py, clear stale edge checkpoints, restart, monitor."""
import paramiko, time, json
from pathlib import Path

HOST_JUMP = "ada.iiit.ac.in"
HOST_INNER = "gnode048"
USER = "shubhamcvit"
PASS = "0410@Shubham"
BASE = "/ssd_scratch/btp-1"
LOCAL_BASE = Path(__file__).resolve().parent.parent

j = paramiko.SSHClient(); j.set_missing_host_key_policy(paramiko.AutoAddPolicy())
j.connect(HOST_JUMP, username=USER, password=PASS)
t = j.get_transport().open_channel("direct-tcpip", (HOST_INNER, 22), ("localhost", 0))
inner = paramiko.SSHClient(); inner.set_missing_host_key_policy(paramiko.AutoAddPolicy())
inner.connect(HOST_INNER, username=USER, password=PASS, sock=t)

def run(cmd, timeout=30):
    _, o, e = inner.exec_command(cmd, timeout=timeout)
    return o.read().decode().strip()

def upload(local_path, remote_path):
    sftp = inner.open_sftp()
    sftp.put(str(local_path), remote_path)
    sftp.close()

# 1. Upload fixed graph_builder.py
print("=== UPLOADING FIXED graph_builder.py ===")
upload(LOCAL_BASE / "scripts" / "graph_builder.py", f"{BASE}/scripts/graph_builder.py")
print("  Uploaded graph_builder.py")

# Verify key fix is present
verify = run(f"grep -n 'all_slug_set' {BASE}/scripts/graph_builder.py | head -5")
print(f"  Fix verification (all_slug_set):\n{verify}")

# 2. Kill any running graph_builder
print("\n=== KILLING OLD PROCESSES ===")
run("pkill -9 -f graph_builder 2>/dev/null || true")
time.sleep(2)
procs = run("pgrep -a -f graph_builder 2>/dev/null || echo none")
print(f"  After kill: {procs}")

# 3. Clear stale edge checkpoints AND output
print("\n=== CLEARING STALE EDGE DATA ===")
cleared = run(f"ls {BASE}/data/knowledge_graph/.checkpoints/maths_edges_grade*.json 2>/dev/null | wc -l")
print(f"  Edge checkpoints to delete: {cleared}")
run(f"rm -f {BASE}/data/knowledge_graph/.checkpoints/maths_edges_grade*.json")
run(f"rm -f {BASE}/data/knowledge_graph/graph_by_subject/maths.json")
run(f"rm -f {BASE}/data/knowledge_graph/graph.json")
after = run(f"ls {BASE}/data/knowledge_graph/.checkpoints/maths_edges_grade*.json 2>/dev/null | wc -l")
print(f"  Edge checkpoints remaining: {after}")
concept_ckpts = run(f"ls {BASE}/data/knowledge_graph/.checkpoints/maths_concepts_batch*.json 2>/dev/null | wc -l")
print(f"  Concept checkpoints (preserved): {concept_ckpts}")

# 4. Start graph_builder — write a launcher script, execute it detached
print("\n=== STARTING GRAPH BUILDER ===")
launcher = (
    "#!/bin/bash\n"
    f"cd {BASE}\n"
    f"export LLAMA_MODEL_PATH=/ssd_scratch/models/llama-8b\n"
    f"export PYTHONPATH={BASE}/scripts\n"
    f"nohup /usr/bin/python3 scripts/graph_builder.py --subject maths --no-skip-existing --validate "
    f">> {BASE}/logs/stage2_maths_v5.log 2>&1 &\n"
    "echo $!\n"
)
sftp = inner.open_sftp()
with sftp.open(f"{BASE}/scripts/_launcher_v5.sh", "w") as f:
    f.write(launcher)
sftp.close()
run(f"chmod +x {BASE}/scripts/_launcher_v5.sh")

# Execute and read PID quickly
_, out_ch, _ = inner.exec_command(f"bash {BASE}/scripts/_launcher_v5.sh", timeout=20)
out_ch.channel.settimeout(20)
try:
    pid = out_ch.read().decode().strip()
except Exception:
    pid = "unknown"
print(f"  Started PID: {pid}")

# 5. Wait 15s and tail log
print("\n=== WAITING 15s FOR STARTUP ===")
time.sleep(15)
log_tail = run(f"tail -20 {BASE}/logs/stage2_maths_v5.log 2>/dev/null")
print(log_tail)

# Final status
print("\n=== FINAL STATUS ===")
procs2 = run("pgrep -a -f graph_builder 2>/dev/null || echo none")
print(f"  PIDs: {procs2}")
edge_ckpts = run(f"ls {BASE}/data/knowledge_graph/.checkpoints/maths_edges_grade*.json 2>/dev/null | wc -l")
print(f"  Edge checkpoints: {edge_ckpts}")
print("Done. Run monitor loop now.")

inner.close(); j.close()
