from abc import abstractmethod

from bot.message.messageData import MessageData
from logger import Logger
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.handler import Handler
from telegram.update import Update
from telegram.utils.helpers import mention_markdown


class AbstractHandler: 
    @abstractmethod
    def get_bot_handler(self) -> Handler: raise Exception('get_bot_handler method is not implemented')

    @abstractmethod
    def handle(self, update: Update, context: CallbackContext) -> None: raise Exception('handle method is not implemented')

    @abstractmethod
    def log_action(self, message_data: MessageData) -> None: raise Exception('log_action method is not implemented')

    def interpolate_reply(self, reply: str, message_data: MessageData):
        return reply.format(
            mention_markdown(message_data.user_id, message_data.username),
            message_data.group_name
        )

    def reply_markdown(self, update: Update, message: str) -> None:
        try:
            update.effective_message.reply_markdown_v2(text=message)
        except Exception as err:
            Logger.error(str(err))

    def reply_html(self, update: Update, html: str) -> None:
        try:
            update.effective_message.reply_html(text=html)
        except Exception as err:
            Logger.error(str(err))
