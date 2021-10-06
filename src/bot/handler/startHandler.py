from config.contents import start_text
from logger import Logger
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from bot.handler.abstractHandler import AbstractHandler
from bot.message.messageData import MessageData


class StartHandler(AbstractHandler):
    bot_handler: CommandHandler

    def __init__(self) -> None:
        self.bot_handler = CommandHandler('start', self.handle)

    def handle(self, update: Update, context: CallbackContext) -> None:
        self.reply_markdown(update, start_text)
        self.log_action(MessageData.create_from_arguments(update, context))

    def get_bot_handler(self) -> CommandHandler:
        return self.bot_handler

    def log_action(self, message_data: MessageData) -> None:
        Logger.info(f'User {message_data.username} called /start for {message_data.chat_id}')
