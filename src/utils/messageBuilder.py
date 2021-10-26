from typing import Iterable

from prettytable import prettytable
from telegram.utils.helpers import mention_markdown

from entity.user import User


class MessageBuilder:
    @staticmethod
    def group_message(groups: dict) -> str:
        table = prettytable.PrettyTable(['Name', 'Members'])

        for group in groups:
            table.add_row([group, len(groups[group])])

        return f'<pre>{str(table)}</pre>'

    @staticmethod
    def mention_message(users: Iterable[User]) -> str:
        return ' '.join([mention_markdown(user.user_id, user.username) for user in users])
