# coding:utf8
# author:ginger


import time
import threadpool
def sayhello(str):
    print "Hello ",str
    time.sleep(2)

name_list =['xiaozi','aa','bb','cc']
start_time = time.time()
pool = threadpool.ThreadPool(10)
make_requests = threadpool.makeRequests(sayhello, name_list)
[pool.putRequest(req) for req in make_requests]
pool.wait()
print '%d second'% (time.time()-start_time)