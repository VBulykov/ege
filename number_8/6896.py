from itertools import *
alphabet = sorted('АЛГОРИТМ')
slova = []

for s in product(alphabet, repeat=5):
    slovo = ''.join(s)
    slova.append(slovo)

for slovo in sorted(slova, reverse=True):
    if (
        (slova.index(slovo) + 1) % 2 == 1 and
        slovo[0] != 'Т' and 
        slovo.count('Г') == 2
    ):
        print(slovo)
        print(slova.index(slovo) + 1)
        break