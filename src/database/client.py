from __future__ import annotations
from pymongo import MongoClient
from pymongo.database import Database

from config.envs import MONGO_CONNECTION_STRING, MONGO_DATABASE
from decorators.singleton import Singleton


class Client(metaclass=Singleton):
    mongo_client: MongoClient
    database: Database

    # allow only 10 minutes on idle, close connection after
    max_idle_time: int = 10 * (60 * 1000)

    def __init__(self) -> None:
        self.mongo_client = MongoClient(
            MONGO_CONNECTION_STRING,
            connect=False,
            maxIdleTimeMS=self.max_idle_time
        )
        self.database = self.mongo_client[MONGO_DATABASE]

    def insert_one(self, collection: str, data: dict) -> None:
        self.database.get_collection(collection).insert_one(data)

    def find_one(self, collection: str, query: dict) -> dict:
        return self.database.get_collection(collection).find_one(query)

    def find_many(self, collection: str, filter: dict) -> dict:
        return self.database.get_collection(collection).find(filter)

    def update_one(self, collection: str, filter: dict, data: dict) -> None:
        self.database.get_collection(collection).update_one(
            filter, 
            {"$set": data}
        )

    def aggregate(self, collection, pipeline: list):
        return self.database.get_collection(collection).aggregate(pipeline)
