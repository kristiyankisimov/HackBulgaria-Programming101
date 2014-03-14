def sevens_in_a_row(arr, n):
    if n == 0:
        return True
    length = len(arr)
    for i in range(length):
        if arr[i] == 7 and (i + n) <= length and all(map(lambda x: x == 7, arr[i:i + n:])):
            return True
    return False