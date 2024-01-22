f = [s for s in open('9-225.csv', 'r')]

stroki = []
k = 0

for i in f:
    stroki.append(list(
            map(int, i.split(','))
        )
    )

for stroka in stroki:
    list_count = [stroka.count(el) for el in stroka]
    stroka = sorted(stroka)
    if list_count.count(2) == 2 and list_count.count(1) == 3:
        if (
            (stroka[0] + stroka[4])**2 < (stroka[1]**2 + stroka[2]**2 + stroka[3]**2)
        ):
            k+=1

print(k)