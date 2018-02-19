import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" # 메세지를 받았습니다 : %r" % str(body,'utf8'))


channel.basic_consume(callback, queue='hello', no_ack=True)

print('# 메세지를 기다리고 있습니다. 종료하려면 CTRL+C를 누르세요')

channel.start_consuming()