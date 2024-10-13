def score(name, pos):
    letter_scores = {chr(i): i - 64 for i in range(65, 91)}  
    name_score = sum(letter_scores.get(letter, 0) for letter in name) 
    return name_score * pos

with open('D:/ProjectEuler/22/names.txt') as f:
    names = sorted(f.read().replace('"', '').split(','))  

total_score = 0

for pos, name in enumerate(names, start=1): 
    total_score += score(name, pos)

print(total_score)
