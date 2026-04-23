"""Check generation log on cluster."""
import paramiko, sys

c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect("ada.iiit.ac.in", username="shubhamcvit", password="0410@Shubham", timeout=30)

# Find log and tail it
cmd = """ssh gnode047 'LOG=$(ls -t /ssd_scratch/shubhamcvit/btp/batch_gen_*.log 2>/dev/null | head -1); if [ -n "$LOG" ]; then echo "=== LOG: $LOG ==="; echo ""; grep -c ">>> Done:" "$LOG" 2>/dev/null; echo " chapters done"; echo ""; tail -30 "$LOG"; else echo "No log found"; fi'"""
_, o, e = c.exec_command(cmd, timeout=60)
out = o.read().decode()
err = e.read().decode()
print(out)
if err and "torch_dtype" not in err:
    print("STDERR:", err[:200])
c.close()
