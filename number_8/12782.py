from itertools import product

alphabet = 'ЯЩЕР'
k = 0

for s in product(alphabet, repeat=5):
    slovo = ''.join(s)

    if 'Е' in slovo and slovo.count('Е') <= 3:
        k += 1

print(k)