from __future__ import annotations

import logging
import os

from bot.message.inboundMessage import InboundMessage


# noinspection SpellCheckingInspection
class Logger:
    action_logger: str = 'action-logger'
    action_logger_file: str = '/var/log/bot/action.log'

    main_logger: str = 'main-logger'
    main_logger_file: str = '/var/log/bot/app.log'

    def __init__(self):
        self.configure(self.action_logger, self.action_logger_file, logging.INFO)
        self.configure(self.main_logger, self.main_logger_file, logging.ERROR)

    def configure(self, logger_name, log_file, level) -> None:
        directory = os.path.dirname(log_file)
        if not os.path.exists(directory):
            os.makedirs(directory)

        logger = logging.getLogger(logger_name)
        logger.propagate = False

        file_handler = logging.FileHandler(log_file, mode='w')
        formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s', datefmt='%H:%M:%S %Y/%m/%d')
        file_handler.setFormatter(formatter)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.setLevel(level)
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    @staticmethod
    def register() -> None:
        Logger()

    @staticmethod
    def get(logger_name: str) -> logging.Logger:
        return logging.getLogger(logger_name)

    @staticmethod
    def info(message: str) -> None:
        Logger.get(Logger.action_logger).info(message)

    @staticmethod
    def error(message: str) -> None:
        Logger.get(Logger.main_logger).error(message)

    @staticmethod
    def exception(exception: Exception) -> None:
        Logger.get(Logger.main_logger).exception(exception)

    @staticmethod
    def action(inbound: InboundMessage, action: str) -> None:
        Logger.info(f'User {inbound.username}({inbound.user_id}) called {action.upper()} for {inbound.chat_id}({inbound.group_name})')
