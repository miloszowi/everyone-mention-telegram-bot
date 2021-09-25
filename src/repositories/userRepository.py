from ..firebaseProxy import FirebaseProxy


class UserRepository():
    firebaseProxy: FirebaseProxy

    def __init__(self) -> None:
        self.firebaseProxy = FirebaseProxy()

    # TODO : this repository needs to handle user save/deletion/update
    # right now, all of those above is handled by GroupRepository
    