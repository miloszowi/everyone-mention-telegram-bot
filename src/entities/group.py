from typing import Iterable
from .user import User

class Group():
    __id: int
    __users: Iterable[User] = []

    def __init__(self, id: int) -> None:
        self.__id = id

    def getId(self) -> int:
        return self.__id

    def setUsers(self, users: Iterable[User]) -> None:
        self.__users = users

    def addUser(self, user: User) -> None:
        self.__users.append(user)

    def removeUser(self, user: User) -> None:
        for index, groupUser in enumerate(self.__users):
            if groupUser.getId() == user.getId():
                del self.__users[index]

    def getUsers(self) -> Iterable[User]:
        return self.__users
    
    def hasUser(self, user: User) -> bool:
        userIds = [int(groupUser.getId()) for groupUser in self.getUsers()]

        if user.getId() in userIds:
            return True

        return False