from abc import abstractmethod

from telegram.ext import Handler
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update

from bot.message.inboundMessage import InboundMessage
from bot.message.replier import Replier
from exception.actionNotAllowedException import ActionNotAllowedException
from exception.invalidArgumentException import InvalidArgumentException
from logger import Logger


class AbstractHandler:
    bot_handler: Handler
    inbound: InboundMessage

    @abstractmethod
    def handle(self, update: Update, context: CallbackContext) -> None:
        raise Exception('handle method is not implemented')

    def wrap(self, update: Update, context: CallbackContext) -> None:
        try:
            group_specific = self.is_group_specific()

            self.inbound = InboundMessage.create(update, context, group_specific)
            self.handle(update, context)
        except (ActionNotAllowedException, InvalidArgumentException) as e:
            Replier.markdown(update, str(e))
        except Exception as e:
            Logger.exception(e)

    def is_group_specific(self) -> bool:
        return True
