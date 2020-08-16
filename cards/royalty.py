from enum import Enum


class Royalty(Enum):
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14

    def __str__(self):
        return str(self.name)