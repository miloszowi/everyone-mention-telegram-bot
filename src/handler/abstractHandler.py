from abc import abstractmethod

from logger import Logger
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.handler import Handler
from telegram.update import Update

from handler.vo.updateData import UpdateData


class AbstractHandler: 
    @abstractmethod
    def get_bot_handler(self) -> Handler: raise Exception('get_bot_handler method is not implemented')

    @abstractmethod
    def handle(self, update: Update, context: CallbackContext) -> None: raise Exception('handle method is not implemented')

    @abstractmethod
    def log_action(self, update_data: UpdateData) -> None: raise Exception('log_action method is not implemented')

    def get_update_data(self, update: Update, context: CallbackContext) -> UpdateData:
        return UpdateData.create_from_arguments(update, context)

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
