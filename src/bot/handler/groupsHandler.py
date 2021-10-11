from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.update import Update

from bot.handler.abstractHandler import AbstractHandler
from bot.message.replier import Replier
from config.contents import no_groups
from exception.notFoundException import NotFoundException
from logger import Logger
from repository.groupRepository import GroupRepository
from utils.messageBuilder import MessageBuilder


class GroupsHandler(AbstractHandler):
    bot_handler: CommandHandler
    group_repository: GroupRepository
    action: str = 'groups'

    def __init__(self) -> None:
        self.bot_handler = CommandHandler(self.action, self.wrap)
        self.group_repository = GroupRepository()

    def handle(self, update: Update, context: CallbackContext) -> None:
        try:
            groups = self.group_repository.get_by_chat_id(self.inbound.chat_id)
            Replier.html(update, MessageBuilder.group_message(groups))

            Logger.action(self.inbound, self.action)
        except NotFoundException:
            Replier.markdown(update, no_groups)

    def is_group_specific(self) -> bool:
        return False
