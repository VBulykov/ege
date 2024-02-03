for n in range(1, 10000):
    n_ishodnoe = n
    #1 пункт
    n_tri = ''
    '''while n > 0:
        n_tri += str(n % 3)
        n //= 3 
    n_tri = n_tri[::-1]'''
    
    while n > 0:
        n_tri = str(n % 3) + n_tri
        n //= 3
    #второй пункт
    if n_ishodnoe % 2 == 0:
        n_tri = '1' + n_tri + '00'
    else:
        summa = n_tri.count('1') + n_tri.count('2') * 2
        summa_tri = ''
        while summa > 0:
            summa_tri = str(summa % 3) + summa_tri
            summa //= 3
        
        n_tri = n_tri + summa_tri
    
    if int(n_tri, 3) > 168:
        print(n_ishodnoe)
        break