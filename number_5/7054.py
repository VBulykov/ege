R_spisok = set() #set (множество) позволяет в себе хранить уникальные значения

for n in range(1, 10000):
    #bin(n)[2:] 0b
    #oct(n)[2:] 0o
    #hex(n)[2:] 0x
    n_ishodnoe = n
    #первый пункт
    n6 = ''
    while n > 0:
        n6 = str(n % 6) + n6
        n //= 6

    #второй
    if n_ishodnoe % 3 == 0:
        n6 = n6 + n6[:2]
    else:
        ost3 = n_ishodnoe % 3 * 10
        ost6 = ''
        while ost3 > 0:
            ost6 = str(ost3 % 6) + ost6
            ost3 //= 6
        
        n6 = n6 + ost6
    
    R = int(n6, 6)
    if R > 680:
        R_spisok.add(R)

#print(min(R_spisok))