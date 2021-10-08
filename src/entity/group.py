from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Group:
    chat_id: str
    group_name: str
    users_count: int

    default_name: str = 'default'
