# coding:utf8
# author:ginger
# python---GIL锁，多线程只能用一个核心
import time, threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire()  #获取锁 对全局变量加锁
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
# 抢占式运行
t1.start()
t2.start()
t1.join()
t2.join()
print balance