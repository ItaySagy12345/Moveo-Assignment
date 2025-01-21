FROM python:3.10-slim

# Install netcat for proper connection to postgres service
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

# Default fallback command if something goes wrong with command in docker-compose.yml 
CMD ["uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "8000"]