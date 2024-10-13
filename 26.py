def longest_recurring_cycle():
    max_cycle_length = 0
    max_d = 0
    for d in range(2, 1000):
        remainders = {}
        remainder = 1 % d
        position = 0
        while remainder not in remainders and remainder != 0:
            remainders[remainder] = position
            remainder = (remainder * 10) % d
            position += 1
        if remainder != 0:
            cycle_length = position - remainders[remainder]
            if cycle_length > max_cycle_length:
                max_cycle_length = cycle_length
                max_d = d
    return max_d

print(longest_recurring_cycle())

