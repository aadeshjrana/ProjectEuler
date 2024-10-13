def is_prime(n):
  for i in range(2, n//2 + 1):
    if n % i == 0:
      return False
    return True

number = 600851475143

done = False

while not done:
  for i in range(2, 600851475143):
    if is_prime(i):
      if number % i == 0:
        number/= i
        if number == 1:
          print(i)
          done = True
          break
