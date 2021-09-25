from telegram.ext import Updater
from telegram.ext.dispatcher import Dispatcher

from config.credentials import BOT_TOKEN
from handler.abstractHandler import AbstractHandler
from handler import (inHandler, mentionHandler, outHandler)


class App:
    updater: Updater
    dispatcher: Dispatcher

    def __init__(self):
        self.updater = Updater(BOT_TOKEN)

    def run(self) -> None:
        self.registerHandlers()
        
        self.updater.start_polling()
        self.updater.idle()

    def registerHandlers(self) -> None:
        for handler in AbstractHandler.__subclasses__():
            self.updater.dispatcher.add_handler(
                handler().getBotHandler()
            )


if __name__ == "__main__":
    app = App()

    app.run()
