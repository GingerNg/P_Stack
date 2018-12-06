#!/usr/bin/env python
"""
CSDN专栏:RabbitMQ 从入门到精通

默认情况rabbitMQ 会顺序的分发每个Message。
当每个收到ack后，会将该Message删除，然后将下一个Message分发到下一个Consumer。这种分发方式叫做round-robin

RabbitMQ仅仅通过Consumer的连接中断来确认该Message并没有被正确处理。也就是说，RabbitMQ给了Consumer足够长的时间来做数据处理。

为了保证在RabbitMQ退出或者crash了数据仍没有丢失，需要将queue和Message都要持久化。
durable：rabbitmq服务端宕机 消息不丢失


no-ack＝False：rabbitmq消费者连接断了 消息不丢失
https://www.cnblogs.com/wangqiaomei/p/5715331.html

Fair dispatch 公平分发

https://www.cnblogs.com/wangqiaomei/p/5715331.html
"""
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='X.X.X.X'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!-2')
print (" [x] Sent 'Hello World!'")
connection.close()
