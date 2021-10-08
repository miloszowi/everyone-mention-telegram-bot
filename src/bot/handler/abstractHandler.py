from abc import abstractmethod

from telegram.ext import Handler
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update


class AbstractHandler:
    bot_handler: Handler

    @abstractmethod
    def handle(self, update: Update, context: CallbackContext) -> None:
        raise Exception('handle method is not implemented')
