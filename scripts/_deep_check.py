"""Deep status check - process, nohup output, and timestamps."""
import paramiko

c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('ada.iiit.ac.in', username='shubhamcvit', password='0410@Shubham')

# Check all python processes on gnode047
_, o, _ = c.exec_command('ssh gnode047 "ps aux | grep python | grep -v grep"')
print("=== Python processes on gnode047 ===")
print(o.read().decode())

# Check nohup.out
_, o, _ = c.exec_command('ssh gnode047 "ls -la /ssd_scratch/shubhamcvit/btp/nohup.out 2>/dev/null; tail -5 /ssd_scratch/shubhamcvit/btp/nohup.out 2>/dev/null"')
print("=== nohup.out ===")
print(o.read().decode())

# Check log file timestamp
_, o, _ = c.exec_command('ssh gnode047 "stat /ssd_scratch/shubhamcvit/btp/batch_gen_20260414_154607.log | grep Modify"')
print("=== Log last modified ===")
print(o.read().decode())

# Check current time  
_, o, _ = c.exec_command('ssh gnode047 "date"')
print("=== Current time ===")
print(o.read().decode())

# Check GPU usage
_, o, _ = c.exec_command('ssh gnode047 "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader"')
print("=== GPU usage ===")
print(o.read().decode())

c.close()
