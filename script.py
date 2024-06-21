 
#!/usr/bin/env python3



import subprocess

svc = "sshd"

check_cmd = ["ps",
             "-c",
	     svc]

service_check = subprocess.call(check_cmd)

if service_check == 0:
    print("The service is running.")
else:
    print("The service is NOT running.")
    print("Starting it...")
    try:
        subprocess.call(["systemctl", "start", "sshdd"])
    except:
    print("There was an error starting the process.")
    exit(1)
    subprocess.call(check_cmd)
