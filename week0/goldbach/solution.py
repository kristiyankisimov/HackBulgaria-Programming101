def is_prime(n):
    if n < 2:
        return False
    return sum([div for div in range(1, n + 1) if n % div == 0]) == n + 1

def goldbach(n):
    l = []
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            l.append((i, n-i))
    return l