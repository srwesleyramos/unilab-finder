from enum import Enum


class Type(Enum):
    LIVRE = {
        "key": "0",
        "icon": "0"
    }
    PAREDE = {
        "key": "1",
        "icon": "1"
    }
    ROBO = {
        "key": "7",
        "icon": "7"
    }
    QUEIJO = {
        "key": "9",
        "icon": "9"
    }

    def getKey(self):
        return self.value["key"]

    def getIcon(self):
        return self.value["icon"]

    @classmethod
    def find(cls, argument):
        for obj in cls:
            if obj.getKey() == argument:
                return obj
        return None
