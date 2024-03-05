from typing import Optional

from telegram import InlineKeyboardMarkup, Update
from telegram.utils.helpers import mention_markdown

from bot.message.inboundMessage import InboundMessage
from logger import Logger


class Replier:
    @staticmethod
    def interpolate(content: str, inbound_message: InboundMessage):
        formatted = content.format(
            mention_markdown(inbound_message.user_id, inbound_message.username),
            inbound_message.group_name
        )

        telegramRestrictionCharacters = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']

        for character in telegramRestrictionCharacters:
            formatted.replace(character, r'\{character}')

        return formatted

    @staticmethod
    def markdown(update: Update, message: str, reply_markup: Optional[InlineKeyboardMarkup] = None) -> None:
        try:
            update.effective_message.reply_markdown_v2(message, reply_markup=reply_markup)
        except Exception as err:
            Logger.error("replier.markdown error: " + str(err))

    @staticmethod
    def html(update: Update, html: str, reply_markup: Optional[InlineKeyboardMarkup] = None) -> None:
        try:
            update.effective_message.reply_html(html, reply_markup=reply_markup, disable_web_page_preview=True)
        except Exception as err:
            Logger.error("replier.html error: " + str(err))
