def d(n, m):
    return n % m == 0

B = [i for i in range(120, 131)]

for A in range(1, 10000):
    for x in range(1, 10000):
        if not(((x in B) <= (not(d(x, 7)))) or (A > 2 * x)):
            break
    else:
        print(A)
        break