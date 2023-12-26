from itertools import *
k = 0

for s in product('0123', repeat=3):
    slovo = ''.join(s)
    if s[0] != '0':
        if int(slovo[0]) + int(slovo[2]) > int(slovo[1]):
            k += 1

print(k)