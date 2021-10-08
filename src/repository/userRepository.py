from typing import Iterable

from bot.message.messageData import MessageData
from database.client import Client
from entity.user import User
from exception.notFoundException import NotFoundException


class UserRepository:
    client: Client

    def __init__(self) -> None:
        self.client = Client()

    def get_by_id(self, user_id: str) -> User:
        user = self.client.find_one(
            User.collection,
            {
                User.id_index: user_id
            }
        )

        if not user:
            raise NotFoundException(f'Could not find user with "{user_id}" id')

        return User(
            user[User.id_index],
            user[User.username_index],
            user[User.chats_index]
        )

    def get_by_id_and_chat_id(self, user_id: str, chat_id: str) -> User:
        user = self.get_by_id(user_id)

        if not user.is_in_chat(chat_id):
            raise NotFoundException

        return user

    def save(self, user: User) -> None:
        self.client.update_one(
            User.collection,
            {User.id_index: user.user_id},
            user.to_mongo_document()
        )

    def save_by_message_data(self, data: MessageData) -> None:
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
                    "$in": [chat_id]
                }
            }
        )

        for record in users:
            result.append(User.from_mongo_document(record))

        return result
