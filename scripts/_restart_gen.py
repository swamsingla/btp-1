"""Check cluster state and restart remaining generation."""
import paramiko, time, sys

ADA_HOST = "ada.iiit.ac.in"
ADA_USER = "shubhamcvit"
ADA_PASS = "0410@Shubham"
GPU_NODE = "gnode047"
SCRATCH = "/ssd_scratch/shubhamcvit/btp"
VENV_PYTHON = "/ssd_scratch/shubhamcvit/venv/bin/python3"
GEN_SCRIPT = f"{SCRATCH}/scripts/content_gen_qwen.py"

def ssh_ada():
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(ADA_HOST, username=ADA_USER, password=ADA_PASS, timeout=30)
    return c

def run_gnode(c, cmd, timeout=120):
    full = f"ssh {GPU_NODE} '{cmd}'"
    _, o, e = c.exec_command(full, timeout=timeout)
    return o.read().decode().strip(), e.read().decode().strip()

def run_ada(c, cmd, timeout=60):
    _, o, e = c.exec_command(cmd, timeout=timeout)
    return o.read().decode().strip(), e.read().decode().strip()

# --- Main ---
ada = ssh_ada()
print("Connected to ada")

# Check gnode047 access
out, err = run_gnode(ada, "hostname")
if "Access denied" in err:
    print("ERROR: No active SLURM job on gnode047!")
    print("You need to submit a job first: srun --gres=gpu:3 --pty bash")
    ada.close()
    sys.exit(1)
print(f"gnode047: {out}")

# Check GPU state
out, _ = run_gnode(ada, "nvidia-smi --query-gpu=name,memory.used,memory.total --format=csv,noheader")
print(f"GPUs:\n{out}")

# Check running processes
out, _ = run_gnode(ada, "ps aux | grep content_gen | grep -v grep")
if out:
    print(f"Running process: {out}")
else:
    print("No generation process running")

# Check what outputs exist for remaining chapters
remaining = [
    ("grade11", "chapter2"),
    ("grade11", "chapter3"),
    ("grade12", "chapter2"),
    ("grade12", "chapter3"),
]

print("\n--- Remaining chapters status ---")
jobs_needed = []
for grade, chapter in remaining:
    outdir = f"{SCRATCH}/output/{grade}/maths/{chapter}"
    out, _ = run_gnode(ada, f"ls {outdir}/_index.json 2>/dev/null && echo COMPLETE || echo INCOMPLETE; ls {outdir}/*.md 2>/dev/null | wc -l")
    lines = out.strip().split("\n")
    status = lines[0] if lines else "UNKNOWN"
    md_count = lines[1].strip() if len(lines) > 1 else "0"
    print(f"  {grade}/{chapter}: {status} ({md_count} .md files)")
    
    if "INCOMPLETE" in status:
        chunk_file = f"{SCRATCH}/chunks/{grade}/maths/{chapter}/_all_chunks.json"
        chk, _ = run_gnode(ada, f"test -f {chunk_file} && echo OK || echo MISSING")
        if "OK" in chk:
            jobs_needed.append((grade, chapter, chunk_file, outdir))
            print(f"    -> chunks ready: {chunk_file}")
        else:
            print(f"    -> ERROR: chunks missing at {chunk_file}")

if not jobs_needed:
    print("\nAll chapters already complete!")
    ada.close()
    sys.exit(0)

print(f"\n--- Starting generation for {len(jobs_needed)} chapters ---")

# Build and run the generation commands sequentially via nohup
cmds = []
for grade, chapter, chunk_file, outdir in jobs_needed:
    cmds.append(f'echo ">>> Starting {grade}/{chapter} $(date)"')
    cmds.append(f"mkdir -p {outdir}")
    cmds.append(f"{VENV_PYTHON} {GEN_SCRIPT} {chunk_file} {outdir}")
    cmds.append(f'echo ">>> Done {grade}/{chapter} $(date)"')

log_file = f"{SCRATCH}/restart_gen.log"
script_content = "#!/bin/bash\\n" + "\\n".join(cmds) + f'\\necho "=== ALL DONE $(date) ==="'

# Write script to cluster
run_gnode(ada, f"echo -e '{script_content}' > {SCRATCH}/restart_gen.sh && chmod +x {SCRATCH}/restart_gen.sh")

# Run via nohup
print(f"Starting nohup generation, logging to {log_file}")
run_gnode(ada, f"nohup bash {SCRATCH}/restart_gen.sh > {log_file} 2>&1 &", timeout=30)
time.sleep(5)

# Verify it started
out, _ = run_gnode(ada, f"ps aux | grep content_gen | grep -v grep | wc -l")
print(f"Active processes: {out}")

out, _ = run_gnode(ada, f"head -5 {log_file} 2>/dev/null")
print(f"Log start: {out}")

# Monitor loop
print("\n--- Monitoring (Ctrl+C to stop, generation continues on cluster) ---")
try:
    while True:
        time.sleep(90)
        try:
            # Check log tail
            tail, _ = run_gnode(ada, f"tail -5 {log_file}")
            
            # Count completed chapters
            done, _ = run_gnode(ada, f"grep -c '>>> Done' {log_file} 2>/dev/null || echo 0")
            
            # Check if process still alive
            proc, _ = run_gnode(ada, "ps aux | grep content_gen | grep -v grep | wc -l")
            
            # Count total .md files
            md_count, _ = run_gnode(ada, f"find {SCRATCH}/output/grade11/maths/chapter2 {SCRATCH}/output/grade11/maths/chapter3 {SCRATCH}/output/grade12/maths/chapter2 {SCRATCH}/output/grade12/maths/chapter3 -name '*.md' 2>/dev/null | wc -l")
            
            ts = time.strftime("%H:%M:%S")
            print(f"[{ts}] Done: {done}/{len(jobs_needed)} chapters | {md_count} .md files | Procs: {proc}")
            
            # Show current activity
            for line in tail.split("\n"):
                line = line.strip()
                if line and (">>>" in line or "importance" in line or "chars," in line or "skipping" in line):
                    print(f"  {line[:100]}")
            
            # Check if all done
            if "ALL DONE" in tail:
                print("\nAll generation completed!")
                break
            
            if proc.strip() == "0" and "ALL DONE" not in tail:
                print("\nWARNING: Process died. Check log:")
                last, _ = run_gnode(ada, f"tail -20 {log_file}")
                print(last)
                break
                
        except Exception as e:
            print(f"[{time.strftime('%H:%M:%S')}] Monitor error: {e}, reconnecting...")
            ada = ssh_ada()

except KeyboardInterrupt:
    print(f"\nMonitoring stopped. Check: ssh gnode047 'tail -50 {log_file}'")

ada.close()
