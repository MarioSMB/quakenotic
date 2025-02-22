import asyncio

import logsetup
from base.bot_base import BotBase

from enum import Enum

logger = logsetup.setup_log(__name__)

class IRCCommands(Enum):
    set_nick = ""
    join = ""


class IRCInterface(object):
    pass

class IRCProtocol(asyncio.Protocol):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        return

    def connection_made(self, transport):
        return

    def connection_lost(self, exc):
        return

    def data_received(self, data):
        return

    def eof_received(self):
        return

class IRCBot(BotBase):
    def __init__(self):
        super().__init__()

    def __del__(self):
        return

