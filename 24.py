import math

def millionth_permutation():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    index = 1000000 - 1  
    result = []

    for i in range(9, -1, -1):
        factorial = math.factorial(i)
        digit_index = index // factorial
        index %= factorial
        result.append(digits[digit_index])
        digits.pop(digit_index)

    return ''.join(map(str, result))

print(millionth_permutation())
