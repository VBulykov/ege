from itertools import *
k = 0

for s in product('012345678', repeat=5):
    slovo = ''.join(s)
    
    if slovo[0] != '0':
        if slovo.count('3') == 2:
            if '21' in slovo or '23' in slovo or '25'in slovo or '27'in slovo or '12' in slovo or '32' in slovo or '52' in slovo or '72' in slovo:
                pass
            else:
                k += 1    
                #for el in slovo:

                    #if el in '1357':
                    #    pass

print(k)