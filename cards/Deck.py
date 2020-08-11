from random import *

from cards.card import RegularCard, RoyaltyCard
from cards.royalty import Royalty
from cards.suit import Suit


class Deck:
    def __init__(self):
        self.cards = []
        for s in Suit:
            for i in range(1, 12):
                self.cards.append(RegularCard(s, i))
            for x in Royalty:
                self.cards.append(RoyaltyCard(s, x))


    def deal(self, how_many):
        dealt_cards = []
        for i in range(0, how_many):
            card = choice(self.cards)
            self.cards.remove(card)
            dealt_cards.append(card)
        return dealt_cards





d = Deck()
dealt_cards = d.deal(5)
print(dealt_cards)