from bot.message.inboundMessage import InboundMessage
from entity.user import User
from exception.notFoundException import NotFoundException
from repository.abstractRepository import AbstractRepository


class UserRepository(AbstractRepository):
    collection_name: str = 'users'

    def __init__(self):
        super().__init__()

    def provide(self, inbound: InboundMessage) -> User:
        user = User.from_inbound_message(inbound)

        try:
            entity = self.get(user.user_id)
            if entity != user:
                self.save(user)
        except NotFoundException:
            self.save(user)

        return user

    def get(self, user_id: str) -> User:
        user = self.database_client.find_one(
            self.collection_name,
            {
                User.mongo_user_id_index: user_id
            }
        )

        if not user:
            raise NotFoundException

        return User.from_mongo_document(user)

    def save(self, user: User) -> None:
        self.database_client.save(
            self.collection_name,
            {User.mongo_user_id_index: user.user_id},
            user.to_mongo_document()
        )
