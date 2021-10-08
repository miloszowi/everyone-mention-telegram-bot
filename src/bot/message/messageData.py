from __future__ import annotations

from dataclasses import dataclass

import names
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update

from entity.group import Group
from validator.accessValidator import AccessValidator
from validator.groupNameValidator import GroupNameValidator


@dataclass
class MessageData:
    user_id: str
    chat_id: str
    group_name: str
    username: str

    @staticmethod
    def create_from_arguments(update: Update, context: CallbackContext, include_group: bool = True) -> MessageData:
        user_id = str(update.effective_user.id)
        AccessValidator.validate(user_id)

        chat_id = str(update.effective_chat.id)
        group_name = Group.default_name

        if context.args and context.args[0] and include_group:
            group_name = str(context.args[0]).lower()

            GroupNameValidator.validate(group_name)

            if group_name is not Group.default_name:
                chat_id += f'~{group_name}'

        username = update.effective_user.username or update.effective_user.first_name

        if not username:
            username = names.get_first_name()

        return MessageData(user_id, chat_id, group_name, username)
