def fibonacci_index(n):
    a, b = 1, 1
    index = 2
    while True:
        a, b = b, a + b
        index += 1
        if len(str(b)) >= n:
            return index

print(fibonacci_index(1000))
