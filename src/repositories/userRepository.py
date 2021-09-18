from ..firebaseProxy import FirebaseProxy


class UserRepository():
    firebaseProxy: FirebaseProxy

    def __init__(self) -> None:
        self.firebaseProxy = FirebaseProxy()

    def addForGroup(self, userData: dict, groupId: int) -> None:
        self.firebaseProxy.getChilds(FirebaseProxy.getGroupPath(groupId)).update({
            f'{groupId}_{userData.get("id")}': {
                FirebaseProxy.id_index: userData.get("id"),
                FirebaseProxy.name_index: userData.get("name")
            }
        })

    def removeForGroup(self, userId: int, groupId: int) -> None:
        self.firebaseProxy.getChilds(FirebaseProxy.getGroupPath(groupId)).update({
            FirebaseProxy.getUserPath(userId, groupId): {}
        })

    def isPresentInGroup(self, userId: int, groupId: int) -> bool:
        user = self.firebaseProxy.getChilds(
            FirebaseProxy.getGroupPath(groupId),
            FirebaseProxy.getUserPath(userId, groupId)
        ).get().val()

        return bool(user)
    