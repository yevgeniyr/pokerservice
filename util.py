import os

def still_running(pid):
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True

def log_pid(pid,pid_file):
    with open(pid_file,'w') as pid_file:
        pid_file.write(str(pid))

def get_pid_from_file(pid_file):
    pid = open(pid_file).read()
    if pid:
        return int(pid)
    else:
        return None



