from config.contents import opted_off, opted_off_failed
from exception.invalidArgumentException import InvalidArgumentException
from exception.notFoundException import NotFoundException
from handler.vo.updateData import UpdateData
from logger import Logger
from repository.userRepository import UserRepository
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from handler.abstractHandler import AbstractHandler


class OutHandler(AbstractHandler):
    bot_handler: CommandHandler
    user_repository: UserRepository

    def __init__(self) -> None:
        self.bot_handler = CommandHandler('out', self.handle)
        self.user_repository = UserRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        try:
            update_data = self.get_update_data(update, context)
        except InvalidArgumentException as e:
            return self.reply_markdown(update, str(e))

        try:
            user = self.user_repository.get_by_id(update_data.user_id)

            if not user.is_in_chat(update_data.chat_id):
                raise NotFoundException()
        except NotFoundException:
            return self.reply_markdown(update, opted_off_failed)

        user.remove_from_chat(update_data.chat_id)
        self.user_repository.save(user)

        self.reply_markdown(update, opted_off)
        self.log_action(update_data)

    def get_bot_handler(self) -> CommandHandler:
        return self.bot_handler

    def log_action(self, update_data: UpdateData) -> None:
        Logger.info(f'User {update_data.username} left {update_data.chat_id}')
