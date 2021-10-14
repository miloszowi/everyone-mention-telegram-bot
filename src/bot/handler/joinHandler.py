from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from bot.handler.abstractHandler import AbstractHandler
from bot.message.replier import Replier
from config.contents import joined, not_joined
from exception.invalidActionException import InvalidActionException
from repository.chatRepository import ChatRepository
from repository.userRepository import UserRepository


class JoinHandler(AbstractHandler):
    bot_handler: CommandHandler
    user_repository: UserRepository
    action: str = 'join'

    def __init__(self) -> None:
        self.bot_handler = CommandHandler(self.action, self.wrap)
        self.user_repository = UserRepository()
        self.chat_repository = ChatRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        user = self.user_repository.provide(self.inbound)
        chat = self.chat_repository.provide(self.inbound)
        users = chat.groups.get(self.inbound.group_name)

        if user.user_id in users:
            raise InvalidActionException(Replier.interpolate(not_joined, self.inbound))

        users.append(user.user_id)
        self.chat_repository.save(chat)

        Replier.markdown(update, Replier.interpolate(joined, self.inbound))
