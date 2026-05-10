"""
Fix and restart graph_builder:
1. Kill current broken process
2. Patch graph_builder.py: batch_size 20->5, max_new_tokens 2500->4096
3. Clear bad maths concept checkpoints (keep edge ones just in case)
4. Restart with nohup
"""
import paramiko, time

JUMP_HOST = "ada.iiit.ac.in"; JUMP_USER = "shubhamcvit"; PASSWORD = "0410@Shubham"
INNER_HOST = "gnode048"; BASE_PATH = "/ssd_scratch/btp-1"

def run(client, cmd, timeout=30):
    s = client.get_transport().open_session()
    s.exec_command(cmd)
    out, err = b"", b""
    dl = time.time() + timeout
    while time.time() < dl:
        if s.recv_ready(): out += s.recv(65536)
        if s.recv_stderr_ready(): err += s.recv_stderr(65536)
        if s.exit_status_ready():
            while s.recv_ready(): out += s.recv(65536)
            while s.recv_stderr_ready(): err += s.recv_stderr(65536)
            break
        time.sleep(0.1)
    return out.decode(errors="replace"), err.decode(errors="replace")

def make_client(hostname, username, password, sock=None):
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    kw = dict(hostname=hostname, username=username, password=password,
              look_for_keys=False, allow_agent=False, timeout=20)
    if sock: kw["sock"] = sock
    c.connect(**kw)
    return c

jump = make_client(JUMP_HOST, JUMP_USER, PASSWORD)
ch = jump.get_transport().open_channel("direct-tcpip", (INNER_HOST, 22), ("127.0.0.1", 0))
inner = make_client(INNER_HOST, JUMP_USER, PASSWORD, sock=ch)
print("Connected to gnode048\n")

# Step 1: Kill current process
print("="*60)
print("STEP 1: Kill current broken process")
print("="*60)
o, e = run(inner, "kill $(pgrep -f 'graph_builder.py') 2>/dev/null; echo 'killed'")
print(o)
time.sleep(3)
o, e = run(inner, "ps aux | grep graph_builder | grep -v grep")
print("Remaining:", o if o.strip() else "None - killed successfully ✓")

# Step 2: Clear bad maths concept checkpoints (they only have 1 concept each)
print("\n" + "="*60)
print("STEP 2: Clear bad concept checkpoints")
print("="*60)
o, e = run(inner, f"rm -f {BASE_PATH}/data/knowledge_graph/.checkpoints/maths_concepts_batch*.json && echo 'cleared maths concept checkpoints'")
print(o)
# Also clear edge checkpoints since they were built on bad concepts
o, e = run(inner, f"rm -f {BASE_PATH}/data/knowledge_graph/.checkpoints/maths_edges_grade*.json && echo 'cleared maths edge checkpoints'")
print(o)
# Show what remains
o, e = run(inner, f"ls -la {BASE_PATH}/data/knowledge_graph/.checkpoints/")
print("Remaining checkpoints:", o)

# Step 3: Patch graph_builder.py
print("\n" + "="*60)
print("STEP 3: Patch graph_builder.py")
print("="*60)

# Use Python to do the patches safely
patch_script = r"""
import re

path = '/ssd_scratch/btp-1/scripts/graph_builder.py'
with open(path, 'r') as f:
    content = f.read()

changes = []

# Fix 1: batch_size default 20 -> 5 in extract_canonical_concepts signature
old = 'batch_size: int = 20,'
new = 'batch_size: int = 5,'
if old in content:
    content = content.replace(old, new, 1)
    changes.append('batch_size 20->5 in extract_canonical_concepts')
else:
    changes.append('WARNING: batch_size=20 not found in extract_canonical_concepts')

# Fix 2: max_new_tokens 2500 -> 4096 in the llm_call for concept extraction
old = 'raw_resp = llm_call(system=SYSTEM_HIERARCHY, user=user_prompt, max_new_tokens=2500)'
new = 'raw_resp = llm_call(system=SYSTEM_HIERARCHY, user=user_prompt, max_new_tokens=4096)'
if old in content:
    content = content.replace(old, new, 1)
    changes.append('max_new_tokens 2500->4096 in concept extraction call')
else:
    changes.append('WARNING: max_new_tokens=2500 call not found')

# Fix 3: Also increase edge extraction token limit for completeness
old = 'raw_resp = llm_call(system=SYSTEM_PREREQS, user=user_prompt, max_new_tokens=4000)'
new = 'raw_resp = llm_call(system=SYSTEM_PREREQS, user=user_prompt, max_new_tokens=4096)'
if old in content:
    content = content.replace(old, new, 1)
    changes.append('edge extraction max_new_tokens normalized to 4096')

with open(path, 'w') as f:
    f.write(content)

print('Patches applied:')
for c in changes:
    print(' -', c)

# Verify
with open(path, 'r') as f:
    verify = f.read()
print('batch_size=5 present:', 'batch_size: int = 5,' in verify)
print('max_new_tokens=4096 (concept):', 'max_new_tokens=4096' in verify)
"""

o, e = run(inner, f"python3 -c \"{patch_script.replace(chr(34), chr(39))}\" 2>&1", timeout=15)
# Use heredoc approach instead to avoid quoting issues
patch_cmd = f"""python3 << 'PYEOF'
{patch_script}
PYEOF"""
o, e = run(inner, patch_cmd, timeout=15)
print(o, e)

# Verify the patch
print("\nVerifying patch in graph_builder.py:")
o, e = run(inner, f"grep -n 'batch_size\|max_new_tokens' {BASE_PATH}/scripts/graph_builder.py")
print(o)

# Step 4: Restart with nohup
print("\n" + "="*60)
print("STEP 4: Restart graph_builder")
print("="*60)
restart_cmd = (
    f"cd {BASE_PATH} && "
    f"export LLAMA_MODEL_PATH=/ssd_scratch/models/llama-8b && "
    f"nohup python3 scripts/graph_builder.py --subject maths --no-skip-existing "
    f"> {BASE_PATH}/logs/stage2_maths_v2.log 2>&1 & echo $!"
)
o, e = run(inner, restart_cmd, timeout=10)
pid = o.strip()
print(f"Started with PID: {pid}")

time.sleep(5)

# Verify it's running
o, e = run(inner, "ps aux | grep graph_builder | grep -v grep")
print("Process status:", o if o.strip() else "NOT FOUND - failed to start")

# Show first few lines of new log after a moment
time.sleep(10)
o, e = run(inner, f"cat {BASE_PATH}/logs/stage2_maths_v2.log 2>/dev/null || echo 'log empty'")
print("\nNew log start:\n", o[:2000])

inner.close(); jump.close()
print("\nDone. Monitor with _ssh_monitor_v2.py")
