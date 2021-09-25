from __future__ import annotations

from typing import Iterable


class User():
    collection: str = 'users'
    idIndex: str = '_id'
    chatsIndex: str = 'chats'
    usernameIndex: str = 'username'

    userId: str
    username: str
    chats: Iterable[str]

    def __init__(self, userId, username, chats) -> None:
        self.userId = userId
        self.username = username
        self.chats = chats

    def getUserId(self) -> str:
        return self.userId

    def getUsername(self) -> str:
        return self.username

    def getChats(self) -> Iterable[str]:
        return self.chats

    def isInChat(self, chatId: str) -> bool:
        return chatId in self.getChats()
    
    def addToChat(self, chatId: str) -> None:
        self.chats.append(chatId)

    def removeFromChat(self, chatId: str) -> None:
        if chatId in self.getChats():
            self.chats.remove(chatId)

    def toMongoDocument(self) -> dict:
        return {
            self.usernameIndex: self.getUsername(),
            self.chatsIndex: self.getChats()
        }
    
    @staticmethod
    def fromMongoDocument(mongoDocument: dict) -> User:
        return User(
            mongoDocument[User.idIndex],
            mongoDocument[User.usernameIndex],
            mongoDocument[User.chatsIndex]
        )
