f = open('8946.csv','r')
s = []
k = 0

for stroka in f:
    s.append(stroka.split(','))

for stroka in s:
    for i in range(len(stroka)):
        if i == 4:
            stroka[i] = int(stroka[-1].replace('\n', ''))
        else:
            stroka[i] = int(stroka[i])

for stroka in s:
    pervoe = False
    vtoroe = False
    proizvedenie = 1

    for chislo in stroka:
        proizvedenie *= chislo
    
    max_1 = max(stroka)
    proizvedenie /= max_1

    if proizvedenie < max(stroka)**2:
        pervoe = True

    stroka_2 = stroka
    stroka_2.remove(max(stroka_2))

    max_2 = max(stroka_2)
    stroka_2.remove(max_2)

    if (max_1 + max_2) / 2 >=  sum(stroka_2):
        vtoroe = True

    if pervoe == vtoroe == True:
        k += 1

print(k)