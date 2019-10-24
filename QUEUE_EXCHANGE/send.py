#!/usr/bin/python
import pika
import time

USERNAME = 'admin'
PASSWORD = 'KantorB29'
HOSTNAME = '192.168.10.213'
PORT = 5672
VIRTUALHOST = '/development'

credentials = pika.PlainCredentials(USERNAME, PASSWORD)
parameters = pika.ConnectionParameters(HOSTNAME,PORT,VIRTUALHOST,credentials)
connection = pika.BlockingConnection(parameters)

# create channel
channel = connection.channel()

# menggunakan jalur exchange tanpa queue
# exchange == EXCHANGE, routing_key == QUEUE
# data dikirim tanpa disimpan
while True :
	channel.basic_publish(exchange='jalur_khusus', routing_key='Q1', body='Message for Q1')
	time.sleep(0.4)
	channel.basic_publish(exchange='jalur_lambat', routing_key='Q2', body='Message for Q2')
	time.sleep(0.4)

print(" [x] Sent %r" % message)
connection.close()
