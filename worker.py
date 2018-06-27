import json

from conection import PikaConnection
from email_send import EmailSender

connection = PikaConnection(hostname='localhost', queue='send_email')


def send_email(channel, method, properties, body):
    serializer = json.loads(body)
    EmailSender(**serializer).send()
    channel.basic_ack(delivery_tag=method.delivery_tag)


connection.channel.basic_consume(send_email, queue='send_email', no_ack=False)
connection.channel.start_consuming()
