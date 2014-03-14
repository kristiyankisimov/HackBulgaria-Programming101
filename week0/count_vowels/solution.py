def count_vowels(str):
    count = 0
    vowels = "aeouiy"
    for i in str:
        if i.lower() in vowels:
            count += 1
    return count