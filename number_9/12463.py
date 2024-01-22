f = open('9_12463.csv', 'r')
stroki = []
k = 0
for i in f:
    stroki.append(list(
            map(int, i.split(','))
        )
    )

for stroka in stroki:
    list_count = [stroka.count(el) for el in stroka]
    if sum(list_count) == 23 and len(set(stroka)) == 5:
        max_el = min(stroka)
        for el in stroka:
            if stroka.count(el) > 1:
                max_el = max(max_el, el)
        
        if ((
                sum([el for el in stroka if stroka.count(el) == 1]) / 3
            ) >= max_el
        ):
            k += 1
        
print(k)