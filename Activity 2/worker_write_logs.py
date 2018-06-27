import json

import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout',
)

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(
    exchange='logs',
    queue=queue_name
)

print(f'[*] Starting worker write logs with queue {queue_name}')


def callback(channel, method, properties, body):
    with open('logs.log', 'a') as csv:
        data = json.loads(body)['body']
        message = f"[{data.get('code')}] {data.get('type')}\n"
        csv.writelines(message)
    csv.close()
    print(f'[*] Message for broker write logs {queue_name}.')
    print(f'A new line was created in the logs.log file --- {message}.')

    channel.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(callback, queue=queue_name, no_ack=False)
channel.start_consuming()
