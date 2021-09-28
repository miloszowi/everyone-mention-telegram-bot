from config.contents import opted_off, opted_off_failed
from exception.notFoundException import NotFoundException
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
        updateData = self.get_update_data(update)

        try:
            user = self.user_repository.get_by_id(updateData.user_id)

            if not user.is_in_chat(updateData.chat_id):
                raise NotFoundException()
        except NotFoundException:
            self.reply(update, opted_off_failed)
            return

        user.remove_from_chat(updateData.chat_id)
        self.user_repository.save(user)

        self.reply(update, opted_off)

    def get_bot_handler(self) -> CommandHandler:
        return self.bot_handler
