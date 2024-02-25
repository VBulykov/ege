def f(s, m):
    if s >= 275:
        return m % 2 == 0
    
    if m == 0:
        return 0
    
    h = [
        f(s * 2, m - 1), f(s + 3, m - 1)
    ]

    if m % 2 == 1:
        return any(h)
    else:
        return all(h)    #если противник проиграл то any

def f(a, b, m):
    if a + b >= 275:
        return m % 2 == 0
    
    if m == 0:
        return 0
    
    h = [
        f(a, b + 3, m - 1), f(a + 3, b, m - 1),
        f(a, b + 7, m - 1), f(a + 7, b, m - 1),
        f(a, b * 4, m - 1), f(a * 4, b, m - 1)
    ]

    if m % 2 == 1:
        return any(h)
    else:
        return all(h)    #если противник проиграл то any