def count_divisors(n):
    if n in memo:
        return memo[n]
    
    c = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            c += 1
            if i != n // i:
                c += 1
    
    memo[n] = c
    return c

def find_triangle(l):
    n = 1
    t_num = 0
    global memo
    memo = {}

    while True:
        t_num += n
        d_count = count_divisors(t_num)

        if d_count > l:
            return t_num
        
        n += 1

print(find_triangle(500))
