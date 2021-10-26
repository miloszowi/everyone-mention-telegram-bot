from telegram import InlineQueryResultArticle
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.inlinequeryhandler import \
    InlineQueryHandler as CoreInlineQueryHandler
from telegram.inline.inputtextmessagecontent import InputTextMessageContent
from telegram.update import Update

from bot.handler.abstractHandler import AbstractHandler
from bot.message.inboundMessage import InboundMessage
from exception.actionNotAllowedException import ActionNotAllowedException
from validator.accessValidator import AccessValidator


class InlineQueryHandler(AbstractHandler):
    bot_handler: CoreInlineQueryHandler

    def __init__(self) -> None:
        self.bot_handler = CoreInlineQueryHandler(self.handle)

    def handle(self, update: Update, context: CallbackContext) -> None:
        try:
            AccessValidator.validate(str(update.effective_user.id))
        except ActionNotAllowedException:
            update.inline_query.answer([])
            return

        group_display = update.inline_query.query or InboundMessage.default_group
        group = '' if group_display == InboundMessage.default_group else group_display

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
