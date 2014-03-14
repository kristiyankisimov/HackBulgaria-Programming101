def list_to_number(digits):
    result = digits[0]
    for i in digits[1::]:
        result = result * 10 + i
    return result