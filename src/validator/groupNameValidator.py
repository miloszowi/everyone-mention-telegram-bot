import re

from exception.invalidArgumentException import InvalidArgumentException


class GroupNameValidator:
    MAX_GROUP_NAME_LENGTH: int = 40
    FORBIDDEN_GROUP_NAMES = ['all', 'channel', 'chat', 'everyone', 'group', 'here']

    @staticmethod
    def validate(group: str) -> None:
        group = group.lower()

        if len(group) > 0 and not re.match('^\w+$', group):
            raise InvalidArgumentException(re.escape('Special characters are not allowed.'))

        if len(group) > GroupNameValidator.MAX_GROUP_NAME_LENGTH:
            raise InvalidArgumentException(re.escape(f'Group name length can not be greater than {GroupNameValidator.MAX_GROUP_NAME_LENGTH}.'))

        if group in GroupNameValidator.FORBIDDEN_GROUP_NAMES:
            raise InvalidArgumentException(re.escape(f'This group name is forbidden, please try with other name.'))
