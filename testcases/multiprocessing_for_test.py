# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: multiprocessing_for_test.py
"""

from multiprocessing import Pool, cpu_count
import os, time, random

import requests

url = "http://XXX.XXXX.XXXX.XXX:XXXX/XXX/"
content=""

json_date = {
    "data": content
}

# json_date = {
# 	"input_path":"/opt/project/ner_sftp/input",
# 	"output_path":"/opt/project/ner_sftp/output"
# }

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

def request_tasks(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    for i in range(50):
        try:
            st = time.time()
            # res = requests.post(url=url, json=json_date)
            res = requests.get(url=url)
            time_span = time.time() - st
            # print(res.content)
            print( name, i, res.status_code,time_span)
        except Exception as e:
            print(e)
    # print('Task %s runs %0.2f seconds.' % (name, (end - start)))

def m1(x):
    print(x * x)


class processor(object):
    def __init__(self):
        self._quit = False
    def quit(self):
        '''Set quit signal'''
        self._quit = True

    def run(self):

        '''Run loop'''
        # logger.info("processor starting...")

        while not self._quit:
            time.sleep(5)
            print("i am working")


if __name__=='__main__':
    print('Parent process %s.' % os.getpid())

    st_all = time.time()

    p = Pool(10)
    for i in range(10):
        p.apply_async(request_tasks, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()

    time_span = time.time() - st_all
    print('All subprocesses done. 消耗时间：%s' % time_span)
    print(5000/time_span)

    """
    外网请求，网络延迟大概是10ms"""

    """
    进程操作
    """