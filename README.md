# Real Time Pipeline Template
This template allow you to create a pipeline that use Redis, Kafka, and Elasticsearch.

`Note: ` This is just a template you can modify it as your needs

## Prerequisites
- Docker
- python>=3.8

## Installation
- git clone https://github.com/ghyathmoussa/real-time-data-pipeline.git
- `cd build`
- run the scripts that create Kafka, Redis, and Kubernetes containers
- it is advanced to run kubernetes as a service not a container
### .env
```
PIPELINE_APP_NAME=
KAFKA_HOST=
KAFKA_PORT=
KAFKA_CONSUMER_GROUP=
KAFKA_SOURCE_TOPIC=
KAFKA_DESTINATION_TOPIC=
REDIS_HOST=
REDIS_PORT=
REDIS_PASSWORD=
ES_HOST=
ES_PORT=
ES_INDEX_NAME=
ES_USER=
ES_PASSWORD=
```

## Run
- Run `docker-compose up -d`
- go to `localhost:5544/docs`

