import os
import sys
import yaml
import asyncio
import logging

from typing import Self, Callable
from enum import Enum

logger = logging.getLogger(__name__)

type IPAddress = tuple[str, int] | list[str, int]

socketTypes = {
    "tcp": lambda running_loop=asyncio.get_running_loop: running_loop().create_server,
    "udp": lambda running_loop=asyncio.get_running_loop: running_loop().create_datagram_endpoint,
    "unix": lambda running_loop=asyncio.get_running_loop: running_loop().create_unix_server,
    # "pipe": ...
}

protocols = {

}

class Connection(object):
    def __init__(self, *args, address: IPAddress, type: str = "tcp", **kwargs):
        super().__init__()
        self.address = tuple(address)
        self.type = type

        asyncio.create_task(self.get_transport_protocol())

    async def get_transport_protocol(self, *args, **kwargs):
        a = socketTypes[self.type]()(*args, **kwargs)
        return

    @classmethod
    async def new(cls, *args, **kwargs) -> Self:
        self = cls(*args, **kwargs)
        self.transport, self.protocol = socketTypes[self.type]()
        return self

    def __del__(self):
        return

    def __str__(self):
        return str(self.address)

    def __repr__(self):
        return self.__str__()

class Handler(object):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.shared_pool = {}
        self.remote_servers = {}
        self.relays = {}

    def __del__(self):
        return

    @classmethod
    async def new(cls, *args, **kwargs):
        self = cls(*args, **kwargs)
        return self

    def run(self):
        try:
            asyncio.run(self.start())
        except Exception as exc:
            logger.exception(exc)
        return

    async def start(self):
        await self.setup()

        # while True:
        #     await asyncio.sleep(0)

    async def setup(self, *args, **kwargs):
        self.relays = await self.load("/config/relays.yaml", Connection)
        self.remote_servers = await self.load("/config/sockets.yaml", Connection)
        self.shared_pool = await self.load("/config/sharedchats.yaml",
                           lambda *args, **kwargs: [self.relays[relay] for relay in self.relays] + [self.remote_servers[server] for server in self.remote_servers])

        return

    @staticmethod
    async def load(path: str, call: Callable, *args, **kwargs) -> dict:
        file = yaml.safe_load(open(os.path.dirname(os.path.realpath(sys.argv[0])) + path))
        dictionary = {}

        for each in file:
            dictionary.update({each : call(*args, **{**file[each], **kwargs})})

        return dictionary

    async def handle(self):
        return

handler = Handler()
handler.run()
print(handler.relays, handler.remote_servers, handler.shared_pool)
print(handler.shared_pool)


