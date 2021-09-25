from ..config.contents import opted_off_successfully, opted_off_failed
from ..entities.user import User
from ..repositories.groupRepository import GroupRepository
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
        groupRepository = GroupRepository()
        group = groupRepository.get(update.effective_chat.id)
        user = User(update.effective_user.id, update.effective_user.username)

        if group.hasUser(user):
            group.removeUser(user)
            groupRepository.save(group)
            
            update.message.reply_markdown_v2(text=opted_off_successfully)
            return

        update.message.reply_markdown_v2(text=opted_off_failed)

    def getBotHandler(self) -> CommandHandler:
        return self.botHandler

    def getCommandName(self) -> str:
        return self.commandName
