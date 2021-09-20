from ..entities.group import Group
from ..entities.user import User
from ..firebaseProxy import FirebaseProxy


class GroupRepository():
    firebase: FirebaseProxy
    
    def __init__(self) -> None:
        self.firebase = FirebaseProxy()

    def get(self, id: int) -> Group:
        group = Group(id)
        fbData = self.firebase.getChilds(FirebaseProxy.group_index, id).get()
        users = []

        for userData in fbData.each() or []:
            userData = userData.val()
            users.append(
                User(
                    userData.get(FirebaseProxy.id_index),
                    userData.get(FirebaseProxy.name_index)
                )
            )
    
        group.setUsers(users)

        return group

    def save(self, group: Group) -> None:
        users = {}

        if not group.getUsers():
            self.remove(group)

        for user in group.getUsers():
            users[user.getId()] = {
                FirebaseProxy.id_index: user.getId(),
                FirebaseProxy.name_index: user.getUsername()
            }
        
        self.firebase.getChilds(
            FirebaseProxy.group_index,
            group.getId()
        ).update(users)

    def remove(self, group: Group) -> None:
        self.firebase.getChilds(FirebaseProxy.group_index, group.getId()).remove()