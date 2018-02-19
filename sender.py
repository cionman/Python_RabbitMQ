import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello')

msg = ""

while msg != 'exit':
    msg = input("보낼 메세지를 작성하세요. :")
    channel.basic_publish(exchange='', routing_key='hello', body=msg)
    print('# 메세지를 보냈습니다!')

connection.close()