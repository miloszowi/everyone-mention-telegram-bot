from typing import Iterable

from telegram.utils.helpers import mention_markdown

from bot.handler.abstractHandler import AbstractHandler
from bot.message.messageData import MessageData
from config.contents import mention_failed
from entity.user import User
from exception.invalidArgumentException import InvalidArgumentException
from logger import Logger
from repository.userRepository import UserRepository
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update


class MentionHandler(AbstractHandler):
    bot_handler: CommandHandler
    user_repository: UserRepository

    def __init__(self) -> None:
        self.bot_handler = CommandHandler('everyone', self.handle)
        self.user_repository = UserRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        try:
            message_data = MessageData.create_from_arguments(update, context)
        except InvalidArgumentException as e:
            return self.reply_markdown(update, str(e))
        
        users = self.user_repository.get_all_for_chat(message_data.chat_id)
        
        if users:
            self.reply_markdown(update, self.build_mention_message(users))
            return self.log_action(message_data)

        self.reply_markdown(update, mention_failed)

    def get_bot_handler(self) -> CommandHandler:
        return self.bot_handler

    def log_action(self, message_data: MessageData) -> None:
        Logger.info(f'User {message_data.username} called /everyone for {message_data.chat_id}')

    def build_mention_message(self, users: Iterable[User]) -> str:
        return ' '.join([mention_markdown(user.user_id, user.username) for user in users])

