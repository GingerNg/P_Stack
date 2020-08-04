
from rq import Queue
import redis
from utils.func import count_words_at_url
# 具体业务执行代码


conn = redis.Redis(host='127.0.0.1',
                   port=6379, db=10)  # 指定redis数据库
# 指定队列
q = Queue("high", connection=conn)

job_urls = ['http://baidu.com', 'http://qq.com', 'http://sohu.com']
for url in job_urls:
    q.enqueue_call(count_words_at_url, args=(url,))  # 发送任务
