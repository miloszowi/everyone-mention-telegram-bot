from __future__ import annotations
from typing import Optional


class Chat():
    id: str

    def __init__(self, id: str) -> None:
        self.id = id

    def getId(self) -> str:
        return self.id

    def toDict(self) -> dict:
        return {
            '_id': self.id
        }
    
    @staticmethod
    def getMongoRoot() -> str:
        return 'chat'

    @staticmethod
    def fromDocument(document: Optional[dict]) -> Optional[Chat]:
        if not document:
            return None

        return Chat(document['_id'])