from src.kafka.consumer import KafkaConsumer
from src.kafka.topics import KafkaTopics


item_consumer = KafkaConsumer(name='item_consumer')
item_consumer.subscribe([KafkaTopics.ITEM_CREATED, KafkaTopics.ITEM_UPDATED])
item_consumer.consume()