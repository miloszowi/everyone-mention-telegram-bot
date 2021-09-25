from typing import Iterable
from config.contents import mention_failed
from entities.person import Person
from handlers.handlerInterface import HandlerInterface
from repositories.relationRepository import RelationRepository
from repositories.personRepository import PersonRepository
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
        relationRepository = RelationRepository()
        persons = relationRepository.getPersonsForChat(update.effective_chat.id)

        if not persons:
            self.reply(update, mention_failed)
            return

        self.reply(update, self.buildMentionMessage(persons))


    def getBotHandler(self) -> CommandHandler:
        return self.botHandler

    def getCommandName(self) -> str:
        return self.commandName

    def buildMentionMessage(self, persons: Iterable[Person]) -> str:
        result = ''

        for person in persons:
            result +=  f'*[{person.getUsername()}](tg://user?id={person.getId()})* '

        return result
