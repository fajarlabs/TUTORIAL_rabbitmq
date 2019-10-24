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
# queue_declare(queue, passive=False, durable=False, exclusive=False, auto_delete=False, arguments=None, callback=None)
channel.queue_declare(queue='MY_QUEUE')

# close channel
connection.close()
