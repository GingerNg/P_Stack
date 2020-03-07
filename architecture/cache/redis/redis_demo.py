#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : redis_utils.py
"""
redis提供两个类Redis和StrictRedis用于实现Redis的命令，StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令，
Redis是StrictRedis的子类，用于向后兼容旧版本的redis-py。
"""
import time


class RedisInstance(object):

    def __init__(self, redis_type=None, **args):
        if redis_type == "cluster":
            import rediscluster
            self.r_conn = rediscluster.StrictRedisCluster(**args)
        else:
            import redis
            self.r_conn = redis.StrictRedis(**args)

    def get_value(self, name):
        return self.r_conn.get(name)

    def incr_value(self, name):
        return self.r_conn.incr(name)

    def set_value(self, name, value):
        self.r_conn.set(name, value)

    def getset_value(self, name, value):
        return self.r_conn.getset(name, value)


if __name__ == '__main__':
    # 单点
    conn_dict = {
        'host': 'XXX.XXX.XXX.XXX',
        'port': 22,
        'datastorage': 0
    }

    # redis_type = 'single'
    # redis_instance = RedisInstance(redis_type, **conn_dict)
    # print(redis_instance.set_value('name', 'test'))
    # print(redis_instance.get_value('name'))
    # print(redis_instance.getset_value('name', 0))
    # print(redis_instance.get_value('name'))

    # cluster
    # conn_dict = {
    #     "startup_nodes": [
    #         {'host': '127.0.0.1', 'port': 9001},
    #         {'host': '127.0.0.1', 'port': 9002},
    #         {'host': '127.0.0.1', 'port': 9003}
    #     ]
    # }
    # redis_type = 'cluster'
    # myredis = RedisInstance(redis_type, **conn_dict)
    # print(myredis.SetValue('name', 'test'))
    # print(myredis.GetValue('name'))
    # print(myredis.GetSetValue('name', 0))
    # print(myredis.GetValue('name'))

    """获取所有的key"""
    import redis

    pool = redis.ConnectionPool(host='X.X.X.X', port=8079, db=0)
    r = redis.StrictRedis(connection_pool=pool)

    keys = r.keys()
    print (type(keys))
    for key in keys:
        print(key)

    """
    hash是一个string类型的field和value的映射表
    key跟下标索引有一定的关系，所实现的，让他的查找算法复杂度变为常数O（1）
    name对应的hash中设置一个键值对
    https://www.jianshu.com/p/2639549bedc8
    """
    r.hset("hash1", "k1", "v111")
    r.hset("hash1", "k2", "v211")
    r.hset("hash1","file_id", time.time())
    print(r.hmget("hash1", "k1", "k2"))  # 多个取hash的key对应的值
    print(r.hgetall("hash1"))
    print(r.hlen("hash1"))

    # """获取所有内容"""
    # import redis
    #
    # r = redis.Redis(connection_pool=pool)
    #
    # pipe = r.pipeline()
    # pipe_size = 100000
    #
    # len = 0
    # key_list = []
    # print (r.pipeline())
    # keys = r.keys()
    # for key in keys:
    #     key_list.append(key)
    #     pipe.get(key)
    #     if len < pipe_size:
    #         len += 1
    #     else:
    #         for (k, v) in zip(key_list, pipe.execute()):
    #             print(k, v)
    #         len = 0
    #         key_list = []
    #
    # for (k, v) in zip(key_list, pipe.execute()):
    #     print(k, v)