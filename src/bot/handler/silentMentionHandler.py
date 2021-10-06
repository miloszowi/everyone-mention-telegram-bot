from typing import Iterable

from entity.user import User
from logger import Logger
from telegram.ext.commandhandler import CommandHandler

from bot.handler.abstractHandler import AbstractHandler
from bot.handler.mentionHandler import MentionHandler
from bot.message.messageData import MessageData


class MentionHandler(MentionHandler, AbstractHandler):
    def __init__(self) -> None:
        super().__init__()
        self.bot_handler = CommandHandler('silent', self.handle)

    def build_mention_message(self, users: Iterable[User]) -> str:
        return ' '.join([user.username for user in users])

    def log_action(self, message_data: MessageData) -> None:
        Logger.info(f'User {message_data.username} called /silent for {message_data.chat_id}')
