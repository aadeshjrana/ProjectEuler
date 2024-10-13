def fact(n):
    r = 1
    for i in range(1, n + 1):  
        r = r * i             
    return r

def sum_of_digits(number):
    total = 0
    for digit in str(number):
        total += int(digit)
    return total

def main():
    factorial = fact(100)
    digit_sum = sum_of_digits(factorial) 
    return digit_sum

print(main())

