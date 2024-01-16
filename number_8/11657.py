from itertools import *

k = 0
chetnie = '0246'

for s in product('01234567', repeat=6):
    slovo = ''.join(s)

    if slovo[0] != '0' and slovo.count('3') == 0:
        if len(set(slovo)) == len(slovo):
            for c in chetnie:
                slovo = slovo.replace(c, 'A')
            if 'AA' in slovo:
                k += 1

print(k)