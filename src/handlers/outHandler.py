from config.contents import opted_off_successfully, opted_off_failed
from handlers.handlerInterface import HandlerInterface
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from repositories.relationRepository import RelationRepository


class OutHandler(HandlerInterface):
    botHandler: CommandHandler
    commandName: str = 'out'

    def __init__(self) -> None:
        self.botHandler = CommandHandler(
            self.getCommandName(), 
            self.handle
        )

    def handle(self, update: Update, context: CallbackContext) -> None:
        personId = update.effective_user.id
        chatId = update.effective_chat.id

        relationRepository = RelationRepository()
        relation = relationRepository.get(chatId, personId)
        
        if not relation:
            self.reply(update, opted_off_failed)
            return
        
        relationRepository.remove(relation)
        self.reply(update, opted_off_successfully)

    def getBotHandler(self) -> CommandHandler:
        return self.botHandler

    def getCommandName(self) -> str:
        return self.commandName
