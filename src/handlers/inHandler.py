from ..config.contents import opted_in_successfully, opted_in_failed
from ..entities.user import User
from ..repositories.groupRepository import GroupRepository
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
        groupRepository = GroupRepository()
        group = groupRepository.get(update.effective_chat.id)
        user = User(update.effective_user.id, update.effective_user.username)

        if group.hasUser(user):
            update.message.reply_markdown_v2(text=opted_in_failed)
            return

        group.addUser(user)
        groupRepository.save(group)

        update.message.reply_markdown_v2(text=opted_in_successfully)

    def getBotHandler(self) -> CommandHandler:
        return self.botHandler

    def getCommandName(self) -> str:
        return self.commandName
