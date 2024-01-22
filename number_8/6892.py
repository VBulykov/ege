from itertools import *
alphabet = '012345'
k = 0
for s in product(alphabet, repeat=6):
    slovo = ''.join(s)
    for bukva in '135':
        slovo = slovo.replace(bukva, 'A')
    if (
        slovo[0] != '0' and 
        slovo.count('2') == 1 and 
        ('A2' not in slovo) and ('2A' not in slovo)
    ):
        k += 1

print(k)