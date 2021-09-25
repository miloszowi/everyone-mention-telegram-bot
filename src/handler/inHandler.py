from config.contents import opted_in, opted_in_failed
from exception.notFoundException import NotFoundException
from repository.userRepository import UserRepository
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from handler.abstractHandler import AbstractHandler


class InHandler(AbstractHandler):
    botHandler: CommandHandler
    userRepository: UserRepository

    def __init__(self) -> None:
        self.botHandler = CommandHandler('in', self.handle)
        self.userRepository = UserRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        updateData = self.getUpdateData(update)

        try:
            user = self.userRepository.getById(updateData.getUserId())

            if user.isInChat(updateData.getChatId()):
                self.reply(update, opted_in_failed)
                return

            user.addToChat(updateData.getChatId())
            self.userRepository.save(user)
            
        except NotFoundException:
            self.userRepository.saveByUpdateData(updateData)

        self.reply(update, opted_in)

    def getBotHandler(self) -> CommandHandler:
        return self.botHandler
