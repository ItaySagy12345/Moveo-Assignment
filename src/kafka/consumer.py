import json
from confluent_kafka import Consumer, KafkaException, KafkaError
from src.utils.logger import logger
from src.kafka.utils.config import KAFKA_CONFIG
from src.kafka.utils.topics import KafkaTopics


class KafkaConsumer:
    def __init__(self, name: str):
        self.name = name
        self.consumer = Consumer(KAFKA_CONFIG)

    def subscribe(self, topics: list[KafkaTopics]) -> None:
        """
        Subscribe to a Kafka topic
        Param: topics List[KafkaTopics]: The kafka topics to consume
        Return: None
        """
        
        topics = [topic.value for topic in topics]
        self.consumer.subscribe(topics=topics)
        self._log(f"Subscribed to topics: {json.dumps(topics)}")

    def consume(self) -> None:
        """
        Consume messages from subscribed Kafka topics
        Return: None
        """

        try:
            self._log("Open")

            while True:
                message = self.consumer.poll(timeout=1.0)

                if message is None:
                    continue
                elif message.error():
                    if message.error().code() == KafkaError._PARTITION_EOF:
                        self._log(f"End of partition reached")
                    else:
                        raise KafkaException(message.error())
                else:
                    self._log(f"Consumed message: {message.value().decode('utf-8')}")

        finally:
            self._log("Closed")
            self.consumer.close()

    def _log(self, log: str) -> None:
        """
        Log wrapper
        Param: log [String]: The log to wrap
        Return: None
        """

        logger.info(f"KAFKA CONSUMER ({self.name}): {log}")
