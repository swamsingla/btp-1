"""
Launch term conservation extraction on ada/gnode047 GPU cluster.

1. Collects .md topic files for grade9 ch1-3
2. Uploads to cluster via SFTP
3. Runs Qwen3-8B term extraction on gnode047
4. Downloads results

Runs in parallel with the ongoing Sarvam API translation (no GPU needed for API).

Usage:
  python scripts/_run_term_conservation.py
"""
import json
import os
import sys
import time
from pathlib import Path

import paramiko

# ── Cluster config ──────────────────────────────────────────────────
ADA_HOST = "ada.iiit.ac.in"
ADA_USER = "shubhamcvit"
ADA_PASS = "0410@Shubham"
GPU_NODE = "gnode047"
SCRATCH = "/ssd_scratch/shubhamcvit/btp"
VENV_PYTHON = "/ssd_scratch/shubhamcvit/venv/bin/python3"
ADA_HOME = f"/home2/{ADA_USER}"

# ── Local paths ─────────────────────────────────────────────────────
ROOT = Path(__file__).parent.parent
MD_ROOT = ROOT / "data" / "output" / "grade9" / "maths"
INTERMEDIATE = ROOT / "data" / "intermediate"
INTERMEDIATE.mkdir(parents=True, exist_ok=True)

CHAPTERS = [1, 2, 3]
OUTPUT_NAME = "grade9_conservation_terms.json"


def ssh_connect_ada():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ADA_HOST, username=ADA_USER, password=ADA_PASS, timeout=30)
    return client


def ssh_connect_gnode(ada):
    transport = ada.get_transport()
    channel = transport.open_channel("direct-tcpip", (GPU_NODE, 22), ("127.0.0.1", 0))
    gnode = paramiko.SSHClient()
    gnode.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    gnode.connect(GPU_NODE, username=ADA_USER, password=ADA_PASS, sock=channel, timeout=30)
    return gnode


def run_cmd(client, cmd, timeout=120):
    _, stdout, stderr = client.exec_command(cmd, timeout=timeout)
    out = stdout.read().decode("utf-8", errors="replace").strip()
    err = stderr.read().decode("utf-8", errors="replace").strip()
    return out, err


def sftp_put(client, local_path, remote_path):
    sftp = client.open_sftp()
    try:
        sftp.put(str(local_path), remote_path)
    finally:
        sftp.close()


def sftp_get(client, remote_path, local_path):
    sftp = client.open_sftp()
    try:
        sftp.get(remote_path, str(local_path))
    finally:
        sftp.close()


def collect_md_files():
    """Collect all .md topic files for grade9 ch1-3."""
    files = {}
    for ch in CHAPTERS:
        ch_dir = MD_ROOT / f"chapter{ch}"
        if not ch_dir.exists():
            print(f"  WARNING: {ch_dir} not found, skipping")
            continue
        for md_file in sorted(ch_dir.glob("*.md")):
            key = f"chapter{ch}/{md_file.name}"
            files[key] = md_file.read_text(encoding="utf-8")
    return files


