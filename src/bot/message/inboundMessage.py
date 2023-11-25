from __future__ import annotations

from dataclasses import dataclass

import names
import re
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update

from exception.invalidActionException import InvalidActionException
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

        message_content = update.edited_message.text if update.edited_message else update.message.text
        message_content = message_content.replace("\n", " ")
        chat_id = str(update.effective_chat.id)
        group_name = InboundMessage.default_group

        # done upon resolving a command action
        if context.args and context.args[0] and group_specific:
            group_name = str(context.args[0]).lower()

            GroupNameValidator.validate(group_name)

        # done upon resolving a message handler action
        if '@' in message_content and '@everyone_mention_bot' not in message_content:
            searched_message_part = [part for part in message_content.split(' ') if '@' in part][0]
            group_name = re.sub(r'\W+', '', searched_message_part).lower()

            if group_name in GroupNameValidator.FORBIDDEN_GROUP_NAMES:
                group_name = InboundMessage.default_group

        username = update.effective_user.username or update.effective_user.first_name

        if not username:
            username = names.get_first_name()

        return InboundMessage(user_id, chat_id, group_name, username)
