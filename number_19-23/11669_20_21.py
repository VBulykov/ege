def f(s, m):
    if s < 117:
        return m % 2 == 0

    if m == 0:
        return 0
    
    h = [
        f(s - 7, m - 1), f(s // 3, m - 1)
    ]

    if m % 2 == 1:
        return any(h)
    else:
        return all(h)

print([
    s for s in range(117, 10001) if f(s, 3) and not f(s, 2) and not f(s, 1)
])
print([s for s in range(117, 10001) if not f(s, 2) and f(s, 4)])