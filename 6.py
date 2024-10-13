sum_sq = sum([i**2 for i in range(1, 101)])
sq_sum = sum([i for i in range(1, 101)])**2

print(sq_sum - sum_sq)
