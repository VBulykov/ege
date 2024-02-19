f = open('09_9156.csv', 'r')

k = 0

stroki = []
for i in f:
    stroki.append(i.split(','))


for i in range(len(stroki)):
    stroki[i][-1] = stroki[i][-1].replace('\n', '')

for s in stroki:
    pervoe = False
    vtoroe = False

    for i in range(len(s)):
        s[i] = int(s[i])
    
    if (max(s) + min(s)) % 3 == 0:
        pervoe = True
        
    if abs(s[0] - s[1]) == abs(s[2] - s[3]) or abs(s[0] - s[2]) == abs(s[1] - s[3]) or abs(s[0] - s[3]) == abs(s[1] - s[2]):
        vtoroe = True
    
    if pervoe == True == vtoroe:
        k += 1

print(k)