def f(a, b, m):
    if a >= 40 or b >= 40:
        return m % 2 == 0
    
    if m == 0:
        return 0

    if a > b:
        h = [
                f(a, b * 2, m - 1), 
            f(a + 1, b, m - 1), 
            f(a + 2, b, m - 1), 
            f(a + 3, b, m - 1)
        ]
    elif b > a:
        h = [
                f(a * 2, b, m - 1), 
            f(a, b + 1, m - 1), 
            f(a, b + 2, m - 1), 
            f(a, b + 3, m - 1)
        ]
    else:
        h = [
            f(a + 1, b, m - 1), f(a + 2, b, m - 1), f(a + 3, b, m - 1)
        ]

    if m % 2 != 0:
        return any(h)
    else:
        return all(h)

print(min([a + b for a in range(1, 40) for b in range(1, 40) if f(a, b, 1)]))
a = 11
print(min([s for s in range(1, 40) if not f(a, s, 1) and f(a, s, 3)]))
print(max([s for s in range(1, 40) if not f(a, s, 1) and f(a, s, 3)]))
a = 31
print([s for s in range(1, 40) if f(a, s, 4) and not f(a, s, 2)])