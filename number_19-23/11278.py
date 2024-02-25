def f(a, b, m):
    if a + b >= 449:
        return m % 2 == 0
    
    if m == 0:
        return 0
    
    h = [f(a * 2, b, m - 1), f(a, b * 2, m - 1), f(a + 1, b, m-1), f(a, b + 1, m-1)]

    if m % 2 != 0:
        return any(h)
    else:
        return any(h)#меняем на any() в первой задаче в 2 и 3 all()

#петя 1
a = 11
print(min([s for s in range(1, 436) if f(a, s, 2)]))
#110
print([s for s in range(1, 436) if not f(a, s, 1) and f(a, s, 3)])

print(min([s for s in range(1, 436) if not f(a, s, 2) and f(a, s, 4)]))