from config.contents import start_text
from logger import Logger
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from handler.abstractHandler import AbstractHandler
from handler.vo.updateData import UpdateData


class StartHandler(AbstractHandler):
    bot_handler: CommandHandler

    def __init__(self) -> None:
        self.bot_handler = CommandHandler('start', self.handle)

    def handle(self, update: Update, context: CallbackContext) -> None:
        self.reply_markdown(update, start_text)
        self.log_action(UpdateData.create_from_arguments(update, context))

    def get_bot_handler(self) -> CommandHandler:
        return self.bot_handler

    def log_action(self, update_data: UpdateData) -> None:
        Logger.info(f'User {update_data.username} called /start for {update_data.chat_id}')
