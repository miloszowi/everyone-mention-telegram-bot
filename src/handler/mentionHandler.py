from typing import Iterable

from config.contents import mention_failed
from entity.user import User
from exception.invalidArgumentException import InvalidArgumentException
from repository.userRepository import UserRepository
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from handler.abstractHandler import AbstractHandler


class MentionHandler(AbstractHandler):
    bot_handler: CommandHandler
    user_repository: UserRepository

    def __init__(self) -> None:
        self.bot_handler = CommandHandler('everyone', self.handle)
        self.user_repository = UserRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        try:
            updateData = self.get_update_data(update, context)
        except InvalidArgumentException as e:
            return self.reply_markdown(update, str(e))
        
        users = self.user_repository.get_all_for_chat(updateData.chat_id)
        
        if users:
            return self.reply_markdown(update, self.build_mention_message(users))

        self.reply_markdown(update, mention_failed)

    def get_bot_handler(self) -> CommandHandler:
        return self.bot_handler

    def build_mention_message(self, users: Iterable[User]) -> str:
        result = ''

        for user in users:
            result += f'*[{user.username}](tg://user?id={user.user_id})* '

        return result
