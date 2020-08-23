def contiguous_starting_from(numbers, how_many, starting_index):
    for i in range(starting_index, starting_index + how_many - 1):  # 0, 1, 2, 3, 4, 5
        if numbers[i + 1] - numbers[i] != 1:
            return False
    return True


def contiguous(numbers, how_many):
    numbers_list = list(numbers)
    numbers_list.sort()
    for starting_index in range(0, len(numbers_list) - how_many + 1):
        if contiguous_starting_from(numbers_list, how_many, starting_index):
            return True
    return False


def contiguous_cards(cards, how_many):
    return contiguous(map(lambda x: x.number, cards), how_many)

