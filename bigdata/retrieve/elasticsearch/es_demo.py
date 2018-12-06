# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: es_demo.py
@time: 2018/4/13 10:12
@desc: python client connect to elasticsearch
"""
# http://www.cnblogs.com/letong/p/4749234.html
# http://elasticsearch-py.readthedocs.io/en/master/api.html#elasticsearch
# http://blog.csdn.net/xiaoxinwenziyao/article/details/49471977
# https://github.com/Parsely/pykafka

from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

# 使用kafka 走正式流程操作
#from pykafka import KafkaClient

# topicName = ""
# kafkaHosts = ""
# client = KafkaClient(hosts=kafkaHosts)
# topic = client.topics[topicName]
# producer = topic.get_producer()
es = Elasticsearch([{"host": "XXX.XXX.XXX.XXX", "port": 8004, "timeout": 15000}])
es_Test = Elasticsearch([{"host": "XXX.XXX.XXX.XXX", "port": 9200}])


# {"method":"save","data":[{},{}]}
# def save4Kafka(result):
#   DATAS=[]
#   for rdata in result["hits"]["hits"]:
#       source = rdata["_source"]
#       DATAS.append(source)

#   producer.produce({"method":"save","data":DATAS}.toString)
#
def save4ES(result):
    ACTIONS = [];
    for rdata in result["hits"]["hits"]:
        source = rdata["_source"]
        action = {
            "_index": indexName,
            "_type": typeName,
            "_source": source
        }
        ACTIONS.append(action)

    success = bulk(es_Test, ACTIONS, index=indexName, raise_on_error=True)

    print (success)


indexName = ""
typeName = ""

# 总条数
count = es.count(index=indexName)["count"]

# 每页多少条
pageLine = 1000;

# 多少页
# page = (count&pageLine) == 0?(count/pageLine):(count/pageLine+1)
page = count / pageLine if (count % pageLine) == 0 else count / pageLine + 1
page = 7234
# 获取数据.分页获取
# for x in range(7233, page):
#     result = es.search(index=indexName, from_=x * pageLine, size=pageLine)
#     # save4Kafka(result)
#     save4ES(result)

if __name__ == "__main__":
    # res = es.get(index="my-index", doc_type="test-type", id=1)
    # print (res)
    print ("----")
    # 插入数据
    # es.index(index="my-index", doc_type="test-type", id=1, body={"any": "data02", "timestamp": datetime.now()})
    res = es.get(index="my-index", doc_type="test-type", id=1)
    print (res)
    # res = es.get(index="my-index", doc_type="test-type")
    # print(res)

    # result = es.search(index="mydb", body={'_type':'test'}) ## “index = db的名称”
    """
    index <==> datastorage
    doc_type <==> collection
    """
    # result = es.search(index="mydb",doc_type="test")
    # for rdata in result["hits"]["hits"]:
    #     print (rdata)

