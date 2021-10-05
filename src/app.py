from logging import Logger
import logging
from telegram.ext import Updater
from telegram.ext.dispatcher import Dispatcher

from logger import Logger
from config.credentials import BOT_TOKEN, PORT, WEBHOOK_URL
from handler import (groupsHandler, inHandler, mentionHandler, outHandler,
                     silentMentionHandler, startHandler)
from handler.abstractHandler import AbstractHandler


class App:
    updater: Updater
    dispatcher: Dispatcher

    log_file: str = '/var/log/bot.log'
    log_format: str = '%(levelname)s-%(asctime)s: %(message)s'

    def __init__(self):
        self.updater = Updater(BOT_TOKEN)

    def run(self) -> None:
        self.setup_logging()
        self.register_handlers()
        self.register_webhook()
        
        self.updater.idle()

    def register_handlers(self) -> None:
        for handler in AbstractHandler.__subclasses__():
            self.updater.dispatcher.add_handler(
                handler().get_bot_handler()
            )

    def register_webhook(self) -> None:
        self.updater.start_webhook(
            listen="0.0.0.0",
            port=int(PORT),
            url_path=BOT_TOKEN,
            webhook_url="/".join([WEBHOOK_URL, BOT_TOKEN])
        )

        Logger.get_logger(Logger.action_logger).info(
            f'Webhook configured, listening on {WEBHOOK_URL}/<bot-token>'
        )

    def setup_logging(self) -> None:
        logger = Logger()
        logger.setup()

if __name__ == "__main__":
    app = App()

    app.run()
