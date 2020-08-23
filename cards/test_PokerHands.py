from unittest import TestCase

from cards.hands.RoyalFlush import isRoyalFlush
from cards.card import Card
from cards.royalty import Royalty
from cards.suit import Suit


class Test(TestCase):
    def test_empty(self):
        self.assertFalse(isRoyalFlush([]))

    def test_is_royal_flush(self):
        self.assertTrue(isRoyalFlush([
            Card(Suit.Heart, Royalty.Ace.value),
            Card(Suit.Heart, Royalty.Jack.value),
            Card(Suit.Heart, 3),
            Card(Suit.Heart, 10),
            Card(Suit.Heart, Royalty.Queen.value),
            Card(Suit.Heart, Royalty.King.value),
        ]))

    def test_is_not_royal_flush(self):
        self.assertFalse(isRoyalFlush([
            Card(Suit.Heart, Royalty.Ace.value),
            Card(Suit.Heart, Royalty.Jack.value),
            Card(Suit.Heart, 3),
            Card(Suit.Heart, 10),
            Card(Suit.Clover, Royalty.Queen.value),
            Card(Suit.Heart, Royalty.King.value),
        ]))

