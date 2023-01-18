from enum import Enum, auto


class Color(Enum):
    YELLOW = auto()
    RED = auto()
    PINK = auto()

    def __str__(self):
        return {
            Color.YELLOW: "#FFCC00",
            Color.RED: "#FF0000",
            Color.PINK: "#FFCCFF",
        }[self]
