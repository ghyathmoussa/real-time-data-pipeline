import json
from typing import List
from kafka import KafkaProducer, KafkaConsumer
from aiokafka import AIOKafkaConsumer
import socket

class KafkaClient:
    def __init__(self, loop, bootstrap_servers: List[str]):
        self.loop = loop
        self.KAFKA_SERVERS = bootstrap_servers
        self.client_id = socket.gethostname()
        self.value_serializer = lambda v: json.dumps(v).encode('utf-8')
        self.value_deserializer = lambda v: json.loads(v.decode('utf-8'))
        self.compression_type = "gzip"
    
    def get_value_serializer(self):
        return self.value_serializer
    
    def get_value_deserializer(self):
        return self.value_deserializer
    
    def get_compression_type(self):
        return self.compression_type
    
    def get_client_id(self):
        return self.client_id
    
    def get_group_id(self):
        return "default"
    
    def build_producer_config(self, **kwargs):
        return {
            "bootstrap_servers": kwargs.get("bootstrap_servers", self.KAFKA_SERVERS),
            "value_serializer": kwargs.get("value_serializer", self.get_value_serializer()),
            "compression_type": kwargs.get("compression_type", self.get_compression_type()),
            "ack": "all"
        }
    
    def build_consumer_config(self, **kwargs):
        return {
            "bootstrap_servers": kwargs.get("bootstrap_servers", self.KAFKA_SERVERS),
            "value_deserializer": kwargs.get("value_deserializer", self.get_value_deserializer()),
            "client_id": kwargs.get("client_id", self.get_client_id()),
            "group_id": kwargs.get("group_id", self.get_group_id())
        }
     # For AIO Kafka   
    def create_task(self, coro):
        print(f"Creating task {coro}")
        r = self.loop.create_task(coro)
        print(f"Created task {r}:{coro}")
    
    def get_aio_consumer(self, topic, **kwargs):
        conf = self.build_consumer_config(**kwargs)
        consumer = AIOKafkaConsumer(topic, **conf)
        return consumer

    def get_consumer(self, topic, **kwargs):
        conf = self.build_consumer_config(**kwargs)
        consumer = KafkaConsumer(topic, **conf)
        return consumer
    
    def get_producer(self, **kwargs):
        conf = self.build_producer_config(**kwargs)
        producer = KafkaProducer(**conf)
        return producer
        
    # For AIO Kafka
    async def consume_aio_topic(self, topic, group_id, consumer=None, callback=None, option=None):
        if consumer is None:
            consumer = self.get_consumer(topic, group_id=group_id)
        if callback is None:
            callback = print("No callback function")
        try:
            print(f"starting consumer for topic {topic}")
            await consumer.start()
            async for msg in consumer:
                if callback:
                    self.create_task(callback(msg))
                else:
                    print(f"consumed from {topic}: {msg}")
                # await consumer.commit(msg.offset)

        except Exception as ex:
            print(f"consume_topic:{ex}")

        finally:
            print(f"stopping consumer for topic {topic}")
            await consumer.stop()
    ## Use this function just for AIOKafka
    def consumer_topic(self, topic, group_id, consumer=None):
        if consumer is None:
            consumer = self.get_consumer(topic=topic, group_id=group_id)
        
        consumer.subscribe(topic)
        msg = consumer.poll(timeout_ms=3.0)
        if not msg:
            return None
        if msg.error():
            raise Exception(msg.error())
        
        val = msg.value().decode()
        return json.loads(val)

        
        
        