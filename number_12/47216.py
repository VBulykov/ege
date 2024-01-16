for n in range(100):
    s = '>' + '0' * 39 + '1' * n + '2' * 39
    
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    
    summa = s.count('1') + s.count('2') * 2

    del_k = 0
    for i in range(1, summa + 1):
        if summa % i == 0:
            del_k += 1
        if del_k > 2:
            break
    
    if del_k == 2:
        print(n)
        break
        

123456