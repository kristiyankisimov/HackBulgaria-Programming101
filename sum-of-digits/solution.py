def sum_of_digits(n):
    sum = 0
    k = abs(n)
    while k != 0:
        sum += k % 10
        k = k // 10
    return sum