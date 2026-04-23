"""Upload restart script via SFTP and launch generation for remaining 4 chapters."""
import paramiko, time, sys

ADA_HOST = "ada.iiit.ac.in"
ADA_USER = "shubhamcvit"
ADA_PASS = "0410@Shubham"
GPU_NODE = "gnode047"
SCRATCH = "/ssd_scratch/shubhamcvit/btp"
VENV_PY = "/ssd_scratch/shubhamcvit/venv/bin/python3"
GEN = f"{SCRATCH}/scripts/content_gen_qwen.py"
LOG = f"{SCRATCH}/restart_gen.log"

JOBS = [
    ("grade11", "chapter2", 5),
    ("grade11", "chapter3", 10),
    ("grade12", "chapter2", 3),
    ("grade12", "chapter3", 15),
]

def ssh_ada():
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(ADA_HOST, username=ADA_USER, password=ADA_PASS, timeout=30)
    return c

def gnode(c, cmd, timeout=120):
    _, o, e = c.exec_command(f"ssh {GPU_NODE} '{cmd}'", timeout=timeout)
    return o.read().decode().strip(), e.read().decode().strip()

ada = ssh_ada()
print("Connected to ada")

# Verify gnode047
out, err = gnode(ada, "hostname")
if "Access denied" in err:
    print("ERROR: No SLURM job on gnode047")
    sys.exit(1)
print(f"Node: {out}")

# Build shell script content
lines = ["#!/bin/bash", f"LOG={LOG}", 'echo "=== Restart generation $(date) ===" | tee $LOG']
for grade, chapter, topics in JOBS:
    chunk = f"{SCRATCH}/chunks/{grade}/maths/{chapter}/_all_chunks.json"
    outdir = f"{SCRATCH}/output/{grade}/maths/{chapter}"
    lines.append(f'echo ">>> Generating {grade} {chapter} ({topics} topics) $(date)" | tee -a $LOG')
    lines.append(f"mkdir -p {outdir}")
    lines.append(f"{VENV_PY} {GEN} {chunk} {outdir} 2>&1 | tee -a $LOG")
    lines.append(f'echo ">>> Done {grade} {chapter} $(date)" | tee -a $LOG')
lines.append('echo "=== ALL DONE $(date) ===" | tee -a $LOG')

script_text = "\n".join(lines) + "\n"

# Upload via SFTP to ada home, then copy to scratch via gnode
home_script = f"/home2/{ADA_USER}/btp/restart_gen.sh"
sftp = ada.open_sftp()
try:
    sftp.mkdir(f"/home2/{ADA_USER}/btp")
except:
    pass
with sftp.open(home_script, "w") as f:
    f.write(script_text)
sftp.close()
print(f"Script uploaded to {home_script}")

# Copy to scratch on gnode
gnode(ada, f"cp {home_script} {SCRATCH}/restart_gen.sh && chmod +x {SCRATCH}/restart_gen.sh")
out, _ = gnode(ada, f"cat {SCRATCH}/restart_gen.sh | head -3")
print(f"Script on scratch: {out}")

# Launch with nohup
print("Launching generation...")
gnode(ada, f"nohup bash {SCRATCH}/restart_gen.sh > /dev/null 2>&1 &", timeout=30)
time.sleep(8)

# Verify started
out, _ = gnode(ada, "ps aux | grep content_gen_qwen | grep -v grep | wc -l")
print(f"Active processes: {out}")
out, _ = gnode(ada, f"wc -l {LOG} 2>/dev/null; tail -3 {LOG} 2>/dev/null")
print(f"Log: {out}")

# Monitor
total = len(JOBS)
print(f"\n--- Monitoring {total} chapters (Ctrl+C to stop) ---")
try:
    while True:
        time.sleep(90)
        try:
            tail, _ = gnode(ada, f"tail -8 {LOG}")
            done_c, _ = gnode(ada, f"grep -c '>>> Done' {LOG} 2>/dev/null || echo 0")
            proc, _ = gnode(ada, "ps aux | grep content_gen_qwen | grep -v grep | wc -l")
            md_count, _ = gnode(ada, f"find {SCRATCH}/output/grade11/maths/chapter2 {SCRATCH}/output/grade11/maths/chapter3 {SCRATCH}/output/grade12/maths/chapter2 {SCRATCH}/output/grade12/maths/chapter3 -name '*.md' 2>/dev/null | wc -l")

            ts = time.strftime("%H:%M:%S")
            print(f"\n[{ts}] Chapters done: {done_c}/{total} | .md files: {md_count} | Procs: {proc}")
            for line in tail.split("\n"):
                l = line.strip()
                if l and (">>>" in l or "importance" in l or "chars," in l or "skipping" in l or "topics" in l or "Generating:" in l or "Done!" in l):
                    print(f"  {l[:120]}")

            if "ALL DONE" in tail:
                print("\n*** ALL GENERATION COMPLETED! ***")
                break
            if proc.strip() == "0" and "ALL DONE" not in tail:
                last20, _ = gnode(ada, f"tail -20 {LOG}")
                print(f"\nProcess stopped. Last log:\n{last20}")
                break
        except Exception as e:
            print(f"[{time.strftime('%H:%M:%S')}] Error: {e}")
            try:
                ada = ssh_ada()
            except:
                pass
except KeyboardInterrupt:
    print("\nMonitoring stopped. Generation continues on cluster.")

ada.close()
