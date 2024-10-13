def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def quadratic_primes(a, b):
    n = 0
    while True:
        if not is_prime(n**2 + a*n + b):
            return n
        n += 1

max_primes = 0
max_a = 0
max_b = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        primes = quadratic_primes(a, b)
        if primes > max_primes:
            max_primes = primes
            max_a = a
            max_b = b

print(max_a * max_b)
