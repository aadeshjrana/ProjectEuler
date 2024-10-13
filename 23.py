def is_abundant(n):
    sum_divisors = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors > n

def generate_abundant_numbers(limit):
    abundant_numbers = []
    for i in range(12, limit + 1):
        if is_abundant(i):
            abundant_numbers.append(i)
    return abundant_numbers

def cannot_be_sum(limit, abundant_numbers):
    can_be_written = [False] * (limit + 1)
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            sum_abundant = abundant_numbers[i] + abundant_numbers[j]
            if sum_abundant <= limit:
                can_be_written[sum_abundant] = True
            else:
                break
    sum_of_non_abundant = sum(i for i in range(1, limit + 1) if not can_be_written[i])
    return sum_of_non_abundant

limit = 28123
abundant_numbers = generate_abundant_numbers(limit)
result = cannot_be_sum(limit, abundant_numbers)
print(result)
