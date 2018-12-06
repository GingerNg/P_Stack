#!/usr/bin/env python
'''
http://blog.csdn.net/anzhsoft/article/details/19570187


'''
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='X.X.X.X'))
channel = connection.channel()

channel.queue_declare(queue='hello')

print (' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print (" [x] Received %r" % (body,))
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=False)  # 默认情况下，消息确认是打开的（enabled）--> 默认情况下 no_ack=false

# 当no_ack=False: 收到消息后，不ack，


channel.start_consuming()
