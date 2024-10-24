import random
def first_stone():
    stones = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    ston = random.choice(stones)
    return ston
s = first_stone()
parole = []

for i in range(1, s):
    for j in range(i+1, s):
        if s % (i+j) == 0 and i!=j:
            parole.append(i)
            parole.append(j)

print(s, parole)










