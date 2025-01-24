import json
from confluent_kafka import Consumer, KafkaException, KafkaError
from src.utils.logger import logger
from src.kafka.topics import KafkaTopics


class KafkaConsumer:
    config = {     
        'bootstrap.servers': 'kafka:9093',
        'group.id': 'fastapi-consumer',
        'auto.offset.reset': 'earliest'
    }
    
    def __init__(self, name: str):
        self.name = name
        self.consumer = Consumer(self.config)
        logger.info("Initialized")

    def subscribe(self, topics: list[KafkaTopics]) -> None:
        """
        Subscribe to a Kafka topic
        Param: topics List[KafkaTopics]: The kafka topics to consume
        Returns: None
        """
        
        topics: list[str] = [topic.value for topic in topics]
        self.consumer.subscribe(topics=topics)
        self._log(f"Subscribed to topics: {json.dumps(topics)}")

    def consume(self) -> None:
        """
        Produce a Kafka message to a specific topic
        Returns: None
        """
                
        try:
            self._log("Open")
            
            while True:
                message = self.consumer.poll(timeout=1.0)

                if message is None:
                    continue
                elif message.error():
                    if message.error().code() == KafkaError._PARTITION_EOF:
                        self._log(f"End of partition reached {message.partition()} at offset {message.offset()}")
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
        Returns: None
        """

        logger.info(f"KAFKA CONSUMER ({self.name}): {log}")