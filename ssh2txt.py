#pip install paramiko
import paramiko
import time
from datetime import datetime
print('device ip (102.33.54.252):')
ip = input()
print('device port (22):')
port = input()
print('device admin (root):')
admin = input()
print('device password (#secure2!):')
password = input()
print('command to run (show job -c):')
command = input()
print('time intervall? (seconds):')
intervall = input()
print('name of output file and file-extension? (ssh.txt):')
filename = input()


while True:
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, admin, password, look_for_keys=False )
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
    output = ssh_stdout.readlines()
    ssh.close()
    with open(filename, 'a') as f:
        for i in output:
            f.write("%s\n" % i)
    now = datetime.now()
    now = now.strftime("%H:%M:%S")
    print('last run: ', now)
    time.sleep(int(intervall))
    