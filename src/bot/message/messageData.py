from __future__ import annotations

import re
from dataclasses import dataclass

import names
from entity.group import Group
from exception.invalidArgumentException import InvalidArgumentException
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update

from validator.groupNameValidator import GroupNameValidator


@dataclass
class MessageData():
    user_id: str
    chat_id: str
    group_name: str
    username: str

    @staticmethod
    def create_from_arguments(update: Update, context: CallbackContext, include_group: bool = True) -> MessageData:
        chat_id = str(update.effective_chat.id)
        group_name = Group.default_name

        if context.args and context.args[0] and include_group:
            group_name = str(context.args[0]).lower()

            GroupNameValidator.validate(group_name)

            if group_name is not Group.default_name:
                chat_id += f'~{group_name}'
            

        user_id = str(update.effective_user.id)
        username = update.effective_user.username or update.effective_user.first_name

        if not username:
            username = names.get_first_name()

        return MessageData(user_id, chat_id, group_name, username)
