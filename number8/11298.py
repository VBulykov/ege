from itertools import *

k = 0
n = 1

for s in product('АЖЗОПЮ', repeat=6):
    slovo = ''.join(s)

    if n % 2 == 0:
        if slovo[0] == 'А':
            if slovo.count('З') >= 2:
                k += 1
    n += 1

print(k)