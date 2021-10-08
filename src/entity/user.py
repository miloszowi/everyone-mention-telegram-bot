from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class User:
    user_id: str
    username: str
    chats: List[str]

    collection: str = 'users'
    id_index: str = '_id'
    chats_index: str = 'chats'
    username_index: str = 'username'

    def is_in_chat(self, chat_id: str) -> bool:
        return chat_id in self.chats
    
    def add_to_chat(self, chat_id: str) -> None:
        self.chats.append(chat_id)

    def remove_from_chat(self, chat_id: str) -> None:
        if chat_id in self.chats:
            self.chats.remove(chat_id)

    def to_mongo_document(self) -> dict:
        return {
            self.username_index: self.username,
            self.chats_index: self.chats
        }
    
    @staticmethod
    def from_mongo_document(mongo_document: dict) -> User:
        return User(
            mongo_document[User.id_index],
            mongo_document[User.username_index],
            mongo_document[User.chats_index]
        )
