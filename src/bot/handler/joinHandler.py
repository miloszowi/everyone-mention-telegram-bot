from telegram.utils.helpers import mention_markdown
from bot.handler.abstractHandler import AbstractHandler
from bot.message.messageData import MessageData
from config.contents import joined, not_joined
from exception.invalidArgumentException import InvalidArgumentException
from exception.notFoundException import NotFoundException
from logger import Logger
from repository.userRepository import UserRepository
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update


class JoinHandler(AbstractHandler):
    bot_handler: CommandHandler
    user_repository: UserRepository

    def __init__(self) -> None:
        self.bot_handler = CommandHandler('join', self.handle)
        self.user_repository = UserRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        try:
            message_data = MessageData.create_from_arguments(update, context)
        except InvalidArgumentException as e:
            return self.reply_markdown(update, str(e))

        try:
            user = self.user_repository.get_by_id(message_data.user_id)

            if user.is_in_chat(message_data.chat_id):
                return self.reply_markdown(update, self.interpolate_reply(not_joined, message_data))

            user.add_to_chat(message_data.chat_id)
            self.user_repository.save(user)
        except NotFoundException:
            self.user_repository.save_by_message_data(message_data)

        self.reply_markdown(update, self.interpolate_reply(joined, message_data))
        self.log_action(message_data)

    def get_bot_handler(self) -> CommandHandler:
        return self.bot_handler

    def log_action(self, message_data: MessageData) -> None:
        Logger.info(f'User {message_data.username} joined {message_data.chat_id}')
