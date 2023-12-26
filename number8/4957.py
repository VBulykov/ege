from itertools import *


vowels = 'АИЯ'
consonants = 'НСТ'
alphabet = 'АНАСТАСИЯ'
k = 0
first = False
second = False

for s in set(permutations(alphabet, 9)):
    slovo = ''.join(s)

    for bukva in slovo:
        if bukva in vowels:
            slovo = slovo.replace(bukva, 'A')
        else:
            slovo = slovo.replace(bukva, 'B')
    
    if not('AAA' in slovo and 'BBB' in slovo):
        k += 1

print(k)