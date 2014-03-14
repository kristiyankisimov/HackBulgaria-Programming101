def count_substrings(heystack, needle):
    count, i = 0, 0
    while i < len(heystack):
        if heystack[i : i + len(needle)] == needle:
            i += len(needle)
            count += 1
        else:
            i += 1
    return count