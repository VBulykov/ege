from itertools import *
k = 0

for s in product('012345678', repeat=5):
    slovo = ''.join(s)
    
    if slovo[0] != '0':
        if slovo.count('3') == 2:
            for el in slovo:
                if el in '1357':
                    slovo = slovo.replace(el, 'A')

            if 'A2' in slovo or '2A'  in slovo:
                pass
            else:
                k += 1

print(k)