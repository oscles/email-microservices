import json
from random import choice

import pika

from db_errors import ERRORS_LIST as ERRORS

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout',
)


def send_email_errors():
    subject = input('Insert the subject: ')
    to_address = input('Insert the destine address: ')
    body = choice(ERRORS)

    data = {
        'subject': subject,
        'to_address': to_address,
        'body': body,
    }

    channel.basic_publish(
        exchange='logs',
        routing_key='',
        body=to_json(data=data)
    )
    print(f'[*] Send body with code {choice(ERRORS)["code"]}')


def to_json(data):
    return json.dumps(data)


send_email_errors()
connection.close()
