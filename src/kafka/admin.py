from confluent_kafka.admin import AdminClient, NewTopic
from src.kafka.utils.topics import KafkaTopics
from src.utils.logger import logger
from src.kafka.utils.config import KAFKA_CONFIG


class KafkaAdmin:
    def __init__(self):
        self.admin = AdminClient({'bootstrap.servers': KAFKA_CONFIG['bootstrap.servers']})

    def get_existing_topics(self) -> list[str]:
        """
        Returns the list of existing Kafka topics
        Return: List[str] The list of existing topics
        """
        
        return self.admin.list_topics(timeout=10).topics
    
    def create_topic(self, topics: list[KafkaTopics]) -> None:
        """
        Creates a new Kafka topic
        Param: topics List[KafkaTopics] The Kafka topics to create
        Return: None
        """

        try:
            new_topics = [NewTopic(topic=topic.value, num_partitions=1, replication_factor=1) for topic in topics]
            create_results = self.admin.create_topics(new_topics)

            for topic, result in create_results.items():
                    try:
                        result.result()
                        self._log(f"Successfully created topic: {topic}")
                    except Exception as e:
                        raise RuntimeError(f"Failed to create topic {topic}: {e}")
        except Exception as e:
            self._log(f"Failed to create topic {topic}: {e}")
            raise RuntimeError(f"Failed to create topic {topic}: {e}")

    def _log(self, log: str) -> None:
        """
        Log wrapper
        Param: log [String]: The log to wrap
        Return: None
        """

        logger.info(f"KAFKA ADMIN: {log}")


kafka_admin = KafkaAdmin()