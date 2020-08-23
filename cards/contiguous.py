def conti_starting_from(numbers, how_many, starting_index):
    for i in range(starting_index, starting_index + how_many - 1):  # 0, 1, 2, 3, 4, 5
        if numbers[i + 1] - numbers[i] != 1:
            return False
    return True


def conti(numbers, how_many):
    for starting_index in range(0, len(numbers) - how_many + 1):
        if conti_starting_from(numbers, how_many, starting_index):
            return True
    return False
