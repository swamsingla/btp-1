"""Check generation status on gnode047."""
import paramiko

SCRATCH = "/ssd_scratch/shubhamcvit/btp"

c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('ada.iiit.ac.in', username='shubhamcvit', password='0410@Shubham')

def run_ada(cmd):
    _, o, e = c.exec_command(cmd)
    return o.read().decode().strip(), e.read().decode().strip()

def run(cmd):
    out, err = run_ada(f'ssh gnode047 "{cmd}"')
    return out

# Check node reachability
out, err = run_ada("ssh -o ConnectTimeout=5 gnode047 'echo OK' 2>&1")
print(f"gnode047 reachable: {out}")

# List ALL output dirs and .md counts
print("\n=== All chapter outputs ===")
out = run(f"find {SCRATCH}/output -name '*.md' | sort")
for line in sorted(out.split("\n")):
    if line.strip():
        print(f"  {line.strip()}")

# Check _index.json presence (marks completion)
print("\n=== _index.json status ===")
out = run(f"find {SCRATCH}/output -name '_index.json' | sort")
for line in sorted(out.split("\n")):
    if line.strip():
        print(f"  {line.strip()}")

# Summary per chapter
print("\n=== Summary ===")
for grade in range(6, 13):
    for ch in range(1, 4):
        path = f"{SCRATCH}/output/grade{grade}/maths/chapter{ch}"
        md_count = run(f"ls {path}/*.md 2>/dev/null | wc -l")
        has_idx = run(f"test -f {path}/_index.json && echo YES || echo NO")
        if md_count != "0" or has_idx == "YES":
            print(f"  grade{grade}/ch{ch}: {md_count} .md files | _index.json: {has_idx}")

c.close()
