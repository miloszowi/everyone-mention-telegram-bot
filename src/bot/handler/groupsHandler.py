from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from bot.handler.abstractHandler import AbstractHandler
from bot.message.replier import Replier
from config.contents import no_groups
from exception.invalidActionException import InvalidActionException
from exception.notFoundException import NotFoundException
from repository.chatRepository import ChatRepository
from utils.messageBuilder import MessageBuilder


class GroupsHandler(AbstractHandler):
    bot_handler: CommandHandler
    chat_repository: ChatRepository
    action: str = 'groups'

    def __init__(self) -> None:
        self.bot_handler = CommandHandler(self.action, self.wrap)
        self.chat_repository = ChatRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        try:
            chat = self.chat_repository.get(self.inbound.chat_id)
            if not chat.groups:
                raise NotFoundException

            Replier.html(update, MessageBuilder.group_message(chat.groups))
        except NotFoundException:
            raise InvalidActionException(no_groups)

    def is_group_specific(self) -> bool:
        return False
