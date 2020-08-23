from cards.Deck import Deck
from cards.hands.RoyalFlush import isRoyalFlush
from cards.util.contiguous import contiguous_cards
from cards.suit import Suit


def is_straight(cards):
    return contiguous_cards(cards, 5)


def is_straight_flush(cards):
    number_suit = {}
    for s in Suit:
        number_suit[s] = []

    for i in cards:
        number_suit[i.suit].append(i)
    for i in number_suit.values():
        if contiguous_cards(i, 5):
            return True
    return False


################


def is_of_a_kind(cards, what_of_a_kind):
    count_keeper = {}
    for card in cards:
        count_keeper[card.number] = count_keeper.get(card.number, 0) + 1
    for count in count_keeper.values():
        if count == what_of_a_kind:
            return True
    return False


def is_full_house(cards):
    x = (is_of_a_kind(cards, 3))
    y = (is_of_a_kind(cards, 2))
    if x == True and y == True:
        return True
    else:
        return False


def is_flush(cards):
    number_suit = {}
    for s in Suit:
        number_suit[s] = 0

    for i in cards:
        number_suit[i.suit] = number_suit[i.suit] + 1
    for x in number_suit.values():
        if x == 5:
            return True
    return False


def is_2_pair(cards):
    first_pair = (is_of_a_kind(cards, 2))
    second_pair = (is_of_a_kind(cards, 2))
    if first_pair == True and second_pair == True:
        return True
    else:
        return False


def is_high_card(cards):
    if (isRoyalFlush(cards)) == False and (is_straight_flush(cards)) == False and (is_of_a_kind(cards, 4)) == False and (
    is_of_a_kind(cards, 3)) == False and (is_of_a_kind(cards, 2)) == False and (is_full_house(cards)) == False and (
    is_flush(cards)) and (is_2_pair(cards)) == False and (is_straight_flush(cards)) == False:
        return True
    else:
        return False


for i in range(20):
    z = Deck()
    v = z.deal(7)
    is4OfAKind = is_high_card(v)
    if is4OfAKind:
        print(i)
        print(is4OfAKind)
        print(v)
