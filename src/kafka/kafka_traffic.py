# import os
# from typing import Any
# from confluent_kafka import Producer


# kafka_bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9093")
# print(kafka_bootstrap_servers)
# producer = Producer({
#     'bootstrap.servers': kafka_bootstrap_servers,
# })

# def kafka_report(error: Any, message: Any) -> None:
#     """
#     Prints the status of Kafka messages
#     Param: error [Any]: The error if there is one
#     Param: message [Any]: The message
#     Return None
#     """

#     if error is not None:
#         print(f"Message delivery failed: {error}")
#     else:
#         print(f"Message delivered to {message.topic()} [{message.partition()}]")