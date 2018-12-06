# coding:utf8
# author:ginger

import os

"""
print 'Process (%s) start...' % os.getpid()
pid = os.fork() # 创建子进程
if pid==0:
    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

"""



from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，
    # 用start()方法启动，这样创建进程比fork()还要简单。
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    p.join() # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print 'Process end.'

