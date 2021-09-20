from typing import Optional

class User():
    __id: int
    __username: Optional[str]
    __groupId: int

    def __init__(self, id: int, username: Optional[str]) -> None:
        self.__id = id
        self.__username = username

    def getId(self) -> int:
        return self.__id

    def getUsername(self) -> Optional[str]:
        return self.__username
    
    def getGroupId(self) -> int:
        return self.__groupId