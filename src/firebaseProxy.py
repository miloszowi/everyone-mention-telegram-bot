import pyrebase
from pyrebase.pyrebase import Database as FirebaseDB
from .config.credentials import firebaseConfig


class FirebaseProxy():
    db: FirebaseDB

    # Group specific values
    group_index: str = 'groups'

    # User specific values
    id_index: str = 'id'
    name_index: str = 'name'

    def __init__(self) -> None:
        firebase = pyrebase.pyrebase.initialize_app(firebaseConfig)
        self.db = firebase.database()

    def getChilds(self, *childs: str) -> FirebaseDB:
        current = self.db

        for child_index in childs:
            current = current.child(child_index)
        
        return current

    @staticmethod
    def getGroupPath(groupId: int) -> str:
        return f'{FirebaseProxy.group_index}/{groupId}'

    @staticmethod
    def getUserPath(userId: int, groupId: int) -> str:
        return f'{groupId}_{userId}'
