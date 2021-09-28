from __future__ import annotations

from dataclasses import dataclass

import names
from telegram.update import Update


@dataclass
class UpdateData():
    user_id: str
    chat_id: str
    username: str

    @staticmethod
    def create_from_update(update: Update) -> UpdateData:
        user_id = str(update.effective_user.id)
        chat_id = str(update.effective_chat.id)
        username = update.effective_user.username or update.effective_user.first_name

        if not username:
            username = names.get_first_name()

        return UpdateData(user_id, chat_id, username)
