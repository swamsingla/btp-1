import paramiko, json

j = paramiko.SSHClient(); j.set_missing_host_key_policy(paramiko.AutoAddPolicy())
j.connect('ada.iiit.ac.in', username='shubhamcvit', password='0410@Shubham')
t = j.get_transport().open_channel('direct-tcpip', ('gnode048', 22), ('localhost', 0))
inner = paramiko.SSHClient(); inner.set_missing_host_key_policy(paramiko.AutoAddPolicy())
inner.connect('gnode048', username='shubhamcvit', password='0410@Shubham', sock=t)

def run(cmd, timeout=30):
    _, o, e = inner.exec_command(cmd, timeout=timeout)
    return o.read().decode().strip()

print('=== PROCESSES ===')
print('graph_builder:', run('pgrep -a -f graph_builder 2>/dev/null || echo none'))
print('python3:', run('pgrep -a -f python3 2>/dev/null | grep -v pgrep || echo none'))

print('\n=== rebuild_edges_v2.log (last 40 lines) ===')
print(run('tail -40 /ssd_scratch/btp-1/logs/rebuild_edges_v2.log'))

print('\n=== edge checkpoints ===')
print(run('for f in /ssd_scratch/btp-1/data/knowledge_graph/.checkpoints/maths_edges_grade*.json; do echo -n "$f: "; python3 -c "import json,sys; d=json.load(open(sys.argv[1])); print(len(d), chr(39)records chr(39))" "$f"; done'))

print('\n=== maths.json ===')
raw = run('cat /ssd_scratch/btp-1/data/knowledge_graph/graph_by_subject/maths.json 2>/dev/null')
if raw:
    d = json.loads(raw)
    print(f"concepts: {d['total_concepts']}  edges: {d['total_edges']}")
else:
    print('NOT_YET')

inner.close(); j.close()
