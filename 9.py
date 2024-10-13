def pythagorean_triplet(target_sum):
    for a in range(1, target_sum // 3):
        for b in range(a + 1, target_sum // 2):
            c = target_sum - a - b
            if a**2 + b**2 == c**2:
                return a, b, c, a * b * c

triplet = pythagorean_triplet(1000)
print(f"{triplet[3]}")
