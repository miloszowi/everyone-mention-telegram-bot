from telegram.ext import Updater
from telegram.ext.dispatcher import Dispatcher

from config.credentials import BOT_TOKEN
from handler.abstractHandler import AbstractHandler
from handler import (inHandler, mentionHandler, outHandler, silentMentionHandler, groupsHandler)


class App:
    updater: Updater
    dispatcher: Dispatcher

    def __init__(self):
        self.updater = Updater(BOT_TOKEN)

    def run(self) -> None:
        self.register_handlers()
        
        self.updater.start_polling()
        self.updater.idle()

    def register_handlers(self) -> None:
        for handler in AbstractHandler.__subclasses__():
            self.updater.dispatcher.add_handler(
                handler().get_bot_handler()
            )


if __name__ == "__main__":
    app = App()

    app.run()
