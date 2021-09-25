from database.databaseClient import DatabaseClient
from entities.chat import Chat
from typing import Optional

class ChatRepository:
    database: DatabaseClient

    def __init__(self) -> None:
        self.database = DatabaseClient()

    def get(self, id: str) -> Optional[Chat]:
        chat = Chat(id)
        search = self.database.findOne(Chat.getMongoRoot(), chat.toDict())
        
        return Chat.fromDocument(search)
        
    def save(self, chat: Chat) -> None:
        self.database.insert(Chat.getMongoRoot(), chat.toDict())