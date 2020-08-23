from unittest import TestCase

from cards.hands.RoyalFlush import isRoyalFlush
from cards.card import Card
from cards.hands.TwoPair import is_two_pair
from cards.royalty import Royalty
from cards.suit import Suit
from cards.hands.Straight import is_straight


class TestPokerHands(TestCase):
    def test_empty_royal_flush(self):
        self.assertFalse(isRoyalFlush([]))

    def test_is_royal_flush(self):
        self.assertTrue(isRoyalFlush([
            Card(Suit.Heart, Royalty.Ace.value),
            Card(Suit.Heart, Royalty.Jack.value),
            Card(Suit.Clover, Royalty.Jack.value),
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
            Card(Suit.Diamond, 3),
            Card(Suit.Heart, 10),
            Card(Suit.Clover, Royalty.Queen.value),
            Card(Suit.Heart, Royalty.King.value),
        ]))

    def test_is_straight_empty(self):
        self.assertFalse(is_straight([]))

    def test_is_straight(self):
        self.assertTrue(is_straight([
            Card(Suit.Heart, Royalty.Ace.value),
            Card(Suit.Heart, 6),
            Card(Suit.Heart, 3),
            Card(Suit.Heart, 5),
            Card(Suit.Clover, 7),
            Card(Suit.Spade, 4),
            Card(Suit.Heart, 10)
        ]))

    def test_is_not_straight(self):
        self.assertFalse(is_straight([
            Card(Suit.Heart, Royalty.Ace.value),
            Card(Suit.Heart, 2),
            Card(Suit.Heart, 5),
            Card(Suit.Diamond, 7),
            Card(Suit.Clover, 9),
            Card(Suit.Spade, Royalty.Jack.value),
            Card(Suit.Spade, 5)
        ]))

    def test_is_two_pair1(self):
        self.assertTrue(is_two_pair([
            Card(Suit.Heart, Royalty.Ace.value),
            Card(Suit.Heart, 6),
            Card(Suit.Heart, 4),
            Card(Suit.Heart, 5),
            Card(Suit.Clover, 5),
            Card(Suit.Spade, 4),
            Card(Suit.Heart, 10)
        ]))
