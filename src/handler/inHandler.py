from config.contents import opted_in, opted_in_failed
from exception.invalidArgumentException import InvalidArgumentException
from exception.notFoundException import NotFoundException
from repository.userRepository import UserRepository
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from handler.abstractHandler import AbstractHandler


class InHandler(AbstractHandler):
    bot_handler: CommandHandler
    user_repository: UserRepository

    def __init__(self) -> None:
        self.bot_handler = CommandHandler('in', self.handle)
        self.user_repository = UserRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        try:
            update_data = self.get_update_data(update, context)
        except InvalidArgumentException as e:
            return self.reply_markdown(update, str(e))

        try:
            user = self.user_repository.get_by_id(update_data.user_id)

            if user.is_in_chat(update_data.chat_id):
                return self.reply_markdown(update, opted_in_failed)

            user.add_to_chat(update_data.chat_id)
            self.user_repository.save(user)
            
        except NotFoundException:
            self.user_repository.save_by_update_data(update_data)

        self.reply_markdown(update, opted_in)

    def get_bot_handler(self) -> CommandHandler:
        return self.bot_handler
