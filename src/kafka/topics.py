from enum import Enum


class KafkaTopics(Enum):
    """
    An enum for Kafka topics
    """

    ITEM_CREATED = 'item_created'
    ITEM_UPDATED = 'item_updated'