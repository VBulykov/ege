def f(s, m):
    if s >= 129:
        return m % 2 == 0
    
    if m == 0:
        return 0
    
    h = [f(s + 1, m - 1), f(s * 2, m - 1)]
    
    if m % 2 == 0:
        return any(h)
    else:
        return all(h)

print([s for s in range(1, 129) if f(s, 1) or f(s, 3)])
print([s for s in range(1, 129) if f(s, 4) and not f(s, 2)])
print([s for s in range(1, 129) if f(s, 5) and not f(s, 1) and not f(s, 3)])