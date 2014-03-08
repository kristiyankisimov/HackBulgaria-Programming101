def number_to_list(n):
    to_list = []
    while n > 0:
        to_list.append(n % 10)
        n //= 10
    return to_list[::-1]