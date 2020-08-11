class Card:
    def __init__(self, suit):
        self.suit = suit


class RoyaltyCard(Card):
    def __init__(self, suit, royalty):
        self.suit = suit
        self.royalty = royalty

    def __repr__(self):
        return '%s of %s' % (self.royalty, self.suit)


class RegularCard(Card):
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __repr__(self):
        return '%s of %s' % (self.number, self.suit)
