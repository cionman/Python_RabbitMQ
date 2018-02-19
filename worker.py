import pika
import time
import datetime

from pika.adapters.blocking_connection import BlockingChannel

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

print('# 메세지를 기다리고 있습니다. 종료하려면 CTRL+C를 누르세요.')


def callback(ch:BlockingChannel, method, properties, body):
    msg = str(body, "utf8").split(":")
    print(
        '# [%s] %s 메세지를 받았습니다. \n %r' % (datetime.datetime.now(), msg[0], body))

    time.sleep(int(str(msg[1])) / 10)
    print(" # [%s] 완료했습니다." % datetime.datetime.now())
    ch.basic_ack(delivery_tag= method.delivery_tag)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback, queue='task_queue')

channel.start_consuming()