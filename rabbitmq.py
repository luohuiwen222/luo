#!/usr/bin/python3
import pika
import json
credentials = pika.PlainCredentials('admin','123456')

connection= pika.BlockingConnection(pika.ConnectionParameters(host = '192.168.74.71',port = 5672,virtual_host = '/',credentials = credentials))
channel = connection.channel()
esult = channel.queue_declare( queue='rabbit-test')

for  i in  range(200):
    message=json.dumps({'OrdetId':"1000%s"%i})
    channel.basic_publish(exchange = '',routing_key= 'rabbit-test',body = message)
    print(message)
connection.close()