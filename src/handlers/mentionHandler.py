from ..config.contents import mention_failed
from ..firebaseProxy import FirebaseProxy
from ..repositories.groupRepository import GroupRepository
from .handlerInterface import HandlerInterface
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update


class MentionHandler(HandlerInterface):
    botHandler: CommandHandler
    commandName: str = 'everyone'

    def __init__(self) -> None:
        self.botHandler = CommandHandler(
            self.getCommandName(), 
            self.handle
        )

    def handle(self, update: Update, context: CallbackContext) -> None:
        groupId = update.effective_chat.id
        groupRepository = GroupRepository()
        mentionMessage = self.buildMentionMessage(groupRepository.get(id=groupId))

        update.message.reply_markdown_v2(text=mentionMessage)

    def getBotHandler(self) -> CommandHandler:
        return self.botHandler

    def getCommandName(self) -> str:
        return self.commandName

    def buildMentionMessage(self, usersData: dict) -> str:
        result = ''

        for userData in usersData:
            userId = str(userData.get(FirebaseProxy.id_index))
            username = userData.get(FirebaseProxy.name_index) or userId

            result += "*[%s](tg://user?id=%s)* " % (username, userId)

        return result or mention_failed
