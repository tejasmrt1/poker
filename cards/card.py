from cards.royalty import Royalty


class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __repr__(self):
        if self.number > 10:
            return '%s of %s' % (Royalty(self.number), self.suit)
        return '%s of %s' % (self.number, self.suit)