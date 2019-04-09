import _thread
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process
from queue import Queue

"""
多次取数据，多线程/多进程处理
"""

##############***********loader

class Loader(object):
    def __init__(self,queue):
        self.queue = queue

    def work(self):
        self.load()
        # while True:
        #     self.load()
        #     time.sleep(5)

    def load(self):
        self.queue.put("1212")
        self.queue.put("1212")
        self.queue.put("1212")


class DemoLoader(Loader):
    
    def load(self):
        for i in range(10):
            # self.queue.put(str(i))
            self.queue.put_nowait(str(i)+"..."+str(time.time()))

    def work(self):
        while True:
            if self.queue.qsize() < self.queue.maxsize/2:
                self.load()
            else:
                time.sleep(5)

#####################**************worker

class Worker(object):
    def __init__(self,queue,thread_num = "0"):
        self.queue = queue
        self.thread_num = thread_num

    def work(self,):
        while True:
            # print(self.queue.qsize())
            if self.queue.empty():
                break
            message = self.queue.get_nowait()
            try:
                print(message)
                self.task(message)
            except Exception as e:
                print(e)


    def task(self,message):

        print("demo")

class DemoWorker(Worker):
    def task(self,message):
        time.sleep(0.5)
        # print("I am demo")
        print(self.thread_num)


#######********************Exector

class Exector(object):
    def __init__(self):
        pass


class MultiThreadExector(Exector):
    """多线程执行器"""
    def __init__(self,Worker,Loader,work_num=10,q_length=10000,reload=0):
        queue = Queue(q_length)
        self.loader = Loader(queue)
        self.loader.load()
        self.threads = []
        self.reload = reload
        if self.reload:
            t = threading.Thread(target=self.loader.work, args=())
            t.start()
        for i in range(work_num):
            worker = Worker(queue,thread_num=str(i))
            t = threading.Thread(target=worker.work, args=())
            t.start()
            self.threads.append(t)

    def start(self):
        for t in self.threads:
            t.join()   # 阻塞线程直到结束


class MultiProcessExector(Exector):
    """多进程执行器"""
    def __init__(self,Worker,Loader,work_num,q_length=10000,reload=0):
        queue = Queue(q_length)
        self.loader = Loader(queue)
        self.loader.load()
        self.processes = []
        self.reload = reload
        if self.reload:
            t = threading.Thread(target=self.loader.work, args=())
            t.start()
        for i in range(work_num):
            worker = Worker(queue, thread_num=str(i))
            p = Process(target=worker.work, args=())
            p.start()
            self.processes.append(p)

    def start(self):
        for t in self.processes:
            t.join()   # 阻塞线程直到结束


if __name__ == '__main__':
    exector = MultiThreadExector(DemoWorker, DemoLoader, 5, q_length=100, reload=1)
    exector.start()

    # exector = MultiProcessExector(DemoWorker, DemoLoader, 5, q_length=100, reload=1)
    # exector.start()


