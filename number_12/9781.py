maximum = 0

l = []

for n in range(4, 10000):
    s = '1' + n * '2'

    while '12' in s or '322' in s or '222' in s:
        if '12' in s:
            s = s.replace('12' , '2', 1)
        if '322' in s:
            s = s.replace('322' , '21', 1)
        if '222' in s:
            s = s.replace('222' , '3', 1)

    summa = s.count('1') + s.count('2') * 2 + s.count('3') * 3
    l.append(summa)

print(max(l))