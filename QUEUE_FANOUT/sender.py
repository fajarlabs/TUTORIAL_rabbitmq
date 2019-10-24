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

"""
CREATE CHANNEL
"""
channel = connection.channel()

"""
Jika ada error ini (406, "PRECONDITION_FAILED - inequivalent arg 'type' for exchange 'jalur_khusus' in vhost '/development': received 'direct' but current is 'fanout'
artinya EXCHANGE udah ada tapi beda exchange_type
"""
channel.exchange_declare(exchange='jalur_khusus', exchange_type='fanout')

"""
PUBLISH MESSAGE WITH INTERVAL
"""
message = "HELLO ALL FRIENDS!"
while True :
	channel.basic_publish(exchange='jalur_khusus', routing_key='', body=message)
	time.sleep(1)

connection.close()
