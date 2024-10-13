def sum_of_fifth_powers():
    total = 0
    for i in range(2, 1000000):
        if i == sum(int(digit)**5 for digit in str(i)):
            total += i
    return total

print(sum_of_fifth_powers())
