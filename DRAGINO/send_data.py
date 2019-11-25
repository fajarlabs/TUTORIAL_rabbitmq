#!/usr/bin/python
from argparse import ArgumentParser
import ConfigParser
import pika
import time
import os

config_device = ConfigParser.RawConfigParser()
config_device.read('/root/device.ini')
config_rabbit = ConfigParser.RawConfigParser()
config_rabbit.read('/root/config.ini')

PATH_STORE = '/tmp/store.log'
QUEUE_ROUTING = 'Q_DATA'

"""
ARGUMENT PARSER PASS FROM PROCESS
"""
parser = ArgumentParser()
parser.add_argument("-a", "--action", dest="action", help="Action for sending data")
parser.add_argument("-d", "--data", dest="data", help="Data for sending to rabbitmq")
parser.add_argument("-q", "--queue", action='store_true', dest="queue", help="Set queue data")
args = parser.parse_args()

if args.action == "send":
	credentials = pika.PlainCredentials(config_rabbit.get('GATEWAY','username'), config_rabbit.get('GATEWAY','password'))
	parameters = pika.ConnectionParameters(config_rabbit.get('GATEWAY','hostname'),config_rabbit.getint('GATEWAY','port'),config_rabbit.get('GATEWAY','vhost'),credentials)
	connection = pika.BlockingConnection(parameters)

	"""
	CREATE CHANNEL
	"""
	channel = connection.channel()

	"""
	DECLARE QUEUE
	"""
	channel.queue_declare(queue=QUEUE_ROUTING)

	with open(PATH_STORE) as f:
		idx = 1
		for line in f:
			try :
				# publish messages
				channel.basic_publish(exchange='', routing_key=QUEUE_ROUTING, body=line.strip())
				# delete data after publish message
				os.system("sed -i -e '"+str(idx)+" d' "+PATH_STORE)
			except Exception as e :
				print(e)
			finally:
				idx += 1

	connection.close()