def main():
    print("=" * 60)
    print("Term Conservation Extraction — Qwen3-8B on gnode047")
    print("=" * 60)

    # Step 1: Collect .md files
    print("\n[Step 1] Collecting .md files for grade9 ch1-3...")
    files = collect_md_files()
    print(f"  Found {len(files)} topic pages:")
    for key in files:
        print(f"    {key} ({len(files[key]):,} chars)")

    input_json = INTERMEDIATE / "grade9_conservation_input.json"
    with open(input_json, "w", encoding="utf-8") as f:
        json.dump(files, f, ensure_ascii=False)
    print(f"  Input JSON: {input_json} ({input_json.stat().st_size // 1024} KB)")

    # Step 2: Connect to cluster
    print("\n[Step 2] Connecting to ada.iiit.ac.in...")
    ada = ssh_connect_ada()
    print("  Connected to ada")

    print(f"  Connecting to {GPU_NODE} via ProxyJump...")
    try:
        gnode = ssh_connect_gnode(ada)
        print(f"  Connected to {GPU_NODE}")
    except Exception as e:
        print(f"  ERROR: Cannot reach {GPU_NODE}: {e}")
        print("  Make sure you have an active SLURM job on gnode047")
        ada.close()
        sys.exit(1)

    # Check GPU availability
    out, _ = run_cmd(gnode, "nvidia-smi --query-gpu=name,memory.used,memory.total --format=csv,noheader,nounits")
    print(f"  GPU status:\n    {out.replace(chr(10), chr(10) + '    ')}")

    # Step 3: Upload files
    print("\n[Step 3] Uploading files to cluster...")
    work_dir = f"{ADA_HOME}/btp_conservation"
    scratch_work = f"{SCRATCH}/conservation_work"

    run_cmd(ada, f"mkdir -p {work_dir}")
    run_cmd(gnode, f"mkdir -p {scratch_work}")

    # Upload input JSON
    remote_input_ada = f"{work_dir}/conservation_input.json"
    sftp_put(ada, input_json, remote_input_ada)
    print(f"  Uploaded input JSON to ada:{remote_input_ada}")

    # Upload extractor script
    extractor_local = Path(__file__).parent / "_term_conservation.py"
    remote_extractor_ada = f"{work_dir}/_term_conservation.py"
    sftp_put(ada, extractor_local, remote_extractor_ada)
    print(f"  Uploaded extractor script")

    # Copy from ada home to gnode scratch
    run_cmd(ada, f"scp {remote_input_ada} {GPU_NODE}:{scratch_work}/conservation_input.json")
    run_cmd(ada, f"scp {remote_extractor_ada} {GPU_NODE}:{scratch_work}/_term_conservation.py")
    print(f"  Copied to gnode047:{scratch_work}/")

    # Step 4: Launch extraction
    print("\n[Step 4] Launching Qwen3-8B term conservation extraction...")
    remote_output = f"{scratch_work}/{OUTPUT_NAME}"
    log_file = f"{scratch_work}/conservation_log.txt"

    launch_cmd = (
        f"cd {scratch_work} && "
        f"nohup {VENV_PYTHON} _term_conservation.py "
        f"conservation_input.json {OUTPUT_NAME} "
        f"> {log_file} 2>&1 </dev/null & disown; echo LAUNCHED_PID=$!"
    )

    _, stdout, _ = gnode.exec_command(launch_cmd)
    deadline = time.time() + 30
    out = ""
    while time.time() < deadline:
        if stdout.channel.recv_ready():
            out += stdout.channel.recv(4096).decode("utf-8", errors="replace")
            if "LAUNCHED_PID=" in out:
                break
        elif stdout.channel.exit_status_ready():
            try:
                out += stdout.channel.recv(4096).decode("utf-8", errors="replace")
            except Exception:
                pass
            break
        time.sleep(0.2)

    if "LAUNCHED_PID=" in out:
        pid = out.split("LAUNCHED_PID=")[-1].strip()
        print(f"  Process launched (PID={pid})")
    else:
        print(f"  Launch output: {out!r}")

    # Step 5: Monitor until complete
    print("\n[Step 5] Monitoring extraction progress...")
    print("  (Model loading takes ~1-2 min, extraction ~2-3 min per topic)")
    max_wait = 900  # 15 min
    start = time.time()
    last_log = ""

    while time.time() - start < max_wait:
        time.sleep(15)

        # Check if output file exists (= done)
        check, _ = run_cmd(gnode, f"test -f {remote_output} && echo DONE || echo WAIT")
        log, _ = run_cmd(gnode, f"tail -5 {log_file} 2>/dev/null || echo '...'")

        if log != last_log:
            elapsed = int(time.time() - start)
            # Show only the last meaningful line
            log_lines = [l for l in log.strip().split("\n") if l.strip()]
            if log_lines:
                print(f"  [{elapsed}s] {log_lines[-1][:100]}")
            last_log = log

        if "DONE" in check:
            print(f"\n  Extraction complete! ({int(time.time() - start)}s)")
            break

        # Check if process died
        proc_check, _ = run_cmd(gnode, f"ps aux | grep _term_conservation | grep -v grep | wc -l")
        if proc_check.strip() == "0" and time.time() - start > 60:
            print(f"\n  Process seems to have exited. Checking log...")
            full_log, _ = run_cmd(gnode, f"cat {log_file} 2>/dev/null")
            print(full_log[-500:] if len(full_log) > 500 else full_log)
            if "DONE" not in check:
                print("  ERROR: Process died before completion")
                gnode.close()
                ada.close()
                sys.exit(1)
    else:
        print(f"\n  TIMEOUT after {max_wait}s")
        log, _ = run_cmd(gnode, f"tail -10 {log_file} 2>/dev/null")
        print(f"  Last log:\n{log}")
        gnode.close()
        ada.close()
        sys.exit(1)

    # Step 6: Download results
    print("\n[Step 6] Downloading results...")
    run_cmd(ada, f"scp {GPU_NODE}:{remote_output} {work_dir}/{OUTPUT_NAME}")
    local_output = INTERMEDIATE / OUTPUT_NAME
    sftp_get(ada, f"{work_dir}/{OUTPUT_NAME}", local_output)
    print(f"  Saved to: {local_output}")

    # Print summary
    with open(local_output, encoding="utf-8") as f:
        results = json.load(f)

    print(f"\n{'='*60}")
    print(f"Term Conservation Summary")
    print(f"{'='*60}")
    print(f"  Pages processed: {results.get('pages_processed', '?')}")
    print(f"  Total unique terms: {results.get('total_unique', '?')}")

    if "per_page" in results:
        for page_key, terms in results["per_page"].items():
            total = sum(len(v) for v in terms.values())
            print(f"\n  {Path(page_key).stem}: {total} terms")
            for cat, t_list in terms.items():
                if t_list:
                    print(f"    {cat}: {', '.join(t_list[:4])}{'...' if len(t_list) > 4 else ''}")

    # Show full log
    full_log, _ = run_cmd(gnode, f"cat {log_file} 2>/dev/null")
    print(f"\n--- Full extraction log ---\n{full_log}")

    gnode.close()
    ada.close()
    print("\nDone!")


if __name__ == "__main__":
    main()
