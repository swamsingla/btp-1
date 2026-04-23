"""Check what output dirs exist and restart remaining chapters."""
import paramiko

c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('ada.iiit.ac.in', username='shubhamcvit', password='0410@Shubham')

# Check all output dirs
_, o, _ = c.exec_command('ssh gnode047 "find /ssd_scratch/shubhamcvit/btp/output -maxdepth 3 -type d | sort"')
print("=== Output directories ===")
print(o.read().decode())

# Check which chapters have _index.json (means fully complete)
_, o, _ = c.exec_command('ssh gnode047 "find /ssd_scratch/shubhamcvit/btp/output -name _index.json | sort"')
print("=== Completed chapters (_index.json) ===")
print(o.read().decode())

# Count .md files per chapter
_, o, _ = c.exec_command('ssh gnode047 "for d in $(find /ssd_scratch/shubhamcvit/btp/output -maxdepth 3 -mindepth 3 -type d | sort); do echo \"$d: $(ls $d/*.md 2>/dev/null | wc -l) md files\"; done"')
print("=== .md files per chapter ===")
print(o.read().decode())

c.close()
