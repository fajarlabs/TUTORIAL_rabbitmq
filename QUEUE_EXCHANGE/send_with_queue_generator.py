#!/usr/bin/python
import pika
import time

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

message = "Hello world!"

# menggunakan jalur exchange tanpa queue
# exchange == EXCHANGE, routing_key == QUEUE
# data dikirim tanpa disimpan
channel.basic_publish(exchange='jalur_khusus', routing_key='', body=message)

print(" [x] Sent %r" % message)
connection.close()
