from typing import Iterable

import prettytable as pt
from config.contents import no_groups
from entity.group import Group
from repository.groupRepository import GroupRepository
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from handler.abstractHandler import AbstractHandler


class GroupsHandler(AbstractHandler):
    bot_handler: CommandHandler
    group_repository: GroupRepository

    def __init__(self) -> None:
        self.bot_handler = CommandHandler('groups', self.handle)
        self.group_repository = GroupRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        real_chat_id = str(update.effective_chat.id)

        groups = self.group_repository.get_by_chat_id(real_chat_id)

        if groups:
            return self.reply_html(update, self.build_groups_message(groups))

        self.reply_markdown(update, no_groups)

    def get_bot_handler(self) -> CommandHandler:
        return self.bot_handler

    def build_groups_message(self, groups: Iterable[Group]) -> str:
        resultTable = pt.PrettyTable(['Name', 'Members'])

        resultTable.add_rows([[record.group_name, record.users_count] for record in groups])

        return f'<pre>{str(resultTable)}</pre>'
