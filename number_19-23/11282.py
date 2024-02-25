def f(s, m):
    if s >= 273:
        return m % 2 == 0
    
    if m == 0:
        return 0
    
    h = [
        f(s + 2, m - 1), f(s + 5, m - 1), f(s * 4, m - 1)
    ]

    if m % 2 == 1:
        return any(h)
    else:
        return any(h)
    

print(min([s for s in range(1, 273) if f(s, 2) and not f(s, 1)]))