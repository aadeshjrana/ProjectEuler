import math

def routes_in_grid(n):
    return math.comb(2 * n, n)

result = routes_in_grid(20)
print(result)
