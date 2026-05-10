import paramiko, time

def run(c, cmd, t=15):
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

jump = paramiko.SSHClient(); jump.set_missing_host_key_policy(paramiko.AutoAddPolicy())
jump.connect("ada.iiit.ac.in", username="shubhamcvit", password="0410@Shubham", look_for_keys=False, allow_agent=False)
ch = jump.get_transport().open_channel("direct-tcpip", ("gnode048", 22), ("127.0.0.1", 0))
inner = paramiko.SSHClient(); inner.set_missing_host_key_policy(paramiko.AutoAddPolicy())
inner.connect("gnode048", username="shubhamcvit", password="0410@Shubham", sock=ch, look_for_keys=False, allow_agent=False)

print("Kill graph_builder:", run(inner, "kill 7527 7526 2>/dev/null; echo ok"))
time.sleep(2)
print("Clear bad ckpts:", run(inner, "rm -f /ssd_scratch/btp-1/data/knowledge_graph/.checkpoints/maths_concepts_batch*.json && echo cleared"))
print("Remaining ckpts:", run(inner, "ls /ssd_scratch/btp-1/data/knowledge_graph/.checkpoints/ | grep maths || echo none"))
print("Processes now:", run(inner, "ps aux | grep python3 | grep -v grep | awk '{print $2,$11,$12}'"))
inner.close(); jump.close()
