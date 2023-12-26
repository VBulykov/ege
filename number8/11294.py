from itertools import *
k = 0

for s in product('ДГШЯБЖ', repeat=6):
    slovo = ''.join(s)

    if slovo.count('Я') == 1:
        k += 1

print(k)