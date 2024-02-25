def f(s, m):
    if s >= 429:
        return m % 2 == 0
    
    if m == 0:
        return 0
    
    h = [
        f(s + 5, m - 1), f(s * 5, m - 1)
    ]

    if m % 2 == 1:
        return any(h)
    else:
        return all(h)
    
print(min([s for s in range(1, 429) if f(s, 2) and not f(s, 1)]))