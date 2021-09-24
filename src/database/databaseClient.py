from pymongo.errors import ServerSelectionTimeoutError
from config.credentials import MONGODB_USERNAME, MONGODB_PASSWORD, MONGODB_DATABASE, MONGODB_HOSTNAME, MONGODB_PORT
from pymongo import MongoClient
from pymongo.database import Database
from urllib.parse import quote_plus

class DatabaseClient():
    mongoClient: MongoClient
    database: Database

    def __init__(self) -> None:
        uri = "mongodb://%s:%s@%s:%s/%s?authSource=admin" % (
            MONGODB_USERNAME, quote_plus(MONGODB_PASSWORD),
            MONGODB_HOSTNAME, MONGODB_PORT, MONGODB_DATABASE
        )

        self.mongoClient = MongoClient(uri)
        self.database = self.mongoClient[MONGODB_DATABASE]

    def insert(self, collection: str, data: dict) -> None:
        self.database.get_collection(collection).insert_one(data)

    def find(self, collection: str, query: dict) -> dict:
        return self.database.get_collection(collection).find(query)

    def findOne(self, collection: str, query: dict) -> dict:
        return self.database.get_collection(collection).find_one(query)

    def remove(self, collection: str, data: dict) -> None:
        self.database.get_collection(collection).remove(data)