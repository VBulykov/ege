def f(s, m):
    if s >= 129:
        return m % 2 == 1
    
    if m >= 3:
        return 0
    
    h = [f(s + 1, m - 1), f(s * 2, m - 1)]
    
    if m % 2 == 1:
        return all(h)
    else:
        return any(h)
    

print([s for s in range(1, 129) if f(s, 2) or not f(s, 1) or not f(s, 3)])