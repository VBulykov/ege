from itertools import *

alphabet = 'ЛЕВИОСА'
vowels = 'АОИЕ'
consonants = 'ЛВС'

k = 0

for s in permutations(alphabet):
    slovo = ''.join(s)
    if slovo[0] not in vowels:
        if slovo[3] not in consonants:
            k += 1

print(k)