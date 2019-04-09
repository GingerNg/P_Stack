# coding:utf8
# author:ginger

# http://www.cnblogs.com/kaituorensheng/p/4465768.html

print ("进程池")
# 进程池
from multiprocessing import Pool
import os, time, random
import sys, traceback

def wrapper(name,func,context):
    try:
        func(name)
    except BaseException:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        stacktrace = traceback.format_exception(exc_type, exc_value, exc_traceback)
        context[name] = stacktrace
    else:
        context[name] = "success"
    return context


def long_time_task(name):
    print ('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print ('Task %s runs %0.2f seconds.' % (name, (end - start)))

def wrong_func(name):
    print ('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    try:
        1/0
    except Exception:
        # print e
        raise RuntimeError
    end = time.time()
    print ('Task %s runs %0.2f seconds.' % (name, (end - start)))



def __callback(self, context):   # 回调函数
    try:
        self.__doneQueue.put(context)
    finally:
        self.__increaseIdleCounter()


if __name__=='__main__':
    print ('Parent process %s.' % os.getpid())
    p = Pool()  # Pool的默认大小是CPU的核数
    for i in range(3):
        p.apply_async(long_time_task, args=(i,))
    # 主进程和线程池 并发运行
    print ('Waiting for all subprocesses done...')
    # p.apply_async(long_time_task, args=(5,))

    applyResult = p.apply_async(wrong_func, args=(7,))

    context = {}
    context = p.apply_async(wrapper,args=('wrong',wrong_func,context))   # 不起作用

    context_long = {}
    context_long = p.apply_async(wrapper,args=('long',long_time_task,context_long))

    p.apply_async(long_time_task, args=(5,))

    # print result.successful()

    p.close() # 调用该方法之后，不能继续添加新的process
    p.join() # 等待子进程结束后，再运行下方的代码
    print ('All subprocesses done.')
    print (context.get())
    print (context_long.get())
    # print (applyResult.get())  # RuntimeError
