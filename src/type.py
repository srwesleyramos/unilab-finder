from enum import Enum

from colorama import Fore, Style


class Type(Enum):
    LIVRE = {
        "key": "0",
        "icon": Fore.BLACK + "0" + Style.RESET_ALL,
    }
    PAREDE = {
        "key": "1",
        "icon": Fore.WHITE + "1" + Style.RESET_ALL,
    }
    ROBO = {
        "key": "7",
        "icon": Fore.MAGENTA + "7" + Style.RESET_ALL,
    }
    QUEIJO = {
        "key": "9",
        "icon": Fore.YELLOW + "9" + Style.RESET_ALL,
    }

    def key(self):
        return self.value["key"]

    def icon(self):
        return self.value["icon"]

    @classmethod
    def find(cls, argument):
        for obj in cls:
            if obj.key() == argument:
                return obj
        return None
