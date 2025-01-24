import threading
from fastapi import FastAPI
from src.routes.items_routes import items_router
from src.kafka.consumer import KafkaConsumer
from src.kafka.topics import KafkaTopics
from src.utils.logger import logger
from contextlib import asynccontextmanager

app = FastAPI()

app.include_router(items_router, prefix="/api")

def start_kafka_consumers():
    """
    Starts the Kafka consumer
    """

    item_consumer = KafkaConsumer(name='item_consumer')
    item_consumer.subscribe([KafkaTopics.ITEM_CREATED, KafkaTopics.ITEM_UPDATED])
    item_consumer.consume()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Starts the server and Kafka consumer in separate threads
    """

    logger.info("Initializing Kafka consumers")
    consumer_thread = threading.Thread(target=start_kafka_consumers, daemon=True)
    consumer_thread.start()

    yield

    logger.info("Shutting down FastAPI server")


app = FastAPI(lifespan=lifespan)