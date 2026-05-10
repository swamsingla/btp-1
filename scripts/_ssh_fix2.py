"""
Kill, fix 3 prompt bugs + batch_size, clear bad checkpoints, restart
"""
import paramiko, time

JUMP_HOST = "ada.iiit.ac.in"; USER = "shubhamcvit"; PW = "0410@Shubham"
INNER = "gnode048"; BASE = "/ssd_scratch/btp-1"

def run(c, cmd, t=30):
    s = c.get_transport().open_session()
    s.exec_command(cmd)
    o = b""
    dl = time.time() + t
    while time.time() < dl:
        if s.recv_ready(): o += s.recv(65536)
        if s.exit_status_ready():
            while s.recv_ready(): o += s.recv(65536)
            break
        time.sleep(0.05)
    return o.decode(errors="replace")

def connect():
    jump = paramiko.SSHClient(); jump.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    jump.connect(JUMP_HOST, username=USER, password=PW, look_for_keys=False, allow_agent=False, timeout=15)
    ch = jump.get_transport().open_channel("direct-tcpip", (INNER, 22), ("127.0.0.1", 0))
    inner = paramiko.SSHClient(); inner.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    inner.connect(INNER, username=USER, password=PW, sock=ch, look_for_keys=False, allow_agent=False, timeout=15)
    return jump, inner

jump, inner = connect()
print("Connected")

# Step 1: Kill
print("\n--- Kill process ---")
print(run(inner, "kill $(pgrep -f 'graph_builder.py') 2>/dev/null; echo killed"))
time.sleep(3)
print("Running after kill:", run(inner, "ps aux | grep graph_builder | grep -v grep | wc -l").strip())

# Step 2: Patch graph_builder.py on remote
print("\n--- Patching graph_builder.py ---")
patch = r'''
path = '/ssd_scratch/btp-1/scripts/graph_builder.py'
with open(path) as f:
    src = f.read()

changes = []

# Fix 1: System prompt - grades should come from input only, not 6-12
old1 = '4. Assign grades: the list of grade levels (6-12) where this concept is taught.'
new1 = '4. Assign grades: ONLY the grades that appear in the input (e.g., if input says "(grade 6)", use [6]). Do NOT invent or extend grades beyond the input.'
if old1 in src:
    src = src.replace(old1, new1, 1)
    changes.append('Fixed system prompt grade instruction')
else:
    changes.append('WARN: grade instruction not found - check manually')

# Fix 2: User prompt - wrong grade range + add subject guard
old2 = '''        user_prompt = f"""Subject: {subject.title()}
Grade range of these topics: 6\\u201312

Raw topics (from NCERT + ICSE + state boards):
{batch_str}

Extract the canonical concept hierarchy for these topics.
Each raw topic may produce 1 high-level concept OR multiple sub-concepts.
IMPORTANT: Populate the "slug" field using lowercase-hyphenated form of canonical_name.
Return JSON array only."""'''

new2 = '''        available_grades = sorted(grade_topics.keys())
        user_prompt = f"""Subject: {subject.title()} ONLY
Grades present in this dataset: {available_grades} (ONLY these grades - do NOT add others)

Raw topics (from NCERT + ICSE + state boards):
{batch_str}

STRICT RULES:
1. Only extract {subject.title()} concepts. If a topic belongs to another subject (e.g., meteorology in a maths list), SKIP it.
2. grades[] must contain ONLY values from {available_grades}. Do NOT add grade 10, 11, 12, etc.
3. Populate "slug" using lowercase-hyphenated canonical_name.
4. Be concise - output compact JSON only, no prose.
Return JSON array only."""'''

if old2.replace('\\u2013', '\u2013') in src:
    src = src.replace(old2.replace('\\u2013', '\u2013'), new2, 1)
    changes.append('Fixed user prompt (grade range + subject guard)')
else:
    # Try simpler find
    marker = 'Grade range of these topics: 6'
    if marker in src:
        # Find the full f-string block
        start = src.index('        user_prompt = f"""Subject: {subject.title()}')
        end = src.index('Return JSON array only."""', start) + len('Return JSON array only."""')
        old_block = src[start:end]
        new_block = '''        available_grades = sorted(grade_topics.keys())
        user_prompt = f"""Subject: {subject.title()} ONLY
Grades present in this dataset: {available_grades} (ONLY these grades - do NOT add others)

Raw topics (from NCERT + ICSE + state boards):
{batch_str}

STRICT RULES:
1. Only extract {subject.title()} concepts. If a topic belongs to another subject, SKIP it.
2. grades[] must contain ONLY values from {available_grades}. Do NOT add grade 10, 11, 12 etc.
3. Populate "slug" using lowercase-hyphenated canonical_name.
4. Be concise - output compact JSON, no prose.
Return JSON array only."""'''
        src = src[:start] + new_block + src[end:]
        changes.append('Fixed user prompt via block replacement')
    else:
        changes.append('WARN: user_prompt block not found')

# Fix 3: batch_size 5 -> 3
old3 = 'batch_size: int = 5,'
new3 = 'batch_size: int = 3,'
if old3 in src:
    src = src.replace(old3, new3, 1)
    changes.append('batch_size 5->3')
else:
    changes.append('WARN: batch_size=5 not found')

with open(path, 'w') as f:
    f.write(src)

print('Changes:')
for c in changes:
    print(' -', c)
'''

cmd = "python3 << 'PYEOF'\n" + patch + "\nPYEOF"
print(run(inner, cmd, t=20))

# Verify patch
print("\n--- Verify patch ---")
print(run(inner, "grep -n 'batch_size\\|Grade range\\|ONLY these grades\\|STRICT RULES\\|Do NOT invent' " + BASE + "/scripts/graph_builder.py"))

# Step 3: Clear bad concept checkpoints
print("\n--- Clear bad maths concept checkpoints ---")
print(run(inner, "rm -f " + BASE + "/data/knowledge_graph/.checkpoints/maths_concepts_batch*.json && echo cleared"))
print(run(inner, "rm -f " + BASE + "/data/knowledge_graph/.checkpoints/maths_edges_grade*.json && echo cleared edges"))
print("Remaining:", run(inner, "ls " + BASE + "/data/knowledge_graph/.checkpoints/ 2>/dev/null"))

# Step 4: Restart
print("\n--- Restart ---")
restart = (
    "cd " + BASE + " && "
    "export LLAMA_MODEL_PATH=/ssd_scratch/models/llama-8b && "
    "nohup python3 scripts/graph_builder.py --subject maths --no-skip-existing "
    "> " + BASE + "/logs/stage2_maths_v3.log 2>&1 & echo $!"
)
pid = run(inner, restart, t=10).strip()
print("PID:", pid)
time.sleep(8)
print("Running:", run(inner, "ps aux | grep graph_builder | grep -v grep | awk '{print $2,$3}'").strip())

inner.close(); jump.close()
print("\nDone. Monitor log: stage2_maths_v3.log")
