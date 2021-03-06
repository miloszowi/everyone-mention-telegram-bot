from config.envs import BANNED_USERS
from exception.actionNotAllowedException import ActionNotAllowedException


class AccessValidator:

    @staticmethod
    def validate(user_id: str) -> None:
        if user_id in BANNED_USERS:
            raise ActionNotAllowedException('User is banned')
