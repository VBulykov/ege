from itertools import *
alphabet = '01234567'
k = 0


for s in permutations(alphabet, 5):
    slovo = ''.join(s)
    slovo_2 = slovo

    if slovo[0] != '0':
        if '1' not in slovo:
            for el in slovo:
                if int(el) % 2 == 0:
                    slovo = slovo.replace(el, 'A')
                else:
                    slovo = slovo.replace(el, 'B')
            
            if 'AA' not in slovo and 'BB' not in slovo:
                k += 1
print(k)