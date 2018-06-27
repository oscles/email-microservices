import pika


class PikaConnection:

    def __init__(self, hostname, queue):
        self.queue = queue
        self.__connection = self.__initilize_connection(hostname)
        self.__channel = self.__connection.channel()
        self.__channel.queue_declare(queue)

    def __initilize_connection(self, hostname):
        return pika.BlockingConnection(
            pika.ConnectionParameters(hostname)
        )

    @property
    def channel(self):
        return self.__channel

    def closed(self):
        self.__connection.close()
