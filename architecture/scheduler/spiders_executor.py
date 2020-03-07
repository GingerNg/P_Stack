#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: spiders_executor.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-11-25 下午12:55
 @desc: 
"""
import Queue
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool
from multiprocessing import cpu_count
import threading
import sys, traceback,commands
import logging
from utils import file_util
import executor


def spider_wrapper(func,context):   # 直接导入包装函数
    try:
        func()
    except BaseException:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        stacktrace = traceback.format_exception(exc_type, exc_value, exc_traceback)
        context[func.__name__] = stacktrace
    else:
        context[func.__name__] = "success"
    return context

'''
py_path 脚本所在的位置
'''
def spider_shell(py_path,context):
    try:
        cmd = 'python '+py_path
        (status, output) = commands.getstatusoutput(cmd)
        # 失败
        if status != 0:
            raise RuntimeError(u"%s command execute error: %s" % (cmd, output))
    except BaseException:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        stacktrace = traceback.format_exception(exc_type, exc_value, exc_traceback)
        context[py_path] = stacktrace
    else:
        context[py_path] = "success"
    return context


class spiders_executor(executor):
    def __init__(self, usethread=True, maxworkers=10, recovery_path = None, maxtasksperworker=None):
        self.__usethread = usethread
        self.__maxworkers=maxworkers
        self.__maxtasksperworker = maxtasksperworker
        self.__isShutdown = False
        self.__recovery_info = None
        self.__recovery_path = recovery_path
        self.__initialize()


    def __initialize(self):
        self.__recovery_info = file_util.read_file_by_line(self.__recovery_path)
        self.__spider_queue = Queue.Queue()
        self.done_queue = Queue.Queue()
        if self.__usethread:
            self.__pool = ThreadPool(processes=self.__maxworkers)   # 线程池
        else:
            self.__pool = Pool(processes=self.__maxworkers, maxtasksperchild=self.__maxtasksperworker)  # 多进程

        self.__mutex = threading.Lock()
        self.__idleCounter = self.__maxworkers  # 空闲Worker计数器
        if self.__idleCounter is None:
            self.__idleCounter = cpu_count()    # 默认worker是CPU的核数


    def push(self,spider):  # spider函数
        self.__spider_queue.put(spider)

    def pop(self):
        return self.__spider_queue.get()

    def __callback(self, context):   # 回调函数
        try:
            self.done_queue.put(context)
        finally:
            self.__increaseIdleCounter()    # task运行完成，空闲进程数+1

    def work_func(self):
        while not self.__isShutdown:
            if self.__idleCounter > 0:
                try:
                    self.__decreaseIdleCounter()
                    context = {}
                    func = self.__spider_queue.get_nowait()
                    self.__pool.apply_async(spider_wrapper, (func, context), callback=self.__callback)
                    # print "11
                    # self.__pool.apply_async(self.pop(), callback=self.__callback)
                except Queue.Empty:
                    self.__pool.close()
                    self.__pool.join()
                    self.shutdown()
                    # print '222'

    def work_shell(self):
        while self.__recovery_info != 0:
            self.__spider_queue.get_nowait()
            self.__recovery_info -=1
        while not self.__isShutdown:
            if self.__idleCounter > 0:
                try:
                    self.__decreaseIdleCounter()
                    context = {}
                    py_path = self.__spider_queue.get_nowait()
                    self.__pool.apply_async(spider_shell, (py_path, context), callback=self.__callback)
                    # print "11111"
                    # self.__pool.apply_async(self.pop(), callback=self.__callback)
                except Queue.Empty:
                    self.__pool.close()
                    self.__pool.join()
                    self.shutdown()
                    # print '222'

    def shutdown(self):
        self.__isShutdown = True


    def __increaseIdleCounter(self):
        self.__mutex.acquire()
        self.__idleCounter += 1
        self.__mutex.release()

    def __decreaseIdleCounter(self):
        self.__mutex.acquire()
        self.__idleCounter -= 1
        self.__mutex.release()

# for test
def func1():
    1/0
    print (func1.__name__)

def func2():
    print (func2.__name__)

if __name__ == '__main__':
    # 扫描脚本
    py_path_list = file_util.find_all_file('/home/XXX/py_path')

    executor = spiders_executor()
    for i in range(0, len(py_path_list)):
        executor.push(py_path_list[i])
    executor.work_shell()
    # executor.push(func1)
    # executor.push(func2)
    # executor.work_func()
    while not executor.done_queue.empty():
        print (executor.done_queue.get())