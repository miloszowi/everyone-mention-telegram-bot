from typing import Iterable, Optional

from database.client import Client
from entity.user import User
from exception.notFoundException import NotFoundException
from handler.vo.updateData import UpdateData


class UserRepository():
    client: Client

    def __init__(self) -> None:
        self.client = Client()

    def get_by_id(self, id: str) -> User:
        user = self.client.find_one(
            User.collection,
            {
                User.id_index: id
            }
        )

        if not user:
            raise NotFoundException(f'Could not find user with "{id}" id')

        return User(
            user[User.id_index],
            user[User.username_index],
            user[User.chats_index]
        )
        
    def save(self, user: User) -> None:
        self.client.update_one(
            User.collection,
            { User.id_index: user.user_id },
            user.to_mongo_document()
        )

    def save_by_update_data(self, data: UpdateData) -> None:
        self.client.insert_one(
            User.collection, 
            {
                User.id_index: data.user_id,
                User.username_index: data.username,
                User.chats_index: [data.chat_id]
            }
        )
    
    def get_all_for_chat(self, chat_id: str) -> Iterable[User]:
        result = []
        users = self.client.find_many(
            User.collection,
            {
                User.chats_index: {
                    "$in" : [chat_id]
                }
            }
        )
        
        for record in users:
            result.append(User.from_mongo_document(record))

        return result
