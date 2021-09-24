from __future__ import annotations
from abc import abstractmethod
from typing import Optional
import names


class Person():
    id: str
    username: str

    def __init__(self, id: str, username: Optional[str] = None) -> None:
        self.id = id
        
        if not username:
            self.username = names.get_first_name()
        else:
            self.username = username

    def getId(self) -> str:
        return self.id

    def getUsername(self) -> str:
        return self.username

    def toDict(self, withUsername: bool = True) -> dict:
        result = {
            '_id': self.id
        }

        if withUsername:
            result['username'] = self.username
        
        return result

    @staticmethod
    def getMongoRoot() -> str:
        return 'person'

    @staticmethod
    def fromDocument(document: Optional[dict]) -> Optional[Person]:
        if not document:
            return None

        return Person(document['_id'], document['username'])