from itertools import *
k = 0

for s in product('0123456', repeat=6):
    slovo = ''.join(s)
    if slovo.count('6') == 1 and slovo[0] != '0':
        for element in slovo:
            if int(element) % 2 != 0:
                slovo = slovo.replace(element, 'A')
            else:
                slovo = slovo.replace(element, 'B')    

        if slovo == 'ABABAB' or slovo == 'BABABA':
            k += 1

print(k)