from abc import abstractmethod

from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.handler import Handler
from telegram.update import Update

from handler.vo.updateData import UpdateData


class AbstractHandler: 
    def __init__(self) -> None:
        pass

    @abstractmethod
    def getBotHandler(self) -> Handler: raise Exception('getBotHandler method is not implemented')

    @abstractmethod
    def handle(self, update: Update, context: CallbackContext) -> None: raise Exception('handle method is not implemented')

    def getUpdateData(self, update: Update) -> UpdateData:
        return UpdateData.createFromUpdate(update)

    def reply(self, update: Update, message: str) -> None:
        update.effective_message.reply_markdown_v2(text=message)
