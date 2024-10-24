import random
def first_stone():
    stones = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    ston = random.choice(stones)
    return ston
n = first_stone()
parole = []

for i in range(1, n):
    for j in range(i+1, n):
        if n % (i+j) == 0 and i!=j:
            parole.append(i)
            parole.append(j)

parole = str(parole)
parole = parole.replace(',', '')
parole = parole.replace('[', '')
parole = parole.replace(']', '')
parole = parole.replace(' ', '')
parole = int(parole)

print(n, "result", parole)