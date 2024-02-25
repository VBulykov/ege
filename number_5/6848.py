N = []

for n in range(1, 1000000):
    n_oct = oct(n)[2:]
    if len(n_oct) == 4:
        summa1 = int(str(n)[0]) + int(str(n)[-1])
        summa2 = int(str(n)[1]) + int(str(n)[2])
        R = int(str(min(summa1, summa2)) + str(max(summa1, summa2)))
        if R == 317:
            N.append(n)

print(min(N) + max(N))