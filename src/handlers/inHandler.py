from ..config.contents import opted_in_successfully, opted_in_failed
from ..repositories.userRepository import UserRepository
from ..firebaseProxy import FirebaseProxy
from .handlerInterface import HandlerInterface
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update


class InHandler(HandlerInterface):
    botHandler: CommandHandler
    commandName: str = 'in'

    def __init__(self) -> None:
        self.botHandler = CommandHandler(
            self.getCommandName(),
            self.handle
        )

    def handle(self, update: Update, context: CallbackContext) -> None:
        groupId = update.effective_chat.id
        userData = {
            FirebaseProxy.id_index: update.effective_user.id,
            FirebaseProxy.name_index: update.effective_user.username
        }
        userRepository = UserRepository()

        if userRepository.isPresentInGroup(userData.get(FirebaseProxy.id_index), groupId):
            update.message.reply_markdown_v2(text=opted_in_failed)
            return

        userRepository.addForGroup(userData, groupId)
        update.message.reply_markdown_v2(text=opted_in_successfully)

    def getBotHandler(self) -> CommandHandler:
        return self.botHandler

    def getCommandName(self) -> str:
        return self.commandName
