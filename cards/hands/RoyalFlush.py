from cards.suit import Suit


def isRoyalFlush(cards):
    number_suit = {}
    for s in Suit:
        number_suit[s] = 0
    for i in cards:
        if i.number > 9:
            number_suit[i.suit] = number_suit[i.suit] + 1
    for x in number_suit.values():
        if x >= 5:
            return True

    return False