f = open('8667.csv', 'r')
s = []
k = 0

for i in f:
    s.append(i.split(','))

for i in s:
    i[-1] = i[-1].replace('\n', '')
    for j in range(len(i)):
        i[j] = int(i[j])

for i in s:
    pervoe = False
    vtoroe = False

    if len(i) == len(set(i)):
        pervoe = True
    
    maximum = max(i)
    minimum = min(i)

    if 5 * (maximum + minimum) >= 3 * (sum(i) - maximum - minimum):
        vtoroe = True
    
    if pervoe == vtoroe == True:
        k += 1

print(k)