from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from bot.handler.abstractHandler import AbstractHandler
from bot.message.replier import Replier
from config.contents import mention_failed
from exception.invalidActionException import InvalidActionException
from exception.notFoundException import NotFoundException
from repository.chatRepository import ChatRepository
from utils.messageBuilder import MessageBuilder


class EveryoneHandler(AbstractHandler):
    bot_handler: CommandHandler
    chat_repository: ChatRepository
    action: str = 'everyone'

    def __init__(self) -> None:
        self.bot_handler = CommandHandler(self.action, self.wrap)
        self.chat_repository = ChatRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        try:
            users = self.chat_repository.get_users_for_group(self.inbound)

            Replier.markdown(update, MessageBuilder.mention_message(users))
        except NotFoundException as e:
            raise InvalidActionException(mention_failed) from e
