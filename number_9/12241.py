f = [s for s in open('12241.csv', 'r')]
stroki = []
k = 0
for i in f:
    stroki.append(list(
            map(int, i.split(','))
        )
    )

for stroka in stroki:
    list_count = [stroka.count(el) for el in stroka]
    if list_count.count(2) == 6 and list_count.count(1) == 1:
        maximum = max([el for el in stroka if stroka.count(el) == 2])
        minimum = min([el for el in stroka if stroka.count(el) == 2])
        for element in stroka:
            if stroka.count(element) == 1:
                nepovt = element
        
        if (maximum + minimum) / 2 < nepovt:
            k += 1

print(k)