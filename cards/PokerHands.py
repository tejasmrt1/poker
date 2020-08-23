from cards.Deck import Deck
from cards.contiguous import conti
from cards.suit import Suit



# def detect(concards, cards):


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



def is4ofakind(cards, what_of_a_kind):
    count_keeper = {}
    for card in cards:
            count_keeper[card.number] = count_keeper.get(card.number, 0) + 1
    for count in count_keeper.values():
        if count == what_of_a_kind:
            return True
    return False







def are_contiguous_five(cards_of_same_suit):
    conti( map(lambda x: x.number, cards_of_same_suit), 5)



def is_straight_flush(cards):
        number_suit = {}
        for s in Suit:
            number_suit[s] = []

        for i in cards:
            number_suit[i.suit].append(i)
        for i in number_suit.values():
            if are_contiguous_five(list(number_suit.values()).sort()):
                return True
        return False



def is_full_house(cards):
    x = (is4ofakind(cards, 3))
    y = (is4ofakind(cards, 2))
    if x == True and y == True:
        return True
    else:
        return False

def is_flush(cards):
    #map of (suit, list of cards)
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
    t = (is4ofakind(cards, 2))
    o = (is4ofakind(cards, 2))
    if t == True and o == True:
        return True
    else:
        return False




def is_straight(cards):
    p = (conti(cards, 5))
    if p == True:
        return True
    else:
        return False




def is_high_card(cards):
    if (isRoyalFlush(cards)) == False and (is_straight_flush(cards)) == False and (is4ofakind(cards, 4)) == False and (is4ofakind(cards, 3)) == False and (is4ofakind(cards, 2)) == False and (is_full_house(cards)) == False and (is_flush(cards)) and (is_2_pair(cards)) == False and (is_straight_flush(cards)) == False:
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






