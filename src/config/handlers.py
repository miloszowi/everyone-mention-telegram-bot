from ..handlers.inHandler import InHandler
from ..handlers.outHandler import OutHandler
from ..handlers.mentionHandler import MentionHandler

handlers = [
    InHandler(),
    OutHandler(),
    MentionHandler()
]
