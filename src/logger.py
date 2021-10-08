from __future__ import annotations

import logging
import os

from bot.message.messageData import MessageData


# noinspection SpellCheckingInspection
class Logger:
    action_logger: str = 'action-logger'
    action_logger_file: str = '/var/log/bot/action.log'

    main_logger: str = 'main-logger'
    main_logger_file: str = '/var/log/bot/app.log'

    # noinspection SpellCheckingInspection
    formatter: logging.Formatter = logging.Formatter('%(asctime)s[%(levelname)s]: %(message)s')

    def __init__(self):
        self.configure(self.action_logger, self.action_logger_file, logging.INFO)
        self.configure(self.main_logger, self.main_logger_file, logging.ERROR)

    def configure(self, logger_name, log_file, level) -> None:
        directory = os.path.dirname(log_file)
        if not os.path.exists(directory):
            os.makedirs(directory)

        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setFormatter(self.formatter)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(self.formatter)

        logger.setLevel(level)
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    @staticmethod
    def register() -> None:
        Logger()

    @staticmethod
    def get_logger(logger_name) -> logging.Logger:
        return logging.getLogger(logger_name)

    @staticmethod
    def info(message: str) -> None:
        Logger.get_logger(Logger.action_logger).info(message)

    @staticmethod
    def error(message: str) -> None:
        Logger.get_logger(Logger.main_logger).error(message)

    @staticmethod
    def action(message_data: MessageData, action: str) -> None:
        Logger.info(f'User {message_data.username}({message_data.user_id}) called {action.upper()} for {message_data.chat_id}')
