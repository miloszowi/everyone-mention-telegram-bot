from telegram.ext import Updater
from telegram.ext.dispatcher import Dispatcher

from bot.handler import *
from bot.handler.abstractHandler import AbstractHandler
from config.credentials import BOT_TOKEN, PORT, WEBHOOK_URL
from logger import Logger


class App:
    updater: Updater
    dispatcher: Dispatcher

    def __init__(self):
        self.updater = Updater(BOT_TOKEN)

    def run(self) -> None:
        Logger.register()
        self.register_handlers()
        self.register_webhook()
        
        self.updater.idle()

    def register_handlers(self) -> None:
        for handler in AbstractHandler.__subclasses__():
            self.updater.dispatcher.add_handler(handler().bot_handler)

    def register_webhook(self) -> None:
        self.updater.start_webhook(
            listen="0.0.0.0",
            port=int(PORT),
            url_path=BOT_TOKEN,
            webhook_url="/".join([WEBHOOK_URL, BOT_TOKEN])
        )

        Logger.info(f'Webhook configured, listening on {WEBHOOK_URL}/<bot-token>')


if __name__ == "__main__":
    app = App()
    app.run()
