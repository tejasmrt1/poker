from cards.util.contiguous import contiguous_cards


def is_straight(cards):
    return contiguous_cards(cards, 5)