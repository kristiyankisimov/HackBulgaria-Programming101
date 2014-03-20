def count_words(arr):
    dictionary = {}
    for item in arr:
        if not item in dictionary:
            dictionary[item] = 1
        else:
            dictionary[item] += 1
    return dictionary
