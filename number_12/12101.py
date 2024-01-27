for n in range(4, 1000):
    s = '9' + '4' * n
    k = s.count('4')
    while '94' in s or '644' in s or '444' in s:
        if '94' in s:
            s = s.replace('94', '4', 1)
        if '644' in s:
            s = s.replace('644', '49', 1)
        if '444' in s:
            s = s.replace('444', '6', 1)
        
    if k / 18 == s.count('4'):
        print(n)
        break