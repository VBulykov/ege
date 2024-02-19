def f(s, m):
    if s >= 21:
        return m % 2 == 0
    
    if m == 0:
        return 0
    
    h = [f(s + 1, m - 1), f(s * 2, m - 1)]

    if m % 2 != 0:
        return any(h)
    else:
        return all(h)
    

print([s for s in range(1, 21) if not f(s, 1) and f(s, 3)])
print([s for s in range(1, 21) if not f(s, 2) and f(s, 4)])
print([s for s in range(1, 21) 
       if f(s, 5) and
       not f(s, 1) and
       not f(s, 3)
    ])