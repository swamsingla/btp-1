"""
Batch orchestrator: transfer chunks to cluster, run generation, monitor progress.
Uses paramiko for passwordless SSH to ada.iiit.ac.in -> gnode047.
"""
import json
import os
import re
import sys
import time
from pathlib import Path

import paramiko

# ── Config ──────────────────────────────────────────────────
ADA_HOST = "ada.iiit.ac.in"
ADA_USER = "shubhamcvit"
ADA_PASS = "0410@Shubham"
GPU_NODE = "gnode047"

SCRATCH = "/ssd_scratch/shubhamcvit/btp"
VENV_PYTHON = "/ssd_scratch/shubhamcvit/venv/bin/python3"
GEN_SCRIPT = f"{SCRATCH}/scripts/content_gen_qwen.py"

ROOT = Path(__file__).parent.parent
CHUNKS_LOCAL = ROOT / "data" / "intermediate" / "chunks"

# ── Chapters to generate ───────────────────────────────────
# (grade, chunk_subpath, output_subpath)
# chunk_subpath: relative path under chunks/ to the chapter dir
# output_subpath: path for output on cluster (grade{N}/maths/chapter{M})
JOBS = []

# Grade 6: direct structure
for ch in [1, 2, 3]:
    JOBS.append((6, f"grade6/maths/chapter{ch}", f"grade6/maths/chapter{ch}"))

# Grade 7: part1 structure  
for ch in [1, 2, 3]:
    JOBS.append((7, f"grade7/maths/part1/chapter{ch}", f"grade7/maths/chapter{ch}"))

# Grade 8: part1 structure
for ch in [1, 2, 3]:
    JOBS.append((8, f"grade8/maths/part1/chapter{ch}", f"grade8/maths/chapter{ch}"))

# Grade 9: chapters 2-3 only (ch1 done)
for ch in [2, 3]:
    JOBS.append((9, f"grade9/maths/chapter{ch}", f"grade9/maths/chapter{ch}"))

# Grade 10: chapters 2-3 only
for ch in [2, 3]:
    JOBS.append((10, f"grade10/maths/chapter{ch}", f"grade10/maths/chapter{ch}"))

# Grade 11: chapters 2-3 only
for ch in [2, 3]:
    JOBS.append((11, f"grade11/maths/chapter{ch}", f"grade11/maths/chapter{ch}"))

# Grade 12: part1 structure, chapters 2-3 only
for ch in [2, 3]:
    JOBS.append((12, f"grade12/maths/part1/chapter{ch}", f"grade12/maths/chapter{ch}"))


def ssh_connect_ada():
    """Connect to ada login node."""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ADA_HOST, username=ADA_USER, password=ADA_PASS, timeout=30)
    return client


def run_on_ada(client, cmd, timeout=60):
    """Run command on ada, return stdout."""
    _, stdout, stderr = client.exec_command(cmd, timeout=timeout)
    out = stdout.read().decode("utf-8", errors="replace")
    err = stderr.read().decode("utf-8", errors="replace")
    return out.strip(), err.strip()


def run_on_gnode(client, cmd, timeout=600):
    """Run command on gnode047 via ada."""
    full_cmd = f"ssh {GPU_NODE} '{cmd}'"
    return run_on_ada(client, full_cmd, timeout=timeout)


def sftp_upload_dir(client, local_dir, remote_dir):
    """Upload a directory to ada via SFTP."""
    sftp = client.open_sftp()
    
    # Create remote dir hierarchy
    parts = remote_dir.split("/")
    current = ""
    for part in parts:
        current += f"/{part}" if current else part
        if current.startswith("/"):
            try:
                sftp.stat(current)
            except FileNotFoundError:
                sftp.mkdir(current)
    
    # Upload all files from local_dir
    local_path = Path(local_dir)
    for f in local_path.iterdir():
        if f.is_file():
            remote_path = f"{remote_dir}/{f.name}"
            sftp.put(str(f), remote_path)
    
    sftp.close()


def upload_chunks_to_scratch(client, chunk_subpath, output_subpath):
    """Upload chunk dir from local to scratch on gnode047 via ada home as relay."""
    local_dir = CHUNKS_LOCAL / chunk_subpath
    if not local_dir.exists():
        print(f"    ERROR: local chunk dir not found: {local_dir}")
        return False
    
    # Upload to ada home first, then copy to scratch via gnode
    ada_tmp = f"/home2/{ADA_USER}/btp/chunks_tmp/{output_subpath}"
    scratch_dest = f"{SCRATCH}/chunks/{output_subpath}"
    
    # Create dir on ada
    run_on_ada(client, f"mkdir -p {ada_tmp}")
    
    # Upload files via SFTP
    sftp_upload_dir(client, local_dir, ada_tmp)
    
    # Copy from ada home to scratch on gnode
    run_on_gnode(client, f"mkdir -p {scratch_dest} && cp -f {ada_tmp}/* {scratch_dest}/")
    
    return True


