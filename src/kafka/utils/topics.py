from enum import Enum

class KafkaTopics(Enum):
    """
    An enum class for Kafka topics
    """

    ITEM_CREATED = 'item_created'
    ITEM_UPDATED = 'item_updated'