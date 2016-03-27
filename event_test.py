import fcntl
import time, os
import sys


fd = sys.stdin.fileno()
fl = fcntl.fcntl(fd,fcntl.F_GETFL)
fcntl.fcntl(fd,fcntl.F_SETFL, fl | os.O_NONBLOCK)



while True:
    try:
        ins = sys.stdin.readline()
        print("ff"+str(ins)+"gg")
        time.sleep(1)
    finally:
        pass
