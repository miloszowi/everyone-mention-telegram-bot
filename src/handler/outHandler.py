from config.contents import opted_off, opted_off_failed
from exception.notFoundException import NotFoundException
from repository.userRepository import UserRepository
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from handler.abstractHandler import AbstractHandler


class OutHandler(AbstractHandler):
    botHandler: CommandHandler
    userRepository: UserRepository

    def __init__(self) -> None:
        self.botHandler = CommandHandler('out', self.handle)
        self.userRepository = UserRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        updateData = self.getUpdateData(update)

        try:
            user = self.userRepository.getById(updateData.getUserId())
            if not user.isInChat(updateData.getChatId()):
                raise NotFoundException()
        except NotFoundException:
            self.reply(update, opted_off_failed)
            return

        user.removeFromChat(updateData.getChatId())
        self.userRepository.save(user)

        self.reply(update, opted_off)

    def getBotHandler(self) -> CommandHandler:
        return self.botHandler
