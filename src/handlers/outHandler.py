from ..config.contents import opted_off_successfully, opted_off_failed
from ..repositories.userRepository import UserRepository
from .handlerInterface import HandlerInterface
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update


class OutHandler(HandlerInterface):
    botHandler: CommandHandler
    commandName: str = 'out'

    def __init__(self) -> None:
        self.botHandler = CommandHandler(
            self.getCommandName(), 
            self.handle
        )

    def handle(self, update: Update, context: CallbackContext) -> None:
        groupId = update.effective_chat.id
        userData = {
            'id': update.effective_user.id,
            'name': update.effective_user.username
        }

        userRepository = UserRepository()
        if not userRepository.isPresentInGroup(userData.get('id'), groupId):
            update.message.reply_markdown_v2(text=opted_off_failed)
            return

        userRepository.removeForGroup(userId=userData.get('id'), groupId=groupId)

        update.message.reply_markdown_v2(text=opted_off_successfully)

    def getBotHandler(self) -> CommandHandler:
        return self.botHandler

    def getCommandName(self) -> str:
        return self.commandName
