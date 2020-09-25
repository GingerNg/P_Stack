import sys
import os
current_path = os.path.dirname(os.path.abspath(__file__))
proj_path = os.path.dirname(os.path.dirname(current_path))
sys.path.append(proj_path)
print(proj_path)
os.chdir(proj_path)
from rq import Queue
import redis
# from utils.func import count_words_at_url
from packges.rq_demo.func import count_words_at_url
# 具体业务执行代码


conn = redis.Redis(host='192.168.235.223',
                   port=6379, db=10)  # 指定redis数据库
# 指定队列
q = Queue("high", connection=conn)

job_urls = ['http://baidu.com', 'http://qq.com', 'http://sohu.com']
for url in job_urls:
    q.enqueue_call(count_words_at_url, args=(url,))  # 发送任务
