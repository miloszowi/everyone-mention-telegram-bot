from typing import Iterable

from bot.message.inboundMessage import InboundMessage
from entity.chat import Chat
from entity.user import User
from exception.notFoundException import NotFoundException
from repository.abstractRepository import AbstractRepository
from repository.userRepository import UserRepository


class ChatRepository(AbstractRepository):
    collection_name: str = 'chats'
    user_repository: UserRepository
    
    def __init__(self):
        super().__init__()
        self.user_repository = UserRepository()

    def provide(self, inbound: InboundMessage) -> Chat:
        try:
            chat = self.get(inbound.chat_id)
            if not chat.groups.get(inbound.group_name):
                chat.groups[inbound.group_name] = []
        except NotFoundException:
            chat = Chat.from_inbound_message(inbound)

        return chat

    def get(self, chat_id: str) -> Chat:
        chat = self.database_client.find_one(
            self.collection_name,
            {
                Chat.mongo_chat_id_index: chat_id
            }
        )

        if not chat:
            raise NotFoundException

        return Chat.from_mongo_document(chat)

    def get_users_for_group(self, inbound: InboundMessage) -> Iterable[User]:
        chat = self.get(inbound.chat_id)
        if not chat.groups.get(inbound.group_name):
            raise NotFoundException

        users = [self.user_repository.get(user_id) for user_id in chat.groups.get(inbound.group_name) if user_id != inbound.user_id]

        if not users:
            raise NotFoundException

        return users

    def save(self, chat: Chat) -> None:
        self.database_client.save(
            self.collection_name,
            {Chat.mongo_chat_id_index: chat.chat_id},
            chat.to_mongo_document()
        )

