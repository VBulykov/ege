from itertools import *
k = 0

for s in product('0123456', repeat=5):
    slovo = ''.join(s)
    if slovo.count('5') == 1 and slovo[0] != '0':
        for element in slovo:
            if int(element) % 2 == 0:
                slovo = slovo.replace(element, 'A')

        if 'A5' not in slovo and '5A' not in slovo:
            k += 1


print(k)