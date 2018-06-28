import json

import pika

from email_send import EmailSender

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.exchange_declare(
    exchange='logs',
    exchange_type='direct',
)

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(
    exchange='logs',
    queue=queue_name,
    routing_key='error',
)

print(f'[*] Starting worker send email with queue {queue_name}')


def callback(channel, method, properties, body):
    body = json.loads(body)
    subject = body.get('subject')
    to_address = body.get('to_address')
    message = f"Code: {body.get('body')['code']}\n" \
              f"Type: {body.get('body')['type']}\n" \
              f"Message: {body.get('body')['body']}"

    EmailSender(
        subject=subject,
        to_address=to_address,
        body=message
    ).send()

    print(f'[*] Message for broker send email {queue_name}.')


channel.basic_consume(callback, queue=queue_name, no_ack=False)
channel.start_consuming()
