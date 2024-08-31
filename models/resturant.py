## Insert a received message from kafka into Elasticsearch
## This project build as restaurant system
## The received messages will be treated as orders 
from datetime import datetime
from services.db import ElasticClient
from services.kafka import KafkaClient
from services.redis import RedisClient
from config import logger
from datetime import datetime


class StgRepository:
    def __init__(self, es_host):
        self.es_client = ElasticClient(host=es_host)
    
    def insert_event_order(self, object_id, object_type, sent_dttm, payload, es_index):
        obj = {
            "object_id": object_id,
            "object_type": object_type,
            "sent_dttm": sent_dttm,
            "payload": payload
        }
        self.es_client.insert(index=es_index, body=obj, id=object_id)
        return {
            "error": False,
            "message": "Order inserted successfully"
        }
    
class StgMessageProcessor:
    def __init__(self, **kwargs):
        self.topic = kwargs.get("topic")
        self.aio_consumer = KafkaClient().get_aio_consumer()
        self.consumer = KafkaClient().get_consumer(topic=self.topic)
        self.producer = KafkaClient().get_producer(topic= self.topic)
        self.redis = RedisClient()
        self.stg_repo = StgRepository()
        self.batch_size = kwargs.get("batch_size", 100)
        
    def run(self):
        logger.info(f"{datetime.utcnow()} START")
        for i in range(self.batch_size):
            msg = self.consumer.consume().value
            if not msg:
                continue
            
            self.stg_repo.insert_event_order(
                object_id=msg["object_id"],
                object_type=msg["object_type"],
                sent_dttm=msg["sent_dttm"],
                payload=msg["payload"]
            )
        dst_msg = self._construct_output_msg()
        self.producer.produce(topic=your_topic, msg=dst_msg)
    def _construct_output_msg(self, msg: dict):
        obj_id = msg["payload"]["object_name"]["id"]
        obj_data = self.redis.get(obj_id)
        obj_name = obj_data["name"]
        
        user_id = obj_data["payload"]["user"]["id"]
        user_data = self.redis.get(user_id)
        user_name = user_data["name"]
        user_login = user_data["login"]
        
        message = msg["payload"]
        ## Add waht you want from data
        return {
            "obj_id": msg["object_id"],
            "obj_type": msg["object_type"]
        }
        
        