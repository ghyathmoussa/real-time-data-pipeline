import json
import redis
from typing import Dict

class RedisClient:
    def __init__(self, host: str, port: int, password: str):
        self.redis_client = redis.StrictRedis(
            host=host,
            port=port,
            password=password,
            ssl=False,
        )
    
    def set(self, key, value):
        self.redis_client.set(k, json.dump(value))
    
    def get(self, key):
        return json.loads(self.redis_client.get(key))

