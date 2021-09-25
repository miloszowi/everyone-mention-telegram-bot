from database.databaseClient import DatabaseClient
from entities.person import Person
from typing import Iterable, Optional

class PersonRepository:
    database: DatabaseClient

    def __init__(self) -> None:
        self.database = DatabaseClient()

    def get(self, id: str) -> Optional[Person]:
        person = Person(id)
        search = self.database.findOne(Person.getMongoRoot(), person.toDict(False))
        
        return Person.fromDocument(search)        
        
    def find(self, query: dict) -> Iterable[Person]:
        result = []
        search = self.database.find(Person.getMongoRoot(), query)

        for document in search:
            result.append(Person.fromDocument(document))

        return result

    def save(self, person: Person) -> None:
        self.database.insert(Person.getMongoRoot(), person.toDict())