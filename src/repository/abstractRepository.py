from database.client import Client


class AbstractRepository:
    collection_name: str
    database_client: Client

    def __init__(self):
        self.database_client = Client()
