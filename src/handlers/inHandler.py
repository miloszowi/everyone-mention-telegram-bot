from config.contents import opted_in_successfully, opted_in_failed
from repositories.relationRepository import RelationRepository
from database.databaseClient import DatabaseClient
from handlers.handlerInterface import HandlerInterface
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
        personId = update.effective_user.id
        chatId = update.effective_chat.id
        username = update.effective_user.username

        relationRepository = RelationRepository()
        relation = relationRepository.get(chatId, personId)

        if relation:
            self.reply(update, opted_in_failed)
            return
        
        relationRepository.save(chatId, personId, username)
        self.reply(update, opted_in_successfully)

    def getBotHandler(self) -> CommandHandler:
        return self.botHandler

    def getCommandName(self) -> str:
        return self.commandName
