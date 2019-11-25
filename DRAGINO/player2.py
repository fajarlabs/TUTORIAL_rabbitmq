#!/usr/bin/python
import pika

#QUEUE_NAME = 'Q_DEV'
ROUTING_KEY = 'R_DEV'

credentials = pika.PlainCredentials('admin', 'KantorB29')
parameters = pika.ConnectionParameters('192.168.10.213',5672,'/development',credentials)
connection = pika.BlockingConnection(parameters)

"""
CREATE CHANNEL
"""
channel = connection.channel()
channel.exchange_declare(exchange='logs',exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queueName = result.method.queue
print(queueName)
channel.queue_bind(exchange='logs', queue=queueName, routing_key=ROUTING_KEY)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(queue=queueName, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
