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
    def create_from_arguments(update: Update, context: CallbackContext) -> UpdateData:
        chat_id = str(update.effective_chat.id)
        
        if context.args and context.args[0]:
            if not context.args[0].isalpha() or context.args[0] == Group.default_name:
                raise InvalidArgumentException(re.escape(f'Group name must contain only letters and can not be `{Group.default_name}`.'))
            else:
                chat_id += f'~{context.args[0]}'.lower()
            

        user_id = str(update.effective_user.id)
        username = update.effective_user.username or update.effective_user.first_name

        if not username:
            username = names.get_first_name()

        return UpdateData(user_id, chat_id, username)
