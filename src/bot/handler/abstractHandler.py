from abc import abstractmethod

from telegram.ext import Handler
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update

from bot.message.inboundMessage import InboundMessage
from bot.message.replier import Replier
from exception.actionNotAllowedException import ActionNotAllowedException
from exception.invalidActionException import InvalidActionException
from exception.invalidArgumentException import InvalidArgumentException
from exception.notFoundException import NotFoundException
from logger import Logger


class AbstractHandler:
    bot_handler: Handler
    inbound: InboundMessage
    action: str

    @abstractmethod
    def handle(self, update: Update, context: CallbackContext) -> None:
        raise Exception('handle method is not implemented')

    def wrap(self, update: Update, context: CallbackContext) -> None:
        try:
            group_specific = self.is_group_specific()

            self.inbound = InboundMessage.create(update, context, group_specific)
            self.handle(update, context)
            Logger.action(self.inbound, self.action)
        except (InvalidActionException, InvalidArgumentException, ActionNotAllowedException) as e:
            Replier.markdown(update, str(e))
        except NotFoundException:
            pass  # probably just mentioning user
        except Exception as e:
            Logger.exception(e)

    def is_group_specific(self) -> bool:
        return True
