from cards.PokerHands import is_of_a_kind


def is_two_pair(cards):
    first_pair = (is_of_a_kind(cards, 2))
    second_pair = (is_of_a_kind(cards, 2))
    if first_pair == True and second_pair == True:
        return True
    else:
        return False