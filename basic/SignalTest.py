# coding=utf-8

import os
import signal
from time import sleep



# http://www.jb51.net/article/74844.htm


def sigHandler(signum, frame):
    print ("stop")
    exit()

# kill -l

# 10 ：  SIGUSR1 用户自定义信号 进程终止

if __name__ == "__main__":
    # register signal.SIGALRM's handler
    signal.signal(signal.SIGALRM, sigHandler)
    signal.alarm(20)  # signal.alarm()执行20秒之后，进程将向自己发出SIGALRM信号
    while 1:
        print ('我的进程id是', os.getpid())

        sleep(10)


