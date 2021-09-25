from abc import abstractmethod
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.handler import Handler
from telegram.update import Update


class HandlerInterface: 
    def __init__(self) -> None:
        pass

    @abstractmethod
    def getBotHandler(self) -> Handler: raise Exception('getBotHandler method is not implemented')

    @abstractmethod
    def handle(self, update: Update, context: CallbackContext) -> None: raise Exception('handle method is not implemented')

    @abstractmethod
    def getCommandName(self) -> str: raise Exception('getCommandName method is not implemented')

    def reply(self, update: Update, message: str) -> None:
        update.effective_message.reply_markdown_v2(text=message)
