from random import *

from cards.card import Card
from cards.suit import Suit


class Deck:
    def __init__(self):
        self.cards = []
        for s in Suit:
            for i in range(2, 15):
                self.cards.append(Card(s, i))

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