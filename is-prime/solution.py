def is_prime(n):
    if n < 2:
        return False
    return sum([i for i in range(1, n + 1) if n % i == 0]) == n + 1