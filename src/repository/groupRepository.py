import itertools
import re
from typing import Iterable

from database.client import Client
from entity.group import Group
from entity.user import User


class GroupRepository():
    client: Client

    count: str = 'count'

    def __init__(self) -> None:
        self.client = Client()

    def get_by_chat_id(self, chat_id: str) -> Iterable[Group]:    
        groups = self.client.aggregate(
            User.collection,
            [
                { "$unwind": f'${User.chats_index}' },
                {
                    "$match": {
                        User.chats_index: { "$regex": re.compile(f'^{chat_id}.*$') },
                    },
                },
                {
                    "$group": {
                        "_id": {
                            "$last": { "$split": [f'${User.chats_index}', "~"] },
                        },
                        self.count: { "$count": {} },
                    },
                },
                {
                    "$sort": { '_id': 1 }
                }
            ]
        )

        result = []
        for group in groups:
            group_name = group['_id']

            if group_name == chat_id:
                group_name = Group.default_name

            result.append(
                Group(chat_id, group_name, group[self.count])
            )

        return result
