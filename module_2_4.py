number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes = []
not_primes = []
number_ = number
for i in number_:
    for j in range(2, i):
        if i % j == 0:       # делится ли каждое i на какое-нибудь j. Если да - это i не простое
            not_primes.append(i)
set_ =set(not_primes)    # убрать
not_primes = list(set_)  # повторы
for i in not_primes:         # удаляем из number_ не простые, остаются простые и (1)
    for j in number_:         #
        if i == j:             #
            number_.remove(i)    #
if 1 in number_:
    number_.remove(1)
primes = primes + number_
print('Primes: ',primes)
print('Not Primes ',not_primes)