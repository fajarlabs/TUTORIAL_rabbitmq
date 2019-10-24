#!/usr/bin/python
import pika

USERNAME = 'admin'
PASSWORD = 'KantorB29'
HOSTNAME = '192.168.10.213'
PORT = 5672
VIRTUALHOST = '/development'
STATIC_QUEUE = ''

credentials = pika.PlainCredentials(USERNAME, PASSWORD)
parameters = pika.ConnectionParameters(HOSTNAME,PORT,VIRTUALHOST,credentials)
connection = pika.BlockingConnection(parameters)

"""
CREATE CHANNEL
"""
channel = connection.channel(2)

result = channel.queue_declare(queue='', exclusive=True)
queueName = result.method.queue
print(queueName)
channel.queue_bind(exchange='jalur_khusus', queue=queueName)

print(' [*] Waiting for jalur_khusus. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(queue=queueName, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
