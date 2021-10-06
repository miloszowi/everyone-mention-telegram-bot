from bot.handler.abstractHandler import AbstractHandler
from bot.message.messageData import MessageData
from config.contents import left, not_left
from exception.invalidArgumentException import InvalidArgumentException
from exception.notFoundException import NotFoundException
from logger import Logger
from repository.userRepository import UserRepository
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update


class LeaveHandler(AbstractHandler):
    bot_handler: CommandHandler
    user_repository: UserRepository

    def __init__(self) -> None:
        self.bot_handler = CommandHandler('leave', self.handle)
        self.user_repository = UserRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        try:
            message_data = MessageData.create_from_arguments(update, context)
        except InvalidArgumentException as e:
            return self.reply_markdown(update, str(e))

        try:
            user = self.user_repository.get_by_id(message_data.user_id)

            if not user.is_in_chat(message_data.chat_id):
                raise NotFoundException()
        except NotFoundException:
            return self.reply_markdown(update, self.interpolate_reply(not_left, message_data))

        user.remove_from_chat(message_data.chat_id)
        self.user_repository.save(user)

        self.reply_markdown(update, self.interpolate_reply(left, message_data))
        self.log_action(message_data)

    def get_bot_handler(self) -> CommandHandler:
        return self.bot_handler

    def log_action(self, message_data: MessageData) -> None:
        Logger.info(f'User {message_data.username} left {message_data.chat_id}')
