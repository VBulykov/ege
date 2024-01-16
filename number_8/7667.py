from itertools import *
k = 0

for s in product('ЕГЭ', repeat=5):
    slovo = ''.join(s)

    if slovo[0] == 'Е' or slovo[0] == 'Э':
        k += 1

print(k)