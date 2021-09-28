from abc import abstractmethod

from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.handler import Handler
from telegram.update import Update

from handler.vo.updateData import UpdateData


class AbstractHandler: 
    @abstractmethod
    def get_bot_handler(self) -> Handler: raise Exception('get_bot_handler method is not implemented')

    @abstractmethod
    def handle(self, update: Update, context: CallbackContext) -> None: raise Exception('handle method is not implemented')

    def get_update_data(self, update: Update) -> UpdateData:
        return UpdateData.create_from_update(update)

    def reply(self, update: Update, message: str) -> None:
        update.effective_message.reply_markdown_v2(text=message)
