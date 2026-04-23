"""
Transfer all completed chapter outputs from cluster to local,
convert to JSON, and upload to MongoDB.

Skips:
  - grade12/ch2, grade12/ch3 (incomplete)
  - grade6/ch2 (headings start from 2.4 — transfer only, no DB upload)
  - grade9-12/ch1 (already in MongoDB — but still transfers if missing locally)
"""
import paramiko
import os
import stat
import sys
from pathlib import Path

ADA_HOST = "ada.iiit.ac.in"
ADA_USER = "shubhamcvit"
ADA_PASS = "0410@Shubham"
GPU_NODE = "gnode047"
SCRATCH = "/ssd_scratch/shubhamcvit/btp"
ADA_HOME = f"/home2/{ADA_USER}/btp"

ROOT = Path(__file__).parent.parent
LOCAL_OUTPUT = ROOT / "data" / "output"

# All chapters with _index.json on cluster (complete)
COMPLETE = [
    ("grade6", "chapter1"), ("grade6", "chapter2"), ("grade6", "chapter3"),
    ("grade7", "chapter1"), ("grade7", "chapter2"), ("grade7", "chapter3"),
    ("grade8", "chapter1"), ("grade8", "chapter2"), ("grade8", "chapter3"),
    ("grade9", "chapter1"), ("grade9", "chapter2"), ("grade9", "chapter3"),
    ("grade10", "chapter1"), ("grade10", "chapter2"), ("grade10", "chapter3"),
    ("grade11", "chapter1"), ("grade11", "chapter2"), ("grade11", "chapter3"),
    ("grade12", "chapter1"),
]

# Incomplete but bring to local anyway
INCOMPLETE = [
    ("grade12", "chapter2"), ("grade12", "chapter3"),
]

# Skip DB upload for these
SKIP_DB = {
    ("grade6", "chapter2"),   # headings start from 2.4
}

# Already in MongoDB — skip re-upload
ALREADY_IN_DB = {
    ("grade9", "chapter1"), ("grade10", "chapter1"),
    ("grade11", "chapter1"), ("grade12", "chapter1"),
}


def ssh_ada():
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(ADA_HOST, username=ADA_USER, password=ADA_PASS, timeout=30)
    return c


def run_ada(c, cmd, timeout=120):
    _, o, e = c.exec_command(cmd, timeout=timeout)
    return o.read().decode().strip(), e.read().decode().strip()


def sftp_download_dir(sftp, remote_dir, local_dir):
    """Recursively download a directory via SFTP."""
    os.makedirs(local_dir, exist_ok=True)
    for entry in sftp.listdir_attr(remote_dir):
        remote_path = f"{remote_dir}/{entry.filename}"
        local_path = os.path.join(local_dir, entry.filename)
        if stat.S_ISDIR(entry.st_mode):
            sftp_download_dir(sftp, remote_path, local_path)
        else:
            sftp.get(remote_path, local_path)


def main():
    ada = ssh_ada()
    print("Connected to ada")

    # Step 1: Copy outputs from scratch (gnode047) to ada home
    all_chapters = COMPLETE + INCOMPLETE
    print(f"\n=== Step 1: Copy {len(all_chapters)} chapters from scratch to ada home ===")

    # First make the dir structure on ada home
    run_ada(ada, f"mkdir -p {ADA_HOME}/output")

    for grade, chapter in all_chapters:
        src = f"{SCRATCH}/output/{grade}/maths/{chapter}"
        dst = f"{ADA_HOME}/output/{grade}/maths/{chapter}"
        print(f"  Copying {grade}/{chapter}...", end=" ", flush=True)
        run_ada(ada, f"mkdir -p {dst}")
        out, err = run_ada(ada, f"ssh gnode047 'cp -r {src}/* {dst}/' 2>&1", timeout=60)
        if err and "No such file" in err:
            print(f"SKIP (not on node)")
        else:
            print("OK")

    # Step 2: Download from ada home to local via SFTP
    print(f"\n=== Step 2: Download to local ===")
    sftp = ada.open_sftp()

    for grade, chapter in all_chapters:
        remote_dir = f"{ADA_HOME}/output/{grade}/maths/{chapter}"
        local_dir = str(LOCAL_OUTPUT / grade / "maths" / chapter)

        # Check if already exists locally with same file count
        try:
            remote_files = sftp.listdir(remote_dir)
        except FileNotFoundError:
            print(f"  {grade}/{chapter}: not found on ada home, skipping")
            continue

        local_path = Path(local_dir)
        if local_path.exists():
            local_files = list(local_path.iterdir())
            if len(local_files) >= len(remote_files):
                print(f"  {grade}/{chapter}: already local ({len(local_files)} files), skipping")
                continue

        print(f"  {grade}/{chapter}: downloading {len(remote_files)} files...", end=" ", flush=True)
        sftp_download_dir(sftp, remote_dir, local_dir)
        print("OK")

    sftp.close()
    ada.close()
    print("\n=== Transfer complete ===")

    # Step 3: Convert .md to JSON
    print(f"\n=== Step 3: Convert to JSON (md_to_json.py) ===")
    import subprocess
    python = str(ROOT / ".venv" / "Scripts" / "python.exe")
    md_to_json = str(ROOT / "scripts" / "md_to_json.py")

    to_convert = [c for c in COMPLETE]  # only complete chapters
    for grade, chapter in to_convert:
        ch_dir = str(LOCAL_OUTPUT / grade / "maths" / chapter)
        if not Path(ch_dir).exists():
            print(f"  {grade}/{chapter}: no local dir, skipping")
            continue
        json_path = ROOT / "data" / "generated" / grade / "maths" / chapter / "en.json"
        if json_path.exists():
            print(f"  {grade}/{chapter}: en.json exists, skipping")
            continue
        print(f"  {grade}/{chapter}: converting...", end=" ", flush=True)
        r = subprocess.run([python, md_to_json, ch_dir], capture_output=True, text=True)
        if r.returncode == 0:
            print("OK")
        else:
            print(f"FAILED\n    {r.stderr[:200]}")

    # Step 4: Upload to MongoDB
    print(f"\n=== Step 4: Upload to MongoDB ===")
    db_uploader = str(ROOT / "scripts" / "db_uploader.py")

    for grade, chapter in COMPLETE:
        if (grade, chapter) in SKIP_DB:
            print(f"  {grade}/{chapter}: SKIP (excluded from DB)")
            continue
        if (grade, chapter) in ALREADY_IN_DB:
            print(f"  {grade}/{chapter}: already in DB, skipping")
            continue
        json_path = ROOT / "data" / "generated" / grade / "maths" / chapter / "en.json"
        if not json_path.exists():
            print(f"  {grade}/{chapter}: no en.json, skipping")
            continue
        print(f"  {grade}/{chapter}: uploading...", end=" ", flush=True)
        r = subprocess.run([python, db_uploader, str(json_path)], capture_output=True, text=True)
        if r.returncode == 0:
            # Show summary line
            for line in r.stdout.splitlines():
                if "upserted" in line.lower() or "chapter" in line.lower() or "topic" in line.lower():
                    print(line.strip(), end=" ")
            print("OK")
        else:
            print(f"FAILED\n    {r.stderr[:200]}")

    print("\n=== ALL DONE ===")


if __name__ == "__main__":
    main()
