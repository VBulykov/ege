k = 0

g_spisok = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in range(10, 100):
    g_spisok.append(g_spisok[n-2] + 1)


f_spisok = [g_spisok[i-1] for i in range(1, 101)]
f_spisok.insert(0, 0)


for num in f_spisok:
    for el in [1, 4, 9, 16, 25, 36, 49]:
        if num == el:
            k += 1
            break

print(k)