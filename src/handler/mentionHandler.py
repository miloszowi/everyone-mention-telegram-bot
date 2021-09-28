from typing import Iterable

from config.contents import mention_failed
from entity.user import User
from repository.userRepository import UserRepository
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from handler.abstractHandler import AbstractHandler


class MentionHandler(AbstractHandler):
    bot_handler: CommandHandler
    user_repository: UserRepository
    silent: str = 'silent'

    def __init__(self) -> None:
        self.bot_handler = CommandHandler('everyone', self.handle)
        self.user_repository = UserRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        updateData = self.get_update_data(update)
        users = self.user_repository.get_all_for_chat(updateData.chat_id)
        
        if users:
            self.reply(update, self.build_mention_message(users, self.isSilent(context)))
            return

        self.reply(update, mention_failed)

    def get_bot_handler(self) -> CommandHandler:
        return self.bot_handler

    def build_mention_message(self, users: Iterable[User], silent: bool = False) -> str:
        result = ''

        for user in users:
            if not silent:
                result += f'*[{user.username}](tg://user?id={user.user_id})* '
            else:
                result += f'*{user.username}\({user.user_id}\)*\n'

        return result

    def isSilent(self, context: CallbackContext) -> bool:
        return self.silent in context.args