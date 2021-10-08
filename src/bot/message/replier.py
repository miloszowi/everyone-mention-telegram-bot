from telegram import Update
from telegram.utils.helpers import mention_markdown

from bot.message.messageData import MessageData
from logger import Logger


class Replier:

    @staticmethod
    def interpolate(content: str, message_data: MessageData):
        return content.format(
            mention_markdown(message_data.user_id, message_data.username),
            message_data.group_name
        )

    @staticmethod
    def markdown(update: Update, message: str) -> None:
        try:
            update.effective_message.reply_markdown_v2(message)
        except Exception as err:
            Logger.error(str(err))

    @staticmethod
    def html(update: Update, html: str) -> None:
        try:
            update.effective_message.reply_html(html)
        except Exception as err:
            Logger.error(str(err))
