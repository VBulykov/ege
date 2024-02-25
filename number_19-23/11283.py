def f(a, b, m):
    if a + b >= 342:
        return m % 2 == 0
    
    if m == 0:
        return 0
    
    h = [f(a+2, b, m-1), f(a, b*5, m-1), f(a, b + 2, m-1), f(a*5, b, m-1)]

    if (m - 1) % 2 == 0:
        return any(h) 
    else:
        return all(h)

a = 11

print(min([s for s in range(1, 326) if f(a, s, 2)]))
#14
print([s for s in range(1, 326) if not f(a, s, 1) and f(a, s, 3)])

print([s for s in range(a, 326) if not f(a, s, 2) and f(a, s, 4)])