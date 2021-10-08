from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from bot.handler.abstractHandler import AbstractHandler
from bot.message.messageData import MessageData
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
        self.bot_handler = CommandHandler(self.action, self.handle)
        self.user_repository = UserRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        try:
            message_data = MessageData.create_from_arguments(update, context)
        except Exception as e:
            return Replier.markdown(update, str(e))

        try:
            user = self.user_repository.get_by_id(message_data.user_id)

            if user.is_in_chat(message_data.chat_id):
                return Replier.markdown(update, Replier.interpolate(not_joined, message_data))

            user.add_to_chat(message_data.chat_id)
            self.user_repository.save(user)
        except NotFoundException:
            self.user_repository.save_by_message_data(message_data)

        Replier.markdown(update, Replier.interpolate(joined, message_data))
        Logger.action(message_data, self.action)
