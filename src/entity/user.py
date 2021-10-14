from __future__ import annotations

from dataclasses import dataclass

from bot.message.inboundMessage import InboundMessage


@dataclass
class User:
    user_id: str
    username: str

    mongo_user_id_index: str = '_id'
    mongo_username_index: str = 'username'

    def to_mongo_document(self) -> dict:
        return {
            self.mongo_user_id_index: self.user_id,
            self.mongo_username_index: self.username
        }
    
    @staticmethod
    def from_mongo_document(mongo_document: dict) -> User:
        return User(
            mongo_document[User.mongo_user_id_index],
            mongo_document[User.mongo_username_index]
        )

    @staticmethod
    def from_inbound_message(inbound: InboundMessage) -> User:
        return User(inbound.user_id, inbound.username)
