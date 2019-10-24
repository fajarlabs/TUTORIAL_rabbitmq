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

# create channel
channel = connection.channel()

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(
    queue='AUTO_DELETE', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()