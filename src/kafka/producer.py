from confluent_kafka import Producer
from src.utils.logger import logger
from src.kafka.topics import KafkaTopics


class KafkaProducer:
    config = {
        'bootstrap.servers': 'kafka:9093',
        'client.id': 'fastapi-producer'
    }

    def __init__(self):
        self._producer = Producer(self.config)

    def produce(self, topic: KafkaTopics, message: str) -> None:
        """
        Produce a Kafka message to a specific topic
        Param: topic [KafkaTopics]: The kafka topic to which the message will be produced
        Param: message [String]: The message to produce
        Returns: None
        """

        self._producer.produce(topic=topic.value, value=message.encode('utf-8'), callback=self._report)
        self._producer.flush()

    def _report(self, error: str, message: str) -> None:
        """
        Callback function that reports on the newly produced message
        Param: error [String]: The error if there is one
        Param: message [String]: The message produced
        Returns: None
        """

        if error:
            self._log(f"Message delivery failed: {error}")
        else:
            self._log(f"Message delivered to {message.topic()}")

    def _log(self, log: str) -> None:
        """
        Log wrapper
        Param: log [String]: The log to wrap
        Returns: None
        """

        logger.info(f"KAFKA PRODUCER: {log}")


kafka_producer = KafkaProducer()