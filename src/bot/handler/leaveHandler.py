from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from bot.handler.abstractHandler import AbstractHandler
from bot.message.replier import Replier
from config.contents import left, not_left
from exception.notFoundException import NotFoundException
from logger import Logger
from repository.userRepository import UserRepository


class LeaveHandler(AbstractHandler):
    bot_handler: CommandHandler
    user_repository: UserRepository
    action: str = 'leave'

    def __init__(self) -> None:
        self.bot_handler = CommandHandler(self.action, self.wrap)
        self.user_repository = UserRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        try:
            user = self.user_repository.get_by_id_and_chat_id(self.inbound.user_id, self.inbound.chat_id)
            user.remove_from_chat(self.inbound.chat_id)
            self.user_repository.save(user)

            Replier.markdown(update, Replier.interpolate(left, self.inbound))
            Logger.action(self.inbound, self.action)
        except NotFoundException:
            return Replier.markdown(update, Replier.interpolate(not_left, self.inbound))
