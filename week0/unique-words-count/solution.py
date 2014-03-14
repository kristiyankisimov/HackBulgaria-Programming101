def unique_words_count(arr):
    unique_words = []
    for item in arr:
        if not item in unique_words:
            unique_words.append(item)
    return len(unique_words)