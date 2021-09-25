from config.credentials import bot_token
from config.handlers import handlers
from handlers.handlerInterface import HandlerInterface
from telegram.ext.dispatcher import Dispatcher
from telegram.ext import Updater

class App:
    updater: Updater
    dispatcher: Dispatcher

    def __init__(self):
        self.updater = Updater(bot_token)

    def run(self) -> None:
        self.registerHandlers()
        
        self.updater.start_polling()
        self.updater.idle()

    def registerHandlers(self) -> None:
        for handler in handlers:
            if not isinstance(handler, HandlerInterface):
                raise Exception('Invalid list of handlers provided. Handler must implement HandlerInterface')

            self.updater.dispatcher.add_handler(handler.getBotHandler())


if __name__ == "__main__":
    app = App()

    app.run()