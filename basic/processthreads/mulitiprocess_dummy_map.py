"""
dummy 是 multiprocessing 模块的完整克隆，唯一的不同在于 multiprocessing 作用于进程，
而 dummy 模块作用于线程（因此也包括了 Python 所有常见的多线程限制）
CPU密集型--多进程
IO密集型--多线程   dummy
"""
import requests
# import urllib3
from multiprocessing.dummy import Pool as ThreadPool

# 一般来说，执行 CPU 密集型任务时，调用越多的核速度就越快。
# 但是当处理网络密集型任务时，事情有有些难以预计了，通过实验来确定线程池的大小才是明智的。
pool = ThreadPool(4)

urls = [
    'http://www.python.org',
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'https://wiki.python.org/moin/',
    'http://planet.python.org/',
    'https://wiki.python.org/moin/LocalUserGroups',
    'http://www.python.org/psf/',
    'http://docs.python.org/devguide/',
    'http://www.python.org/community/awards/'
    # etc..
    ]

def task(url):
    res = requests.get(url=url)
    print(res.content)

"""
适合一次性取数据,多线程/多进程处理
"""
# Make the Pool of workers
# Open the urls in their own threads
# and return the results
results = pool.map(task, urls)
#close the pool and wait for the work to finish
pool.close()
pool.join()




