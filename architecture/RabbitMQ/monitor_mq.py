# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: monitor_mq.py
@time: 2018/5/24 15:17
"""
import pika

pika_conn_params = pika.ConnectionParameters(
    host='X.X.X.X', port=5672,
    credentials=pika.credentials.PlainCredentials('guest', 'guest'),
)
connection = pika.BlockingConnection(pika_conn_params)

channel = connection.channel()
queue = channel.queue_declare(
    queue="hello",
    exclusive=False, auto_delete=False
)
# queue = channel.queue_declare(
#     queue="hello", durable=True,
#     exclusive=False, auto_delete=False
# )

print(queue.method.message_count)