from cards.royalty import Royalty


class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def is_royalty(self):
        return self.number > 10

    def __repr__(self):
        if self.is_royalty():
            return '%s of %s' % (Royalty(self.number), self.suit)
        return '%s of %s' % (self.number, self.suit)