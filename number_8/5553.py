from itertools import *


vowels = 'ОА'
alphabet = 'СОТОЧКА'
k = 0


for s in set(permutations(alphabet, 7)):
    slovo = ''.join(s)

    for bukva in slovo:
        if bukva in vowels:
            slovo = slovo.replace(bukva, '8')

    if '88' in slovo:
        k += 1


print(k)