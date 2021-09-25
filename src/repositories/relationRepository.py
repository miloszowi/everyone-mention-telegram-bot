from typing import Iterable, Optional
from database.databaseClient import DatabaseClient
from entities.chat import Chat
from entities.chatPerson import ChatPerson
from entities.person import Person
from repositories.personRepository import PersonRepository
from repositories.chatRepository import ChatRepository


class RelationRepository():
    client: DatabaseClient

    def __init__(self) -> None:
        self.client = DatabaseClient()

    def get(self, chatId: str, personId: str) -> Optional[ChatPerson]:
        relation = ChatPerson(chatId, personId)
        search = self.client.findOne(ChatPerson.getMongoRoot(), relation.toDict())
        
        return ChatPerson.fromDocument(search)

    def save(self, chatId: str, personId: str, username: Optional[str] = None) -> None:
        relation = ChatPerson(chatId, personId)

        self.client.insert(ChatPerson.getMongoRoot(), relation.toDict())
        personRepository = PersonRepository()
        person = personRepository.get(personId)

        if not person:
            person = Person(personId, username)
            personRepository.save(person)

        chatRepository = ChatRepository()
        chat = chatRepository.get(chatId)
        
        if not chat:
            chat = Chat(chatId)
            chatRepository.save(chat)

    def getPersonsForChat(self, chatId: str) -> Iterable[ChatPerson]:
        result = []
        relations = self.client.find(ChatPerson.getMongoRoot(), {'chat_id': chatId})
        
        search = {}
        for relation in relations:
            search['_id'] = relation['person_id']

        if not search:
            return result

        personRepository = PersonRepository()
        return personRepository.find(search)

    def remove(self, relation: ChatPerson) -> None:
        self.client.remove(ChatPerson.getMongoRoot() ,relation.toDict())

