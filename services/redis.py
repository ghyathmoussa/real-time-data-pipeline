import json
import redis
from typing import Dict
from config import Config

class RedisClient:
    def __init__(self, **kwargs):
        self.config = Config()
        self.redis_client = redis.StrictRedis(
            host=kwargs.get("host", self.config.get_redis_config()["url"]),
            port=kwargs.get("host", self.config.get_redis_config()["port"]),
            password=kwargs.get("host", self.config.get_redis_config()["password"]),
            ssl=False,
        )
    
    def set(self, key, value):
        self.redis_client.set(key, json.dump(value))
    
    def get(self, key):
        return json.loads(self.redis_client.get(key))

