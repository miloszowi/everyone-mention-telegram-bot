import re

from exception.invalidArgumentException import InvalidArgumentException


class GroupNameValidator:

    @staticmethod
    def validate(group: str) -> None:
        group = group.lower()

        if len(group) > 0 and not re.match(r"^[A-Za-z]+$", group):
            raise InvalidArgumentException(re.escape('Group name must contain only letters.'))

        if len(group) > 20:
            raise InvalidArgumentException(re.escape(f'Group name length can not be greater than 20.'))
