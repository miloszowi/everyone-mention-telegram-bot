from urllib.parse import quote_plus

from config.credentials import (MONGODB_DATABASE, MONGODB_HOSTNAME,
                                MONGODB_PASSWORD, MONGODB_PORT,
                                MONGODB_USERNAME)
from pymongo import MongoClient
from pymongo.database import Database


class Client():
    mongo_client: MongoClient
    database: Database

    def __init__(self) -> None:
        uri = "mongodb://%s:%s@%s:%s/%s?authSource=admin" % (
            MONGODB_USERNAME, quote_plus(MONGODB_PASSWORD),
            MONGODB_HOSTNAME, MONGODB_PORT, MONGODB_DATABASE
        )

        self.mongo_client = MongoClient(uri)
        self.database = self.mongo_client[MONGODB_DATABASE]

    def insert_one(self, collection: str, data: dict) -> None:
        self.database.get_collection(collection).insert_one(data)

    def find_one(self, collection: str, query: dict) -> dict:
        return self.database.get_collection(collection).find_one(query)

    def find_many(self, collection: str, filter: dict) -> dict:
        return self.database.get_collection(collection).find(filter)

    def update_one(self, collection: str, filter: dict, data: dict) -> None:
        self.database.get_collection(collection).update_one(
            filter, 
            { "$set" : data }
        )

    def aggregate(self, collection, pipeline: list):
        return self.database.get_collection(collection).aggregate(pipeline)
