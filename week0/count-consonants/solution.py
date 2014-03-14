def count_consonants(string):
    count = 0
    consonants = "bcdfghjklmnpqrstvwxz"
    for i in string:
        if i.lower() in consonants:
            count += 1
    return count