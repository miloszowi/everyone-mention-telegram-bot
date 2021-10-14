from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from bot.message.inboundMessage import InboundMessage


@dataclass
class Chat:
    chat_id: str
    groups: dict

    mongo_chat_id_index: str = '_id'
    mongo_groups_index: str = 'groups'

    def to_mongo_document(self) -> dict:
        return {
            self.mongo_chat_id_index: self.chat_id,
            self.mongo_groups_index: self.groups
        }

    @staticmethod
    def from_mongo_document(mongo_document: dict) -> Chat:
        return Chat(
            mongo_document[Chat.mongo_chat_id_index],
            mongo_document[Chat.mongo_groups_index]
        )

    @staticmethod
    def from_inbound_message(inbound: InboundMessage) -> Chat:
        return Chat(inbound.chat_id, {inbound.group_name: []})
