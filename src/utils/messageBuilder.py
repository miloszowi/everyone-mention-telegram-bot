from typing import Iterable

from prettytable import prettytable
from telegram.utils.helpers import mention_markdown

from entity.group import Group
from entity.user import User


class MessageBuilder:
    @staticmethod
    def group_message(groups: Iterable[Group]) -> str:
        table = prettytable.PrettyTable(['Name', 'Members'])

        table.add_rows([[record.group_name, record.users_count] for record in groups])

        return f'<pre>{str(table)}</pre>'

    @staticmethod
    def mention_message(users: Iterable[User]) -> str:
        return ' '.join([mention_markdown(user.user_id, user.username) for user in users])
