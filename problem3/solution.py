def sum_of_divisors(n):
    sum_of_divisorss = 1
    for i in range(2, n + 1):
        if n % i == 0:
            sum_of_divisorss += i
    return sum_of_divisorss
