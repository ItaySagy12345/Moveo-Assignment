import threading
from fastapi import FastAPI
from src.kafka.admin import kafka_admin
from src.routes.home_route import home_router
from src.routes.items_routes import items_router
from src.kafka.consumer import KafkaConsumer
from src.kafka.utils.topics import KafkaTopics
from fastapi.staticfiles import StaticFiles


def initialize_item_consumer() -> None:
    """
    Initializes a KafkaConsumer instance and subscribes it to the relevant Kafka topics
    Return: None
    """

    item_consumer = KafkaConsumer(name='item_consumer')
    subscribe_topics = [KafkaTopics.ITEM_CREATED, KafkaTopics.ITEM_UPDATED]
    existing_topics: list[str] = kafka_admin.get_existing_topics()
    missing_topics: list[KafkaTopics] = [topic for topic in subscribe_topics if topic not in existing_topics]

    if missing_topics:
        kafka_admin.create_topic(topics=missing_topics)

    item_consumer.subscribe(topics=subscribe_topics)
    item_consumer.consume()


app = FastAPI()

app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(home_router)
app.include_router(items_router, prefix="/api")

threading.Thread(target=initialize_item_consumer, daemon=True).start()