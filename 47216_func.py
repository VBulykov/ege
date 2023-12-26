def func(n):
    IsPrime = [True] * (n + 1)
    IsPrime[0] = False
    IsPrime[1] = False
    d = 2
    
    while d * d <= n:
        if IsPrime[d]:
            for i in range(d * d, n + 1, d):
                IsPrime[i] = False
        d += 1

    return IsPrime

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


    if func(summa + 1)[summa]:
        print(n)
        break