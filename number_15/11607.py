def d(n, m):
    return n % m == 0

for A in range(20000, 1, -1):
    if all((((not(d(x, 263) <= d(x,A))) and d(x, 71)) == 0) for x in range(1, 100000)):
        print(A)
        break