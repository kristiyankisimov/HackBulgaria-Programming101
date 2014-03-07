def contains_digit(number, digit):
    while number > 0:
        if number % 10 == digit:
            return True
        number //= 10
    return False

def contains_digits(number, digits):
    return all([contains_digit(number, digit) for digit in digits])