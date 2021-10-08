from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from bot.handler.abstractHandler import AbstractHandler
from bot.message.messageData import MessageData
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
        self.bot_handler = CommandHandler(self.action, self.handle)
        self.user_repository = UserRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        try:
            message_data = MessageData.create_from_arguments(update, context)
        except Exception as e:
            return Replier.markdown(update, str(e))

        try:
            user = self.user_repository.get_by_id_and_chat_id(message_data.user_id, message_data.chat_id)
            user.remove_from_chat(message_data.chat_id)
            self.user_repository.save(user)

            Replier.markdown(update, Replier.interpolate(left, message_data))
            Logger.action(message_data, self.action)
        except NotFoundException:
            return Replier.markdown(update, Replier.interpolate(not_left, message_data))
