import json

from conection import PikaConnection

connection = PikaConnection(hostname='localhost', queue='send_email')


def send_email_channel(data):
    connection.channel.basic_publish(
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
