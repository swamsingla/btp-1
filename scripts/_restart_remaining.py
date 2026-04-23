"""Restart generation for remaining 4 chapters: Grade 11 Ch2-3, Grade 12 Ch2-3."""
import paramiko
import time

ADA_HOST = 'ada.iiit.ac.in'
ADA_USER = 'shubhamcvit'
ADA_PASS = '0410@Shubham'
GPU_NODE = 'gnode047'
SCRATCH = '/ssd_scratch/shubhamcvit/btp'
VENV_PYTHON = '/ssd_scratch/shubhamcvit/venv/bin/python3'
SCRIPT = f'{SCRATCH}/scripts/content_gen_qwen.py'

# Remaining jobs (chunk_subpath already uploaded to scratch)
REMAINING_JOBS = [
    (11, 'grade11/maths/chapter2', 'grade11/maths/chapter2'),
    (11, 'grade11/maths/chapter3', 'grade11/maths/chapter3'),
    (12, 'grade12/maths/chapter2', 'grade12/maths/chapter2'),
    (12, 'grade12/maths/chapter3', 'grade12/maths/chapter3'),
]

def ssh_connect():
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(ADA_HOST, username=ADA_USER, password=ADA_PASS)
    return c

def run_on_gnode(client, cmd):
    full = f'ssh {GPU_NODE} "{cmd}"'
    _, o, e = client.exec_command(full)
    return o.read().decode(), e.read().decode()

def main():
    c = ssh_connect()
    
    # Build batch script for remaining jobs
    lines = ['#!/bin/bash', f'cd {SCRATCH}', '']
    for grade, chunk_sub, out_sub in REMAINING_JOBS:
        chunk_dir = f'{SCRATCH}/chunks/{chunk_sub}'
        out_dir = f'{SCRATCH}/output/{out_sub}'
        lines.append(f'echo ">>> Generating: Grade {grade} - {out_sub}"')
        lines.append(f'{VENV_PYTHON} {SCRIPT} --chunk-dir {chunk_dir} --output-dir {out_dir} --grade {grade}')
        lines.append(f'echo ">>> Done: Grade {grade} - {out_sub}"')
        lines.append('')
    lines.append('echo "=== ALL REMAINING GENERATION COMPLETE ==="')
    
    script_content = '\n'.join(lines)
    batch_path = f'{SCRATCH}/batch_remaining.sh'
    
    # Write script
    out, err = run_on_gnode(c, f"cat > {batch_path} << 'BATCHEOF'\n{script_content}\nBATCHEOF")
    out, err = run_on_gnode(c, f'chmod +x {batch_path}')
    print(f"Created {batch_path}")
    
    # Generate unique log name
    ts = time.strftime('%Y%m%d_%H%M%S')
    log_file = f'{SCRATCH}/batch_remaining_{ts}.log'
    
    # Start via nohup
    start_cmd = f'cd {SCRATCH} && nohup bash {batch_path} > {log_file} 2>&1 &'
    out, err = run_on_gnode(c, start_cmd)
    time.sleep(3)
    
    # Verify running
    out, err = run_on_gnode(c, 'ps aux | grep content_gen_qwen | grep -v grep | wc -l')
    proc_count = out.strip()
    print(f"Active processes: {proc_count}")
    print(f"Log file: {log_file}")
    
    if proc_count == '0':
        # Check if it started at all
        out, err = run_on_gnode(c, f'cat {log_file}')
        print(f"Log contents:\n{out}")
    
    # Monitor loop
    print("\n=== Starting monitor loop (60s interval) ===")
    while True:
        time.sleep(60)
        try:
            c2 = ssh_connect()
            
            # Check process
            out, _ = run_on_gnode(c2, 'ps aux | grep content_gen_qwen | grep -v grep | wc -l')
            procs = out.strip()
            
            # Check completions
            out, _ = run_on_gnode(c2, f"grep -c '>>> Done:' {log_file} 2>/dev/null || echo 0")
            done = out.strip()
            
            # Last 5 lines
            out, _ = run_on_gnode(c2, f'tail -5 {log_file}')
            
            print(f"\n[{time.strftime('%H:%M:%S')}] Procs: {procs} | Done: {done}/4")
            print(out.strip())
            
            c2.close()
            
            # Check if all done
            if 'ALL REMAINING GENERATION COMPLETE' in out:
                print("\n=== ALL 4 REMAINING CHAPTERS COMPLETE! ===")
                break
            
            if procs == '0' and int(done) < 4:
                print("\nWARNING: Process died again! Check logs.")
                out2, _ = run_on_gnode(ssh_connect(), f'tail -20 {log_file}')
                print(out2)
                break
                
        except Exception as e:
            print(f"Monitor error: {e}")
    
    c.close()

if __name__ == '__main__':
    main()
