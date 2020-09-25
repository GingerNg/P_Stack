import sys
import os
current_path = os.path.dirname(os.path.abspath(__file__))
proj_path = os.path.dirname(os.path.dirname(current_path))
sys.path.append(proj_path)
print(proj_path)
os.chdir(proj_path)
import redis
from multiprocessing import Pool
# from multiprocessing.dummy import Pool
from rq import Worker, Queue, Connection
# from utils.func import count_words_at_url

conn = redis.Redis(host='192.168.235.223',
                   # password='123456',
                   port=6379, db=10)  # 同一个redis连接

# worker逻辑，无需修改


def worker(listen):
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()


if __name__ == "__main__":
    listen = ['high', 'default', 'low']            # 监听的队列，可自定义修改
    try:
        cpu_num = 1
        p = Pool(cpu_num)
        for i in range(cpu_num):
            p.apply_async(worker, args=(listen,))  # 开启worker
        p.close()
        p.join()
    except Exception as e:
        print(e)
