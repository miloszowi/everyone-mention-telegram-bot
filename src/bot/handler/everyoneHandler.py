from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from bot.handler.abstractHandler import AbstractHandler
from bot.message.messageData import MessageData
from bot.message.replier import Replier
from config.contents import mention_failed
from logger import Logger
from repository.userRepository import UserRepository
from utils.messageBuilder import MessageBuilder


class EveryoneHandler(AbstractHandler):
    bot_handler: CommandHandler
    user_repository: UserRepository
    action: str = 'everyone'

    def __init__(self) -> None:
        self.bot_handler = CommandHandler(self.action, self.handle)
        self.user_repository = UserRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        try:
            message_data = MessageData.create_from_arguments(update, context)
        except Exception as e:
            return Replier.markdown(update, str(e))
        
        users = self.user_repository.get_all_for_chat(message_data.chat_id)
        
        if users:
            Replier.markdown(update, MessageBuilder.mention_message(users))
            return Logger.action(message_data, self.action)

        Replier.markdown(update, mention_failed)
