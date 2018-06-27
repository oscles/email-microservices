import json
import pika

from email_send import EmailSender

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(queue='send_email')


def send_email(channel, method, properties, body):
    serializer = json.loads(body)
    EmailSender(**serializer).send()
    channel.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(send_email, queue='send_email', no_ack=False)
channel.start_consuming()
