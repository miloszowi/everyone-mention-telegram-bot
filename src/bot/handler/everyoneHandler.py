from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from bot.handler.abstractHandler import AbstractHandler
from bot.message.replier import Replier
from config.contents import mention_failed
from exception.notFoundException import NotFoundException
from logger import Logger
from repository.userRepository import UserRepository
from utils.messageBuilder import MessageBuilder


class EveryoneHandler(AbstractHandler):
    bot_handler: CommandHandler
    user_repository: UserRepository
    action: str = 'everyone'

    def __init__(self) -> None:
        self.bot_handler = CommandHandler(self.action, self.wrap)
        self.user_repository = UserRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        try:
            users = self.user_repository.get_all_for_chat(self.inbound.chat_id)

            Replier.markdown(update, MessageBuilder.mention_message(users))
            Logger.action(self.inbound, self.action)
        except NotFoundException:
            Replier.markdown(update, mention_failed)
