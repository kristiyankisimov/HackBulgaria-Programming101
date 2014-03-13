def is_an_bn(word):
    if len(word) % 2 == 1:
        return False
    else:
        first = word[:len(word)//2]
        second = word[len(word)//2+1:]
    is_true_first = all(map(lambda x: True if x == 'a' else False, first))
    is_true_second = all(map(lambda x: True if x == 'b' else False, second))
    return is_true_first and is_true_second