"""Restart generation for grade12 ch2 & ch3 with OOM fix."""
import paramiko, time, sys

ADA_HOST = "ada.iiit.ac.in"
ADA_USER = "shubhamcvit"
ADA_PASS = "0410@Shubham"
GPU_NODE = "gnode047"
SCRATCH = "/ssd_scratch/shubhamcvit/btp"
VENV_PY = "/ssd_scratch/shubhamcvit/venv/bin/python3"
GEN = f"{SCRATCH}/scripts/content_gen_qwen.py"
LOG = f"{SCRATCH}/restart_gen2.log"

JOBS = [
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

out, err = gnode(ada, "hostname")
if "Access denied" in err:
    print("ERROR: No SLURM job on gnode047")
    sys.exit(1)
print(f"Node: {out}")

# Kill any lingering processes
gnode(ada, "pkill -f content_gen_qwen || true")
time.sleep(2)

# Build shell script with OOM fix
lines = [
    "#!/bin/bash",
    "export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True",
    f"LOG={LOG}",
    'echo "=== Restart generation v2 $(date) ===" | tee $LOG',
]
for grade, chapter, topics in JOBS:
    chunk = f"{SCRATCH}/chunks/{grade}/maths/{chapter}/_all_chunks.json"
    outdir = f"{SCRATCH}/output/{grade}/maths/{chapter}"
    lines.append(f'echo ">>> Generating {grade} {chapter} ({topics} topics) $(date)" | tee -a $LOG')
    lines.append(f"mkdir -p {outdir}")
    lines.append(f"{VENV_PY} {GEN} {chunk} {outdir} 2>&1 | tee -a $LOG")
    lines.append(f'echo ">>> Done {grade} {chapter} $(date)" | tee -a $LOG')
lines.append('echo "=== ALL DONE $(date) ===" | tee -a $LOG')

script_text = "\n".join(lines) + "\n"

# Upload via SFTP
home_script = f"/home2/{ADA_USER}/btp/restart_gen2.sh"
sftp = ada.open_sftp()
try:
    sftp.mkdir(f"/home2/{ADA_USER}/btp")
except:
    pass
with sftp.open(home_script, "w") as f:
    f.write(script_text)
sftp.close()
print(f"Script uploaded to {home_script}")

gnode(ada, f"cp {home_script} {SCRATCH}/restart_gen2.sh && chmod +x {SCRATCH}/restart_gen2.sh")

# Check existing .md files before restart
for grade, chapter, _ in JOBS:
    out, _ = gnode(ada, f"ls {SCRATCH}/output/{grade}/maths/{chapter}/*.md 2>/dev/null | wc -l")
    print(f"  {grade}/{chapter}: {out} existing .md files (will be skipped)")

# Launch
print("Launching generation...")
gnode(ada, f"nohup bash {SCRATCH}/restart_gen2.sh > /dev/null 2>&1 &", timeout=30)
time.sleep(8)

out, _ = gnode(ada, "ps aux | grep content_gen_qwen | grep -v grep | wc -l")
print(f"Active processes: {out}")
out, _ = gnode(ada, f"tail -5 {LOG} 2>/dev/null")
print(f"Log tail:\n{out}")

# Monitor
total = len(JOBS)
print(f"\n--- Monitoring {total} chapters (Ctrl+C to stop) ---")
try:
    while True:
        time.sleep(90)
        try:
            tail, _ = gnode(ada, f"tail -10 {LOG}")
            proc, _ = gnode(ada, "ps aux | grep content_gen_qwen | grep -v grep | wc -l")
            md12c2, _ = gnode(ada, f"ls {SCRATCH}/output/grade12/maths/chapter2/*.md 2>/dev/null | wc -l")
            md12c3, _ = gnode(ada, f"ls {SCRATCH}/output/grade12/maths/chapter3/*.md 2>/dev/null | wc -l")

            ts = time.strftime("%H:%M:%S")
            print(f"\n[{ts}] gr12ch2: {md12c2}/3 .md | gr12ch3: {md12c3}/15 .md | Procs: {proc}")
            for line in tail.split("\n"):
                l = line.strip()
                if l and (">>>" in l or "importance" in l or "skipping" in l or "tokens]" in l or "Done!" in l or "ALL DONE" in l or "Error" in l or "OOM" in l):
                    print(f"  {l[:120]}")

            if "ALL DONE" in tail:
                print("\n*** ALL GENERATION COMPLETED! ***")
                break
            if proc.strip() == "0" and "ALL DONE" not in tail:
                last, _ = gnode(ada, f"tail -20 {LOG}")
                print(f"\nProcess stopped unexpectedly. Last log:\n{last}")
                break
        except Exception as e:
            print(f"[{time.strftime('%H:%M:%S')}] Error: {e}")
            try:
                ada = ssh_ada()
            except:
                pass
except KeyboardInterrupt:
    print("\nMonitoring stopped.")

ada.close()
