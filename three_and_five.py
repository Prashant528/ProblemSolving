def three_and_five(number):
    if number < 8:
        raise Exception
    if number == 8:
        return 1, 1
    if number % 3 == 0:
        return number / 3, 0
    if number % 5 == 0:
        return 0, number / 5
    if number % 8 == 0:
        return number/8, number/8
    fives = 0
    while number % 3 != 0:
        fives += 1
        number -= 5
    return number/3, fives