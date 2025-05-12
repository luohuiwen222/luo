#!/usr/bin/python3
import pika
import json
#用户名
cert  =  pika.PlainCredentials('admin','123456')
#连接到服务器
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.74.72',5672,'/',cert))
#创建频道
channel = connection.channel()
#声明消息队列，如果不存在就创建
channel.queue_declare( queue='rabbit-test')

def callback(ch,method,properties,body):
    print("[x] Received %r" % body)
channel.basic_consume('rabbit-test', callback,
                                auto_ack=False,
                                exclusive=False,
                                consumer_tag=None,
                                arguments=None
                            )
print('[*] Waiting for message. To exit press CTRL+C')
channel.start_consuming()