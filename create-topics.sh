#!/bin/bash

kafka-topics.sh --bootstrap-server kafka:9093 --create --topic item_created --partitions 3 --replication-factor 2
kafka-topics.sh --bootstrap-server kafka:9093 --create --topic item_updated --partitions 3 --replication-factor 2