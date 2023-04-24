
import time
import os
import platform
import subprocess
import select

# var
filename = "/home/sheliak/Labz/my-papers/poc-c2/ping.pong/stream.txt"

'''
last_status_t = int(time.time())
val = True

while val:
    file_status = os.stat("./stream.txt")
    file_status_t = file_status.st_ctime
    if file_status_t > last_status_t:
        print("file change")
        last_status_t = file_status_t
    else:
        print(file_status.st_ctime, last_status_t)
'''

tailprocess = subprocess.Popen(["tail", "-f", filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

while True:
    line = tailprocess.stdout.readline().decode('utf-8')
    if line == '':
        time.sleep(5)
        print("...")
    print(line.rstrip())
