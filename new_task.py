import pika
import random

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

# durable 옵션 서버 실행이 중단되었다가 다시 실행될때도 상태 유지
channel.queue_declare(queue='task_queue', durable=True)

msgs = [str(i) + ":" + str(random.randrange(1, 11)) for i in range(100)]


def send_msg(msg):
    channel.basic_publish(exchange='', routing_key='task_queue', body=str(msg))


for msg in msgs:
    send_msg(msg)
    print(' # 메세지를 보냈습니다: %r' % msg)

connection.close()
