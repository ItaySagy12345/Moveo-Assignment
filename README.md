# Moveo Assignment

## Overview

This project is an API with the ability to create, update, list and delete items.
It was built with **FastAPI**, **PostgreSQL**, **Kafka**, and **Docker**. 

### Key Components
- **FastAPI**: Used to build the backend API.
- **PostgreSQL**: Relational database for storing item data.
- **Kafka**: Message broker to handle asynchronous communication.
- **Kafka Producer**: Publishes item-related events to Kafka topics for consumers to subscribe to.
- **Kafka Consumer**: Subscribes to the Producers' published events.
- **Docker**: Containerization tool to make the application environment portable.
- **PgAdmin**: Provides a UI for managing the PostgreSQL database.

## Architecture Overview

This project follows an event-driven architecture with Kafka to facilitate communication between services. The core flow is as follows:

1. The user sends a request to an API endpoint (only create_item and update_item endpoints publish their events to Kafka).
2. The server processes the request, interacts with the PostgreSQL database, and publishes a message to Kafka if applicable.
3. The Kafka Consumer listens to create and update topics and processes the events asynchronously.
4. All services (API, Kafka, PostgreSQL) are containerized using Docker.

A look into the docker-compose process (docker-compose up --build):

1. Builds custom image(s) and pulls official images from Docker Hub.
2. Starts up 6 containers using 5 images.
    1. Server: the FastAPi instance - based on the custom image created by the Dockerfile in this directory.
    2. Database: the Postgres instance - based on the official Postgres Docker Hub image.
    3. Pgadmin: a GUI for Postgres - based on the official pgadmin Docker Hub image.
    4. Kafka: event streaming service for event-driven design - based on the official Kafka Docker Hub image.
    5. Kafka-setup: Kafka dependency that creates the relevant topics - based on the official Kafka Docker Hub image.
    6. Zookeeper: Kafka dependency - based on the official Zookeeper Docker Hub image.
3. Automatically applies the db migration to the postgres container (using Alembic).
4. Creates the relevant Kafka topics.

## Setup Instructions

Follow the steps below to set up the application locally.

### Prerequisites

- Docker Desktop: https://www.docker.com/products/docker-desktop/

### Steps to Setup

1. **Clone the Repository:**

   ```bash
   git clone git@github.com:ItaySagy12345/Moveo-Assignment.git
   cd <project_name>

2. **Initialize Containerized Application:**
    - This will also pull all of the necessary images from Docker Hub (using the --build tag).

    ```bash
    docker-compose up --build

3. **Test the Application:**
    - Navigate to http://localhost:8000/docs. This will open the FastAPI Swagger UI for seamless API usage.
    - Navigate to http://localhost:8080. This will open the Pgadmin GUI for easy DB access.
    - use Docker Desktop to check logs in running containers to see general API and Kafka pub/sub activity. 
