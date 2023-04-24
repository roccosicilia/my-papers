
import time
import os
import platform
import subprocess
import select

# var
file = "/home/sheliak/Labz/my-papers/poc-c2/ping.pong/stream.txt"

'''
# Test 1
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

# Test 2
tailprocess = subprocess.Popen(["tail", "-f", filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

while True:
    line = tailprocess.stdout.readline().decode('utf-8')
    if line == '':
        time.sleep(5)
        print("...")
    print(line.rstrip())

# Test 3
tailp = os.popen("tail -f {}".format(file))     # tail

output = select.poll()                          # read tail output
output.register(tailp.fileno(), select.POLLIN)  # read tail output

while True:
    if output.poll(1000):
        line = tailp.readline().strip()
        if line:
            print(line)
    else:
        print("...")
'''

def mytail(file):
    file.seek(0, os.SEEK_END)
    while True:
        # read last line of file
        line = file.readline()
        # sleep if file hasn't been updated
        if not line:
            time.sleep(500)
            continue
        yield line

if __name__ == '__main__':
    
    logfile = open(file,"r")
    loglines = mytail(logfile)
    # iterate over the generator
    for line in loglines:
        print(line)
        
