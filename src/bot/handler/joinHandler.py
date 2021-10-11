from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from bot.handler.abstractHandler import AbstractHandler
from bot.message.replier import Replier
from config.contents import joined, not_joined
from exception.notFoundException import NotFoundException
from logger import Logger
from repository.userRepository import UserRepository


class JoinHandler(AbstractHandler):
    bot_handler: CommandHandler
    user_repository: UserRepository
    action: str = 'join'

    def __init__(self) -> None:
        self.bot_handler = CommandHandler(self.action, self.wrap)
        self.user_repository = UserRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        try:
            user = self.user_repository.get_by_id(self.inbound.user_id)

            if user.is_in_chat(self.inbound.chat_id):
                return Replier.markdown(update, Replier.interpolate(not_joined, self.inbound))

            user.add_to_chat(self.inbound.chat_id)
            self.user_repository.save(user)
        except NotFoundException:
            self.user_repository.save_by_inbound_message(self.inbound)

        Replier.markdown(update, Replier.interpolate(joined, self.inbound))
        Logger.action(self.inbound, self.action)
