def d(n):
  t = 0
  for i in range(1, n // 2 + 1):
    if n % i == 0:
      t += i
  return t

def find(l):
  anum = set()
  for a in range(2, l + 1):
    b = d(a)
    if b > a and b < l:
      if d(b) == a:
        anum.add(a)
        anum.add(b)
  return sum(anum)

print(find(10000))
