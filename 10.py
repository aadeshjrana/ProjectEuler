def p(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
    
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
                
    return sum(i for i, is_prime in enumerate(primes) if is_prime)

print(p(2000000))
