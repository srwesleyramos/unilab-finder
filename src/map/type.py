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

    @classmethod
    def find(cls, argument):
        for obj in cls:
            if obj.value["key"] == argument:
                return obj
        return None
