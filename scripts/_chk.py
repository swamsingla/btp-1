"""One-shot check: topic ingestion progress + concepts quality if graph running"""
import paramiko, time, json as _json

JUMP_HOST = "ada.iiit.ac.in"; USER = "shubhamcvit"; PW = "0410@Shubham"
INNER = "gnode048"; BASE = "/ssd_scratch/btp-1"

def run(c, cmd, t=20):
    s = c.get_transport().open_session(); s.exec_command(cmd)
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

# --- Processes ---
proc = run(inner, "ps aux | grep -E 'topic_ingestion|graph_builder' | grep -v grep | awk '{print $2,$3,$11,$12}'")
print("=" * 65)
print("RUNNING PROCESSES:", proc.strip() if proc.strip() else "NONE")

# --- Topic file status for maths ---
topic_check = """
import json, os
base = '/ssd_scratch/btp-1/data/intermediate/raw_topics'
for grade in range(6, 13):
    path = f'{base}/grade{grade}_maths.json'
    if os.path.exists(path):
        d = json.load(open(path))
        topics = d.get('topics', [])
        has_subs = sum(1 for t in topics if t.get('subtopics'))
        print(f'  grade{grade}_maths: {len(topics)} topics, {has_subs} with subtopics')
    else:
        print(f'  grade{grade}_maths: MISSING')
"""
cmd = "python3 << 'PYEOF'\n" + topic_check + "\nPYEOF"
print("\n--- MATHS TOPIC FILES ---")
print(run(inner, cmd, t=15))

# --- Topic ingestion log tail (try v2 first, fallback to v1)
print("--- TOPIC INGESTION LOG (last 30 lines) ---")
log1 = run(inner, "tail -30 " + BASE + "/logs/stage1_maths_v2.log 2>/dev/null || tail -30 " + BASE + "/logs/stage1_maths_missing.log 2>/dev/null || echo no log yet")
print(log1.strip())

# --- Graph builder log if running ---
gb_log = run(inner, "tail -20 " + BASE + "/logs/stage2_maths_v3.log 2>/dev/null || echo no graph log")
if "no graph log" not in gb_log:
    print("\n--- GRAPH BUILDER LOG (last 20) ---")
    print(gb_log.strip())

# --- Concept quality if checkpoints exist ---
ckpt_count = run(inner, "ls " + BASE + "/data/knowledge_graph/.checkpoints/maths_concepts_batch*.json 2>/dev/null | wc -l").strip()
if int(ckpt_count) > 0:
    print("\n--- CONCEPTS SO FAR (" + ckpt_count + " ckpt files) ---")
    concepts_raw = run(inner,
        "python3 -c \""
        "import json,glob; "
        "files=sorted(glob.glob('" + BASE + "/data/knowledge_graph/.checkpoints/maths_concepts_batch*.json')); "
        "all_c=[]; [all_c.extend(json.load(open(f))) for f in files]; "
        "print(json.dumps(all_c))"
        "\" 2>/dev/null", t=15)
    try:
        concepts = _json.loads(concepts_raw.strip())
        print(f"Total concepts: {len(concepts)}")
        for c in concepts:
            grades = c.get('grades', [])
            name = c.get('canonical_name', c.get('slug', '?'))
            domain = c.get('domain', '')
            print(f"  [{','.join(str(g) for g in grades)}] {name}" + (f" | {domain}" if domain else ""))
        no_grades = [c.get('canonical_name','?') for c in concepts if not c.get('grades')]
        bad_grades = [c.get('canonical_name','?') for c in concepts if any(g not in [6,7,8,9,10,11,12] for g in c.get('grades',[]))]
        print(f"\nQUALITY: missing grades={len(no_grades)}, bad grades={len(bad_grades)}")
        if bad_grades: print("  Bad:", bad_grades[:5])
    except Exception as ex:
        print("Parse error:", ex)

inner.close(); jump.close()

def run(c, cmd, t=20):
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

jump = paramiko.SSHClient(); jump.set_missing_host_key_policy(paramiko.AutoAddPolicy())
jump.connect(JUMP_HOST, username=USER, password=PW, look_for_keys=False, allow_agent=False, timeout=15)
ch = jump.get_transport().open_channel("direct-tcpip", (INNER, 22), ("127.0.0.1", 0))
inner = paramiko.SSHClient(); inner.set_missing_host_key_policy(paramiko.AutoAddPolicy())
inner.connect(INNER, username=USER, password=PW, sock=ch, look_for_keys=False, allow_agent=False, timeout=15)

proc = run(inner, "ps aux | grep graph_builder | grep -v grep | awk '{print $2,$3,$11,$12}'")
ckpt_c = run(inner, "ls " + BASE + "/data/knowledge_graph/.checkpoints/maths_concepts_batch*.json 2>/dev/null | wc -l").strip()
ckpt_e = run(inner, "ls " + BASE + "/data/knowledge_graph/.checkpoints/maths_edges_grade*.json 2>/dev/null | wc -l").strip()
log = run(inner, "tail -40 " + BASE + "/logs/stage2_maths_v2.log 2>/dev/null", t=15)
outfile = run(inner, "ls -lh " + BASE + "/data/knowledge_graph/graph_by_subject/maths.json 2>/dev/null || echo NOT_YET").strip()

# Read all concept checkpoints and aggregate concepts
concepts_json = run(inner,
    "python3 -c \""
    "import json, glob, sys; "
    "files = sorted(glob.glob('" + BASE + "/data/knowledge_graph/.checkpoints/maths_concepts_batch*.json')); "
    "all_c = []; "
    "[all_c.extend(json.load(open(f))) for f in files if json.load(open(f))]; "
    "print(json.dumps(all_c))"
    "\" 2>/dev/null", t=20)

inner.close(); jump.close()

import json as _json
print("=" * 65)
print("PROCESS :", proc.strip() if proc.strip() else "NOT RUNNING")
print("CKPT concepts:", ckpt_c, "  edges:", ckpt_e)
print("OUTPUT  :", outfile)

# Parse and show concepts
try:
    concepts = _json.loads(concepts_json.strip()) if concepts_json.strip() else []
    print("\n--- CONCEPTS GENERATED SO FAR (" + str(len(concepts)) + " total) ---")
    for c in concepts:
        name = c.get("canonical_name", c.get("slug", "?"))
        grades = c.get("grades", [])
        domain = c.get("domain", "")
        area = c.get("area", "")
        aliases = c.get("aliases", [])
        print("  [" + ",".join(str(g) for g in grades) + "] " + name +
              (" | " + domain if domain else "") +
              (" > " + area if area else "") +
              (" (aka: " + ", ".join(aliases[:2]) + ")" if aliases else ""))
    if len(concepts) == 0:
        print("  (none yet)")
    # Quality check
    no_grades = [c.get("canonical_name","?") for c in concepts if not c.get("grades")]
    no_slug = [c.get("canonical_name","?") for c in concepts if not c.get("slug")]
    print("\n--- QUALITY CHECK ---")
    print("  Missing grades field :", len(no_grades), no_grades[:5] if no_grades else "")
    print("  Missing slug field   :", len(no_slug), no_slug[:5] if no_slug else "")
    print("  Unique grade sets    :", sorted(set(tuple(sorted(c.get("grades",[]))) for c in concepts)))
except Exception as ex:
    print("Could not parse concepts:", ex, "| raw:", concepts_json[:300])

print("\n--- last 40 log lines ---")
print(log.strip())