def check_output_exists(client, output_subpath):
    """Check if output already has generated files on scratch."""
    out_dir = f"{SCRATCH}/output/{output_subpath}"
    out, _ = run_on_gnode(client, f"ls {out_dir}/_index.json 2>/dev/null && echo EXISTS || echo MISSING")
    return "EXISTS" in out


def main():
    print("=" * 60)
    print("BTP Batch Generation Orchestrator")
    print("=" * 60)
    print(f"\nJobs: {len(JOBS)} chapters to process")
    print(f"Cluster: {ADA_USER}@{ADA_HOST} -> {GPU_NODE}")
    print(f"Scratch: {SCRATCH}\n")
    
    # ── Step 1: Connect to ada ──────────────────────────────
    print("[1] Connecting to ada...")
    ada = ssh_connect_ada()
    print("    Connected to ada")
    
    # Check gnode047 access
    out, err = run_on_gnode(ada, "hostname && nvidia-smi --query-gpu=name,memory.used,memory.total --format=csv,noheader 2>/dev/null || echo 'GPU_CHECK_FAILED'")
    if "GPU_CHECK_FAILED" in out or "Access denied" in err:
        print(f"    ERROR: Cannot access {GPU_NODE}. Need active SLURM job.")
        print(f"    stderr: {err}")
        ada.close()
        sys.exit(1)
    print(f"    gnode047 accessible: {out.splitlines()[0] if out else 'ok'}")
    for line in out.splitlines()[1:]:
        print(f"    GPU: {line.strip()}")
    
    # ── Step 2: Upload chunks ───────────────────────────────
    print(f"\n[2] Uploading chunks to scratch...")
    jobs_to_run = []
    
    for grade, chunk_sub, out_sub in JOBS:
        # Check if already completed
        if check_output_exists(ada, out_sub):
            print(f"    Grade {grade} {out_sub.split('/')[-1]}: SKIP (output exists)")
            continue
        
        # Check if chunks already on scratch
        scratch_chunk = f"{SCRATCH}/chunks/{out_sub}/_all_chunks.json"
        chk_out, _ = run_on_gnode(ada, f"test -f {scratch_chunk} && echo EXISTS || echo MISSING")
        
        if "EXISTS" in chk_out:
            print(f"    Grade {grade} {out_sub.split('/')[-1]}: chunks already on scratch")
        else:
            print(f"    Grade {grade} {out_sub.split('/')[-1]}: uploading chunks...")
            if not upload_chunks_to_scratch(ada, chunk_sub, out_sub):
                continue
            # Verify upload
            chk_out2, _ = run_on_gnode(ada, f"test -f {scratch_chunk} && echo OK || echo FAIL")
            if "FAIL" in chk_out2:
                print(f"    ERROR: chunk upload verification failed for {out_sub}")
                continue
            print(f"    Grade {grade} {out_sub.split('/')[-1]}: chunks uploaded")
        
        jobs_to_run.append((grade, out_sub))
    
    if not jobs_to_run:
        print("\n    No jobs to run - all already completed!")
        ada.close()
        return
    
    print(f"\n    {len(jobs_to_run)} chapters ready for generation")
    
    # ── Step 3: Create batch script on cluster ──────────────
    print(f"\n[3] Creating batch generation script on cluster...")
    
    gen_commands = []
    for grade, out_sub in jobs_to_run:
        chunk_file = f"{SCRATCH}/chunks/{out_sub}/_all_chunks.json"
        output_dir = f"{SCRATCH}/output/{out_sub}"
        gen_commands.append(
            f'echo ">>> Generating: Grade {grade} {out_sub.split("/")[-1]} ($(date))" | tee -a $LOG\n'
            f'mkdir -p {output_dir}\n'
            f'{VENV_PYTHON} {GEN_SCRIPT} {chunk_file} {output_dir} 2>&1 | tee -a $LOG\n'
            f'echo ">>> Done: Grade {grade} {out_sub.split("/")[-1]} ($(date))" | tee -a $LOG\n'
            f'echo "" | tee -a $LOG'
        )
    
    batch_script = f"""#!/bin/bash
LOG="{SCRATCH}/batch_gen_$(date +%Y%m%d_%H%M%S).log"
echo "=== Batch Generation Started: $(date) ===" | tee $LOG
echo "Jobs: {len(jobs_to_run)} chapters" | tee -a $LOG
echo "" | tee -a $LOG

{chr(10).join(gen_commands)}

echo "" | tee -a $LOG
echo "=== Batch Generation Completed: $(date) ===" | tee -a $LOG
echo "All done! Log: $LOG"
"""
    
    # Write script to ada home, then copy to scratch
    script_path = f"/home2/{ADA_USER}/btp/batch_run.sh"
    scratch_script = f"{SCRATCH}/batch_run.sh"
    
    sftp = ada.open_sftp()
    run_on_ada(ada, f"mkdir -p /home2/{ADA_USER}/btp")
    with sftp.open(script_path, "w") as f:
        f.write(batch_script)
    sftp.close()
    
    run_on_gnode(ada, f"cp {script_path} {scratch_script} && chmod +x {scratch_script}")
    print(f"    Script created: {scratch_script}")
    print(f"    Jobs: {len(jobs_to_run)}")
    for g, o in jobs_to_run:
        print(f"      - Grade {g}: {o.split('/')[-1]}")
    
    # ── Step 4: Start generation in background ──────────────
    print(f"\n[4] Starting generation on {GPU_NODE}...")
    
    # Run in background with nohup so it survives SSH disconnect
    run_on_gnode(ada, f"nohup bash {scratch_script} > /dev/null 2>&1 &", timeout=30)
    time.sleep(3)
    
    # Verify it started
    out, _ = run_on_gnode(ada, "ps aux | grep content_gen_qwen | grep -v grep | head -1")
    if out:
        print(f"    Generation process running: {out[:80]}...")
    else:
        # Check if log was created
        out2, _ = run_on_gnode(ada, f"ls -t {SCRATCH}/batch_gen_*.log 2>/dev/null | head -1")
        if out2:
            print(f"    Log created: {out2}")
            # Check first lines
            out3, _ = run_on_gnode(ada, f"head -5 {out2}")
            print(f"    Log start: {out3}")
        else:
            print("    WARNING: Process may not have started. Check manually.")
    
    # ── Step 5: Monitor progress ────────────────────────────
    print(f"\n[5] Monitoring progress...")
    print("    (Ctrl+C to stop monitoring - generation continues on cluster)\n")
    
    total_jobs = len(jobs_to_run)
    completed = 0
    
    try:
        while completed < total_jobs:
            time.sleep(60)  # Check every 60 seconds
            
            try:
                # Find latest log file
                log_path, _ = run_on_gnode(ada, f"ls -t {SCRATCH}/batch_gen_*.log 2>/dev/null | head -1")
                if not log_path:
                    print(f"    [{time.strftime('%H:%M:%S')}] No log file found yet...")
                    continue
                
                # Get last 20 lines of log
                tail, _ = run_on_gnode(ada, f"tail -20 {log_path}")
                
                # Count completed jobs
                done_out, _ = run_on_gnode(ada, f"grep -c '>>> Done:' {log_path} 2>/dev/null || echo 0")
                try:
                    completed = int(done_out.strip())
                except (ValueError, IndexError):
                    completed = 0
                
                # Get currently generating topic
                current = ""
                for line in tail.splitlines():
                    if "Generating:" in line or "importance:" in line or "chars," in line:
                        current = line.strip()
                
                print(f"    [{time.strftime('%H:%M:%S')}] Progress: {completed}/{total_jobs} chapters | {current[:80]}")
                
                # Check if process still running
                proc_out, _ = run_on_gnode(ada, "ps aux | grep content_gen_qwen | grep -v grep | wc -l")
                if proc_out.strip() == "0" and completed < total_jobs:
                    # Check if batch finished or crashed
                    last_line, _ = run_on_gnode(ada, f"tail -1 {log_path}")
                    if "Completed" in last_line:
                        print(f"\n    Generation completed!")
                        break
                    else:
                        print(f"\n    WARNING: Process seems to have stopped. Last log line:")
                        print(f"    {last_line}")
                        break
                
                if completed >= total_jobs:
                    print(f"\n    All {total_jobs} chapters generated!")
                    break
                    
            except Exception as e:
                print(f"    [{time.strftime('%H:%M:%S')}] Monitor error: {e}")
                # Reconnect if needed
                try:
                    ada.exec_command("echo ping", timeout=5)
                except:
                    print("    Reconnecting to ada...")
                    ada = ssh_connect_ada()
    
    except KeyboardInterrupt:
        print(f"\n\n    Monitoring stopped. Generation continues on cluster.")
        print(f"    To check later: ssh {ADA_USER}@{ADA_HOST}")
        print(f"    Then: ssh {GPU_NODE} 'tail -50 {SCRATCH}/batch_gen_*.log'")
    
    ada.close()
    print("\nDone.")


if __name__ == "__main__":
    main()
