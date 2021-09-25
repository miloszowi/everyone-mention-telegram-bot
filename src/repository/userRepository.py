from typing import Iterable, Optional

from database.client import Client
from entity.user import User
from exception.notFoundException import NotFoundException
from handler.vo.updateData import UpdateData


class UserRepository():
    client: Client

    def __init__(self) -> None:
        self.client = Client()

    def getById(self, id: str) -> User:
        user = self.client.findOne(
            User.collection,
            {
                User.idIndex: id
            }
        )

        if not user:
            raise NotFoundException(f'Could not find user with "{id}" id')

        return User(
            user[User.idIndex],
            user[User.usernameIndex],
            user[User.chatsIndex]
        )
        
    def save(self, user: User) -> None:
        self.client.updateOne(
            User.collection,
            { User.idIndex: user.getUserId() },
            user.toMongoDocument()
        )

    def saveByUpdateData(self, data: UpdateData) -> None:
        self.client.insertOne(
            User.collection, 
            {
                User.idIndex: data.getUserId(),
                User.usernameIndex: data.getUsername(),
                User.chatsIndex: [data.getChatId()]
            }
        )
    
    def getAllForChat(self, chatId: str) -> Iterable[User]:
        result = []
        users = self.client.findMany(
            User.collection,
            {
                User.chatsIndex: {
                    "$in" : [chatId]
                }
            }
        )
        
        for record in users:
            result.append(User.fromMongoDocument(record))

        return result

    

