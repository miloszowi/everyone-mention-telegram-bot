from __future__ import annotations

import names
from telegram.update import Update


class UpdateData():
    userId: str
    chatId: str
    username: str

    def __init__(self, userId: str, chatId: str, username: str) -> None:
        self.userId = userId
        self.chatId = chatId
        self.username = username

    def getUserId(self) -> str:
        return self.userId

    def getChatId(self) -> str:
        return self.chatId

    def getUsername(self) -> str:
        return self.username

    @staticmethod
    def createFromUpdate(update: Update) -> UpdateData:
        userId = str(update.effective_user.id)
        chatId = str(update.effective_chat.id)
        username = update.effective_user.username or update.effective_user.first_name

        if not username:
            username = names.get_first_name()

        return UpdateData(userId, chatId, username)
