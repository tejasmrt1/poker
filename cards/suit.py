from enum import Enum


class Suit(Enum):
    Heart = 1
    Diamond = 2
    Spade = 3
    Clover = 4

    def __str__(self):
        return self.name

