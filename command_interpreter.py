import cmd
from enum import Enum

class List(Enum):
    all = ...
    relays = ...
    pools = ...
    sockets = ...

class Shell(cmd.Cmd):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        return

    def __del__(self):
        return

    def do_list(self, arg):
        match arg:
            case "all":
                return
            case "relays":
                return
            case "pools":
                return
            case "sockets":
                return
        return

def parse(args):
    return