f = open('9_12241.csv')
stroki = []
for i in f:
    stroka = str(i)
    stroki.append(stroka)
f.close()

stroki_list = []
for i in stroki:
    stroka = i.split(',')
    stroki_list.append(stroka)

for i in range(len(stroki_list)):
    stroki_list[i] = list(map(int, stroki_list[i]))

k = 0
for el in stroki_list:
    mn = set(el)
    k1 = k2 = 0
    sp2 = []
    for num in mn:
        if el.count(num) == 1:
            k1 += 1
            uniq = num
        elif el.count(num) == 2:
            k2 += 1
            sp2.append(num)
    
    if k1 == 1 and k2 == 3:
        if (max(sp2) + min(sp2)) / 2 < uniq:
            k += 1

print(k)