def is_prime(n):
    if n < 2:
        return False
    return sum([i for i in range(1, n + 1) if n % i == 0]) == n + 1

def generate_primes(n):
    return [i for i in range(2, n + 1) if is_prime(i) == True]

def power_of_prime(number, prime):
    power = 0
    while number % prime == 0:
        number //= prime
        power += 1
    return power

def prime_factorization(n):
    l = generate_primes(n)
    result = []
    for i in l:
        result.append((i, power_of_prime(n, i)))
    return list(filter(lambda x: x[1] != 0, result))