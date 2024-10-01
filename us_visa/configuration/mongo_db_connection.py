import sys

from us_visa.exception import USvisaException
from us_visa.logger import logging

import os
from us_visa.constants import DATABASE_NAME
import pymongo
import certifi
from dotenv import load_dotenv

ca = certifi.where()

class MongoDBClient:
    client = None
    load_dotenv()

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv('MONGODB_URL')
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {os.getenv('MONGODB_URL')} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection succesfull")
        except Exception as e:
            raise USvisaException(e,sys)