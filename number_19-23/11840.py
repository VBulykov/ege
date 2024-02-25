def f(a, b, m):
    #a - первая куча
    #b - вторая куча

    if a + b >= 375:
        return m % 2 == 0
    
    if m == 0:
        return 0
    
    h = [
        f(a + 3, b, m - 1), f(a, b + 3, m - 1), 
        f(a * 2, b, m - 1), f(a, b * 2, m - 1)
    ]
    #первое условие
    if (m - 1) % 2 == 0:
        return any(h)
    else:
        return any(h)

    #второе и третье условие
    '''if (m - 1) % 2 == 0:
        return any(h)
    else:
        return all(h)'''

a = 27
#петя - 1

print(min([s for s in range(1, 348) if f(a, s, 2) and not f(a, s, 1)]))

print(min([s for s in range(1, 348) if f(a, s, 3) and not f(a, s, 1)]))
print(max([s for s in range(1, 348) if f(a, s, 3) and not f(a, s, 1)]))

print(min([s for s in range(1, 348) if f(a, s, 4) and f(a, s, 4)]))