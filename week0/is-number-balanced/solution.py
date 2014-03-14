def number_to_list(n):
    l = []
    while n > 0:
        l.append(n % 10)
        n //= 10
    return l

def is_number_balanced(n):
    as_list = number_to_list(n)
    length = len(as_list)
    if length % 2 == 0:
        return sum(as_list[0:length // 2:]) == sum(as_list[length // 2:length:])
    return sum(as_list[0:length // 2:]) == sum(as_list[length // 2 + 1:length:])