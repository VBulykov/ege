f = open('8666.csv', 'r')
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
    
    if max(i) > (sum(i) - max(i)):
        vtoroe = True
    
    if pervoe != vtoroe:
        k += 1

print(k)