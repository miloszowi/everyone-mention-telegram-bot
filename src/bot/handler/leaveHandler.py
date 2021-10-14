from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from bot.handler.abstractHandler import AbstractHandler
from bot.message.replier import Replier
from config.contents import left, not_left
from exception.invalidActionException import InvalidActionException
from repository.userRepository import UserRepository
from repository.chatRepository import ChatRepository


class LeaveHandler(AbstractHandler):
    bot_handler: CommandHandler
    user_repository: UserRepository
    chat_repository: ChatRepository
    action: str = 'leave'

    def __init__(self) -> None:
        self.bot_handler = CommandHandler(self.action, self.wrap)
        self.user_repository = UserRepository()
        self.chat_repository = ChatRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        user = self.user_repository.provide(self.inbound)
        chat = self.chat_repository.provide(self.inbound)
        group = chat.groups.get(self.inbound.group_name)

        if user.user_id not in group:
            raise InvalidActionException(Replier.interpolate(not_left, self.inbound))

        group.remove(user.user_id)
        if not group:
            chat.groups.pop(self.inbound.group_name)

        self.chat_repository.save(chat)

        Replier.markdown(update, Replier.interpolate(left, self.inbound))
