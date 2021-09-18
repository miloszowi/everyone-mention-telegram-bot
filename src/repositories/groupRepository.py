from ..firebaseProxy import FirebaseProxy


class GroupRepository():
    firebase: FirebaseProxy
    
    def __init__(self) -> None:
        self.firebase = FirebaseProxy()

    def get(self, id: int) -> dict:
        result = []
        groupData = self.firebase.getChilds(FirebaseProxy.group_index, id).get()
        
        if groupData.each():
            for user_root in groupData.each():
                result.append(user_root.val())

        return result
