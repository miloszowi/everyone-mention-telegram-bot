from __future__ import annotations
from typing import Optional


class ChatPerson():
    chat_id: str
    person_id: str

    def __init__(self, chatId: str, personId: str) -> None:
        self.chat_id = chatId
        self.person_id = personId

    def getChatId(self) -> str:
        return self.chat_id

    def getPersonId(self) -> str:
        return self.person_id

    def toDict(self) -> dict:
        return {
            '_id': f'{self.chat_id}-{self.person_id}',
            'chat_id': self.chat_id,
            'person_id': self.person_id
        }

    @staticmethod
    def getMongoRoot() -> str:
        return 'chat_person'
    
    @staticmethod
    def fromDocument(document: Optional[dict]) -> Optional[ChatPerson]:
        if not document:
            return None
        return ChatPerson(document['chat_id'], document['person_id'])