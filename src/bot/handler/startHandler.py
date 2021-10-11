from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from bot.handler.abstractHandler import AbstractHandler
from bot.message.replier import Replier
from config.contents import start_text
from logger import Logger


class StartHandler(AbstractHandler):
    bot_handler: CommandHandler
    action: str = 'start'

    def __init__(self) -> None:
        self.bot_handler = CommandHandler(self.action, self.wrap)

    def handle(self, update: Update, context: CallbackContext) -> None:
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Inline Mode', switch_inline_query_current_chat='example'),
                ],
                [
                    InlineKeyboardButton('GitHub', url='https://github.com/miloszowi/everyone-mention-telegram-bot'),
                    InlineKeyboardButton('Creator', url='https://t.me/miloszowi')
                ]
            ]
        )

        Replier.html(update, start_text, markup)
        Logger.action(self.inbound, self.action)

    def is_group_specific(self) -> bool:
        return False
