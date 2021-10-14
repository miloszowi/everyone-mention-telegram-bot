from __future__ import annotations

from dataclasses import dataclass

import names
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update

from validator.accessValidator import AccessValidator
from validator.groupNameValidator import GroupNameValidator


@dataclass
class InboundMessage:
    user_id: str
    chat_id: str
    group_name: str
    username: str

    default_group: str = 'default'

    @staticmethod
    def create(update: Update, context: CallbackContext, group_specific: bool) -> InboundMessage:
        user_id = str(update.effective_user.id)
        AccessValidator.validate(user_id)

        chat_id = str(update.effective_chat.id)
        group_name = InboundMessage.default_group

        if context.args and context.args[0] and group_specific:
            group_name = str(context.args[0]).lower()

            GroupNameValidator.validate(group_name)

        username = update.effective_user.username or update.effective_user.first_name

        if not username:
            username = names.get_first_name()

        return InboundMessage(user_id, chat_id, group_name, username)
