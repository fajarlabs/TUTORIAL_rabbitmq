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

while True :
	"""
	QUEUE dibuat DURABLE oleh admin RABBITMQ
	di sender, routing_key adalah nama dari queuenya yang telah dibuat terlebih dahulu
	"""
	channel.basic_publish(exchange='', routing_key='chat', body='Hello World!')
	print(" [x] Sent 'Hello World!'")
	time.sleep(1)
connection.close()
