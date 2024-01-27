s = open('24_10724.txt').readline()

alphabet = '0123456789ABCDEF'
#alphabet = sorted('1234567890qwertyuiopasdfghjklzxcvbnm'.upper())
#print(alphabet[:16])

k = 0
m = 0

for el in s:
    if el in alphabet:
        if el != '0':
            k += 1

    else:
        k = 0
    
    m = max(m, k)



print(m) 