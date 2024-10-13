def longest_collatz_chain(limit):
    memo = {1: 1}
    max_length, starting_number = 0, 0
    
    for i in range(2, limit):
        n, length = i, 0
        while n != 1:
            if n in memo:
                length += memo[n]
                break
            length += 1
            n = n // 2 if n % 2 == 0 else 3 * n + 1
        memo[i] = length
        if length > max_length:
            max_length, starting_number = length, i
            
    return starting_number

print(longest_collatz_chain(1000000))
