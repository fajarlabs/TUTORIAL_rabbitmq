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

# create QUEUE by script
# fungsi ini adalah membuat queue bila belum dibuat, tapi sifatnya non-durable
# atau ketika server rabbit di restart data yang ada queue akan hilang / hapus
# exchange_declare(exchange, exchange_type='direct', passive=False, durable=False, auto_delete=False, internal=False, arguments=None, callback=None)
channel.exchange_declare('myexchange','direct')

# close channel
connection.close()
