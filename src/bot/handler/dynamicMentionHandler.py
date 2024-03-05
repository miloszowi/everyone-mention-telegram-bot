import re

from telegram.ext import Filters, MessageHandler
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update

from bot.handler.abstractHandler import AbstractHandler
from bot.message.replier import Replier
from repository.chatRepository import ChatRepository
from utils.messageBuilder import MessageBuilder


class DynamicMentionHandler(AbstractHandler):
    bot_handler: MessageHandler
    chat_repository: ChatRepository
    action: str = 'dynamic-mention'

    def __init__(self) -> None:
        self.bot_handler = MessageHandler(
            Filters.regex(re.compile(r'@[^ ]')),
            self.wrap
        )
        self.chat_repository = ChatRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        if hasattr(update, 'message_reaction'):
            return
        
        users = self.chat_repository.get_users_for_group(self.inbound)

        Replier.markdown(update, MessageBuilder.mention_message(users))
