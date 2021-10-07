from bot.handler.abstractHandler import AbstractHandler
from entity.group import Group
from telegram import InlineQueryResultArticle
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.inlinequeryhandler import \
    InlineQueryHandler as CoreInlineQueryHandler
from telegram.inline.inputtextmessagecontent import InputTextMessageContent
from telegram.update import Update


class InlineQueryHandler(AbstractHandler):
    bot_handler: CommandHandler

    def __init__(self) -> None:
        self.bot_handler = CoreInlineQueryHandler(self.handle)

    def handle(self, update: Update, context: CallbackContext) -> None:
        group_display = update.inline_query.query or Group.default_name
        group = '' if group_display == Group.default_name else group_display

        results = [
            InlineQueryResultArticle(
                id='everyone',
                title='MENTION',
                description=f'Mention members in group "{group_display}"',
                input_message_content=InputTextMessageContent(f'/everyone {group}')
            ),
            InlineQueryResultArticle(
                id='join',
                title='JOIN',
                description=f'Joins group "{group_display}"',
                input_message_content=InputTextMessageContent(f'/join {group}')
            ),
            InlineQueryResultArticle(
                id='leave',
                title='LEAVE',
                description=f'Leaves group "{group_display}"',
                input_message_content=InputTextMessageContent(f'/leave {group}')
            )
        ]

        update.inline_query.answer(results, cache_time=4800)

    def get_bot_handler(self) -> CoreInlineQueryHandler:
        return self.bot_handler
