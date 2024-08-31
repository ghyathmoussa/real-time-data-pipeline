# This file to get all configs of your app
import logging
from pathlib import Path
import os
import json


PROJECT_DIR = Path(__file__).parent

class Config:
    def __init__(self, **kwargs):
        pass
    
    def get_kafka_host(self,):
        return os.getenv("KAFKA_HOST").split(",")

    def get_redis_config(self,):
        return {
            "url": os.getenv("REDIS_HOST"),
            "username": os.getenv("REDIS_USERNAME"),
            "password": os.getenv("REDIS_PASSWORD")
        }

    def get_es_config(self,):
        return {
            "url": os.getenv("ES_HOST"),
            "username": os.getenv("ES_USERNAME"),
            "password": os.getenv("ES_PASSWORD")
        }
# Logger Config
LOG_DIR = PROJECT_DIR  /  "logs"
LOG_LEVEL = 'INFO'

logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
formatter = logging.Formatter(
    '[%(asctime)s] %(levelname)s [%(funcName)s():%(lineno)s] [%(process)d-%(thread)d] %(message)s')

file_handler = logging.FileHandler(LOG_DIR / "event_logs.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


