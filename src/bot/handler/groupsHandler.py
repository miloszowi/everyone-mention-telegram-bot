from typing import Iterable

import prettytable as pt
from bot.handler.abstractHandler import AbstractHandler
from bot.message.messageData import MessageData
from config.contents import no_groups
from entity.group import Group
from logger import Logger
from repository.groupRepository import GroupRepository
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update


class GroupsHandler(AbstractHandler):
    bot_handler: CommandHandler
    group_repository: GroupRepository

    def __init__(self) -> None:
        self.bot_handler = CommandHandler('groups', self.handle)
        self.group_repository = GroupRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        message_data = MessageData.create_from_arguments(update, context, False)

        groups = self.group_repository.get_by_chat_id(message_data.chat_id)

        if groups:
            self.reply_html(update, self.build_groups_message(groups))
            return self.log_action(message_data)

        self.reply_markdown(update, no_groups)

    def get_bot_handler(self) -> CommandHandler:
        return self.bot_handler

    def log_action(self, message_data: MessageData) -> None:
        Logger.info(f'User {message_data.username} called /groups for {message_data.chat_id}')

    def build_groups_message(self, groups: Iterable[Group]) -> str:
        resultTable = pt.PrettyTable(['Name', 'Members'])

        resultTable.add_rows([[record.group_name, record.users_count] for record in groups])

        return f'<pre>{str(resultTable)}</pre>'
