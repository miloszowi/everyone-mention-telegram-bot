from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from bot.handler.abstractHandler import AbstractHandler
from bot.message.messageData import MessageData
from bot.message.replier import Replier
from config.contents import start_text
from logger import Logger


class StartHandler(AbstractHandler):
    bot_handler: CommandHandler
    action: str = 'start'

    def __init__(self) -> None:
        self.bot_handler = CommandHandler(self.action, self.handle)

    def handle(self, update: Update, context: CallbackContext) -> None:
        try:
            MessageData.create_from_arguments(update, context)
        except Exception as e:
            return Replier.markdown(update, str(e))
        Replier.markdown(update, start_text)
        Logger.action(MessageData.create_from_arguments(update, context), self.action)
