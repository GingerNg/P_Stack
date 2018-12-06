#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: kafka_demo.py
 @author: ginger 
 @software: PyCharm
 @desc:
 @source: https://www.cnblogs.com/yueyanyu/p/6409374.html
"""

from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import json
import _thread, threading


class Kafka_producer():
    '''
    使用kafka的生产模块
    '''

    def __init__(self, kafkahost,kafkaport, kafkatopic):
        self.kafkaHost = kafkahost
        self.kafkaPort = kafkaport
        self.kafkatopic = kafkatopic
        self.producer = KafkaProducer(bootstrap_servers = '{kafka_host}:{kafka_port}'.format(
            kafka_host=self.kafkaHost,
            kafka_port=self.kafkaPort
            ))

    def sendjsondata(self, params):
        try:
            parmas_message = json.dumps(params)
            producer = self.producer
            producer.send(self.kafkatopic, parmas_message.encode('utf-8'))
            producer.flush()
        except KafkaError as e:
            print (e)


class Kafka_consumer():
    '''
    使用Kafka—python的消费模块
    '''

    def __init__(self, kafkahost, kafkaport, kafkatopic, groupid):
        self.kafkaHost = kafkahost
        self.kafkaPort = kafkaport
        self.kafkatopic = kafkatopic
        self.groupid = groupid
        self.consumer = KafkaConsumer(self.kafkatopic, group_id = self.groupid,
                                      bootstrap_servers = '{kafka_host}:{kafka_port}'.format(
            kafka_host=self.kafkaHost,
            kafka_port=self.kafkaPort ))

    def consume_data(self):
        try:
            for message in self.consumer:
                # print json.loads(message.value)
                yield message  # yield 生成迭代器
        except KeyboardInterrupt as e:  # python3
            print (e)


def main():
    '''
    测试consumer和producer
    :return:
    '''
    #测试生产模块
    producer = Kafka_producer("XXX.XXX.XXX.XXX", 9200, "XX")
    for id in range(10):
        mq_message = {
            "id": "task_id",
            "info_meta": {"file_id":"001"}
        }
        print(mq_message)
        producer.sendjsondata(mq_message)





if __name__ == '__main__':
    main()
