# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: mongo_test.py
@time: 2018/8/3 15:22
"""
from pymongo import MongoClient

conn = MongoClient('X.X.X.X', 21117)

print (conn.database_names)


db = conn.mydb  # 连接mydb数据库，没有则自动创建
my_set = db.testSync # 使用test_set集合，没有则自动创建

data = {"url": "24_1932523_2018-04-16", "updatetime": 1517990450.949889, "_id": "testSync2", "result": {"hotel_level_ctrip": "携程"}, "taskid": "b11a0bf670e1b9ece3d674fc12e02187"}
my_set.insert(data)