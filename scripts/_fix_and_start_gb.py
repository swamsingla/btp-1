"""
1. Kill any stray topic_ingestion processes
2. Check all grade file statuses
3. Inject hardcoded standard topics for any grade with 0/missing topics
4. Start graph_builder for maths
"""
import paramiko, time, os, json

JUMP_HOST = "ada.iiit.ac.in"; USER = "shubhamcvit"; PW = "0410@Shubham"
INNER_HOST = "gnode048"; BASE = "/ssd_scratch/btp-1"
SCRIPTS = os.path.dirname(os.path.abspath(__file__))

# ── Hardcoded fallback topics (CBSE/NCERT standard syllabus) ──────────────────
HARDCODED = {
    7: {
        "grade": 7, "subject": "maths",
        "topics": [
            {"raw_name": "Integers", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Properties of Integers", "Addition and Subtraction of Integers", "Multiplication of Integers", "Division of Integers"]},
            {"raw_name": "Fractions and Decimals", "source_boards": ["NCERT", "CBSE"], "note": "", "subtopics": ["Multiplication of Fractions", "Division of Fractions", "Multiplication of Decimals", "Division of Decimals"]},
            {"raw_name": "Data Handling", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Collection and Organisation of Data", "Mean", "Median", "Mode", "Bar Graphs", "Probability"]},
            {"raw_name": "Simple Equations", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Setting Up an Equation", "Solving an Equation", "Applications"]},
            {"raw_name": "Lines and Angles", "source_boards": ["NCERT", "CBSE"], "note": "", "subtopics": ["Related Angles", "Pairs of Lines", "Checking for Parallel Lines"]},
            {"raw_name": "The Triangle and its Properties", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Medians", "Altitudes", "Angle Sum Property", "Exterior Angle", "Pythagoras Property"]},
            {"raw_name": "Congruence of Triangles", "source_boards": ["NCERT", "CBSE"], "note": "", "subtopics": ["Congruence Criteria", "SSS", "SAS", "ASA", "RHS"]},
            {"raw_name": "Comparing Quantities", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Equivalent Ratios", "Percentage", "Profit and Loss", "Simple Interest"]},
            {"raw_name": "Rational Numbers", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["What are Rational Numbers", "Positive and Negative Rational Numbers", "Rational Numbers on Number Line", "Standard Form"]},
            {"raw_name": "Practical Geometry", "source_boards": ["NCERT", "CBSE"], "note": "", "subtopics": ["Construction of a Line Parallel to a Given Line", "Construction of Triangles"]},
            {"raw_name": "Perimeter and Area", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Squares and Rectangles", "Area of Triangle", "Area of Parallelogram", "Circles", "Conversion of Units"]},
            {"raw_name": "Algebraic Expressions", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Terms of an Expression", "Like and Unlike Terms", "Monomial Binomial Polynomial", "Addition and Subtraction", "Finding the Value"]},
            {"raw_name": "Exponents and Powers", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Exponents", "Laws of Exponents", "Standard Form of Large Numbers"]},
            {"raw_name": "Symmetry", "source_boards": ["NCERT", "CBSE"], "note": "", "subtopics": ["Lines of Symmetry", "Rotational Symmetry", "Line Symmetry and Rotational Symmetry"]},
            {"raw_name": "Visualising Solid Shapes", "source_boards": ["NCERT", "CBSE"], "note": "", "subtopics": ["Plane Figures and Solid Shapes", "Faces Edges Vertices", "Nets for Building 3D Shapes", "Drawing Solids on Flat Surface"]},
        ]
    },
    12: {
        "grade": 12, "subject": "maths",
        "topics": [
            {"raw_name": "Relations and Functions", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Types of Relations", "Types of Functions", "Composition of Functions", "Invertible Functions", "Binary Operations"]},
            {"raw_name": "Inverse Trigonometric Functions", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Basic Concepts", "Properties of Inverse Trigonometric Functions"]},
            {"raw_name": "Matrices", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Matrix Notation and Order", "Types of Matrices", "Operations on Matrices", "Transpose", "Symmetric and Skew Symmetric Matrices", "Elementary Operations"]},
            {"raw_name": "Determinants", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Expansion of Determinants", "Properties of Determinants", "Adjoint and Inverse of Matrix", "Applications: Solving System of Equations"]},
            {"raw_name": "Continuity and Differentiability", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Continuity", "Differentiability", "Chain Rule", "Derivatives of Implicit Functions", "Exponential and Logarithmic Functions", "Logarithmic Differentiation", "Mean Value Theorem"]},
            {"raw_name": "Application of Derivatives", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Rate of Change", "Increasing and Decreasing Functions", "Tangents and Normals", "Approximations", "Maxima and Minima"]},
            {"raw_name": "Integrals", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Integration as Inverse of Differentiation", "Methods of Integration", "Definite Integrals", "Fundamental Theorem of Calculus"]},
            {"raw_name": "Application of Integrals", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Area Under Simple Curves", "Area Between Two Curves"]},
            {"raw_name": "Differential Equations", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Basic Concepts", "General and Particular Solutions", "Formation of Differential Equations", "Methods of Solving First Order First Degree"]},
            {"raw_name": "Vector Algebra", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Basic Concepts", "Types of Vectors", "Addition of Vectors", "Scalar Product", "Vector Product"]},
            {"raw_name": "Three Dimensional Geometry", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Direction Cosines and Ratios", "Equation of a Line", "Angle Between Lines", "Shortest Distance", "Equation of a Plane"]},
            {"raw_name": "Linear Programming", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Introduction to Linear Programming", "Graphical Method of Solution", "Different Types of Problems"]},
            {"raw_name": "Probability", "source_boards": ["NCERT", "CBSE", "ICSE"], "note": "", "subtopics": ["Conditional Probability", "Multiplication Theorem", "Independent Events", "Bayes Theorem", "Random Variables and Probability Distribution", "Bernoulli Trials and Binomial Distribution"]},
        ]
    }
}

def run(c, cmd, t=45):
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
    ch = jump.get_transport().open_channel("direct-tcpip", (INNER_HOST, 22), ("127.0.0.1", 0))
    inner = paramiko.SSHClient(); inner.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    inner.connect(INNER_HOST, username=USER, password=PW, sock=ch, look_for_keys=False, allow_agent=False, timeout=15)
    return jump, inner

def upload_text(inner, content, remote_path):
    sftp = inner.open_sftp()
    with sftp.open(remote_path, 'w') as f:
        f.write(content)
    sftp.close()

def upload_file(inner, local, remote):
    sftp = inner.open_sftp(); sftp.put(local, remote); sftp.close()

def get_topic_count(inner, grade):
    f = f"{BASE}/data/intermediate/raw_topics/grade{grade}_maths.json"
    out = run(inner, f"[ -f {f} ] && python3 -c \"import json; d=json.load(open('{f}')); print(len(d.get('topics',[])))\" 2>/dev/null || echo MISSING").strip()
    try:
        return int(out)
    except ValueError:
        return -1

jump, inner = connect()

# 1. Kill any stray topic_ingestion or re-run processes
print("Killing stray processes...")
print(run(inner, "pkill -f 'topic_ingestion' 2>/dev/null; echo killed"))

time.sleep(2)

# 2. Check status
print("\n=== Grade file status ===")
grades_status = {}
for g in [6, 7, 8, 9, 10, 11, 12]:
    n = get_topic_count(inner, g)
    grades_status[g] = n
    mark = "✓" if n > 0 else ("MISSING" if n < 0 else "EMPTY")
    print(f"  grade{g}: {n if n >= 0 else '---'} topics  [{mark}]")

# 3. Inject hardcoded topics for any grade with 0 or missing topics
bad_grades = [g for g, n in grades_status.items() if n <= 0]
if bad_grades:
    print(f"\nBad grades: {bad_grades}")
    for g in bad_grades:
        if g in HARDCODED:
            payload = json.dumps(HARDCODED[g], indent=2)
            remote_path = f"{BASE}/data/intermediate/raw_topics/grade{g}_maths.json"
            upload_text(inner, payload, remote_path)
            n = len(HARDCODED[g]["topics"])
            print(f"  Injected {n} hardcoded topics for grade {g} → {remote_path}")
        else:
            print(f"  WARNING: grade {g} is bad and has no hardcoded fallback!")
else:
    print("\nAll grades OK — no injection needed.")

# 4. Re-check
print("\n=== Post-injection status ===")
all_ok = True
for g in [6, 7, 8, 9, 10, 11, 12]:
    n = get_topic_count(inner, g)
    mark = "✓" if n > 0 else "PROBLEM"
    print(f"  grade{g}: {n if n >= 0 else 'MISSING'} topics  [{mark}]")
    if n <= 0:
        all_ok = False

if not all_ok:
    print("\nERROR: Some grades still have no topics. Check manually before proceeding.")
    inner.close(); jump.close()
    exit(1)

# 5. Clear old graph_builder checkpoints
print("\nClearing old concept/edge checkpoints...")
print(run(inner, f"rm -f {BASE}/data/intermediate/concept_ckpt_*.jsonl {BASE}/data/intermediate/edge_ckpt_*.jsonl && echo done"))

# 6. Upload latest graph_builder
print("Uploading graph_builder.py...")
upload_file(inner, os.path.join(SCRIPTS, "graph_builder.py"), BASE + "/scripts/graph_builder.py")
print("Uploaded ✓")

# 7. Start graph builder
print("\nStarting graph_builder (Stage 2)...")
cmd = (
    f"cd {BASE} && "
    "export LLAMA_MODEL_PATH=/ssd_scratch/models/llama-8b && "
    f"nohup python3 scripts/graph_builder.py --subject maths --no-skip-existing "
    f"> {BASE}/logs/stage2_maths_v3.log 2>&1 & echo $!"
)
gb_pid = run(inner, cmd, t=10).strip()
print(f"graph_builder PID: {gb_pid}")

time.sleep(10)
gb_running = run(inner, "ps aux | grep graph_builder | grep -v grep | awk '{print $2,$3,$11,$12}'").strip()
print(f"Confirmed running: {gb_running}")

log_start = run(inner, f"tail -8 {BASE}/logs/stage2_maths_v3.log 2>/dev/null").strip()
print(f"\nStage 2 log start:\n{log_start}")

inner.close(); jump.close()
print("\nAll done. Monitor with _chk.py")
