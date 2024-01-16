from itertools import *
num = 1

for s in product('БГЛНОУШ', repeat=4):  
    print(s)  
    stroka = ''.join(s)

    if num % 2 != 0:
        if stroka[0] != 'Б':
            if stroka.count('Н') >= 2:
                if 'У' not in stroka:
                    print(num)

    num += 1