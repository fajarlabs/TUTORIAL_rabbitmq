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

"""
Jika ada error ini (406, "PRECONDITION_FAILED - inequivalent arg 'type' for exchange 'logs' in vhost '/development': received 'direct' but current is 'fanout'
artinya EXCHANGE udah ada tapi beda exchange_type
"""
channel.exchange_declare(exchange='logs', exchange_type='fanout')

"""
PUBLISH MESSAGE WITH INTERVAL
"""
channel.basic_publish(exchange='logs', routing_key=ROUTING_KEY, body='10.23.2019')
connection.close()
