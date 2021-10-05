from __future__ import annotations

from dataclasses import dataclass
import re

import names
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update
from entity.group import Group

from exception.invalidArgumentException import InvalidArgumentException


@dataclass
class UpdateData():
    user_id: str
    chat_id: str
    username: str

    @staticmethod
    def create_from_arguments(update: Update, context: CallbackContext, include_group: bool = True) -> UpdateData:
        chat_id = str(update.effective_chat.id)
        
        if context.args and context.args[0] and include_group:
            group_name = str(context.args[0]).lower()
            if not re.match(r"^[A-Za-z]+$", group_name):
                raise InvalidArgumentException(re.escape('Group name must contain only letters.'))

            if group_name == Group.default_name:
                raise InvalidArgumentException(re.escape(f'Group can not be `{Group.default_name}`.'))

            if len(group_name) > 20:
                raise InvalidArgumentException(re.escape(f'Group name length can not be greater than 20.'))

            chat_id += f'~{group_name}'
            

        user_id = str(update.effective_user.id)
        username = update.effective_user.username or update.effective_user.first_name

        if not username:
            username = names.get_first_name()

        return UpdateData(user_id, chat_id, username)
