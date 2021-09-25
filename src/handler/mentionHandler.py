from typing import Iterable

from config.contents import mention_failed
from entity.user import User
from repository.userRepository import UserRepository
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from handler.abstractHandler import AbstractHandler


class MentionHandler(AbstractHandler):
    botHandler: CommandHandler
    userRepository: UserRepository
    silent: str = 'silent'

    def __init__(self) -> None:
        self.botHandler = CommandHandler('everyone', self.handle)
        self.userRepository = UserRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        updateData = self.getUpdateData(update)
        users = self.userRepository.getAllForChat(updateData.getChatId())
        
        if users:
            self.reply(update, self.buildMentionMessage(users, self.isSilent(context)))
            return

        self.reply(update, mention_failed)

    def getBotHandler(self) -> CommandHandler:
        return self.botHandler

    def buildMentionMessage(self, users: Iterable[User], silent: bool = False) -> str:
        result = ''

        for user in users:
            if not silent:
                result += f'*[{user.getUsername()}](tg://user?id={user.getUserId()})* '
            else:
                result += f'*{user.getUsername()}\({user.getUserId()}\)*\n'

        return result

    def isSilent(self, context: CallbackContext) -> bool:
        return context.args and context.args[0] == self.silent