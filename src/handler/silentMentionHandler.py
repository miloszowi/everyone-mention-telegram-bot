from typing import Iterable

from entity.user import User
from telegram.ext.commandhandler import CommandHandler

from handler.abstractHandler import AbstractHandler
from handler.mentionHandler import MentionHandler


class MentionHandler(MentionHandler, AbstractHandler):
    def __init__(self) -> None:
        super().__init__()
        self.bot_handler = CommandHandler('silent', self.handle)

    def build_mention_message(self, users: Iterable[User]) -> str:
        result = ''

        for user in users:
            result += f'*{user.username}\({user.user_id}\)*\n'

        return result
