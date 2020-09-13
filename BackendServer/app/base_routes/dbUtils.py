from pymongo import MongoClient
from cryptography.fernet import Fernet
import os
import json


class DBUtils:
    def __init__(self):
        self.db_configs = {"LOCAL": {
            "user": "admin",
            "password": "admin", 
            "url": "localhost", 
            "port": "27017", 
            "auth_db": "admin"
        }}

    def get_db(self, machine, db_name):
        db_configs=self.db_configs
        config = db_configs[machine]
        # conn = "mongodb://" + config["user"] + ":" + config["password"] + "@" + config["url"] +\
        #        ":" + config["port"] + "/" + config["auth_db"]
        conn = "mongodb://" + config["url"] + ":" + config["port"] + "/" + config["auth_db"]
        client = MongoClient(conn)
        return client[db_name]

    def get_collection_obj(self, machine, db_name, collection_name):
        db = self.get_db(machine, db_name)
        return db[collection_name]