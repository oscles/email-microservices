import json

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(queue='send_email')


def send_email_channel(data):
    channel.basic_publish(
        exchange='',
        routing_key='send_email',
        body=data
    )


def initialize():
    subject = input('Ingrese el asunto: ')
    to_address = input('Ingrese el email destino: ')
    message = input('Ingrese su mensaje: ')
    to_json = json.dumps({
        'subject': subject,
        'to_address': to_address,
        'body': message,
    })
    send_email_channel(to_json)


if __name__ == '__main__':
    initialize()
