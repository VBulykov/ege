s = open('24_9845.txt').readline()

for bukva in 'ABC':
    s = s.replace(bukva, 'A')

for cifra in '89':
    s = s.replace(cifra, '1')

k = m = 1

for i in range(len(s) - 1):
    if s[i] + s[i+1] in ['A1', '1A']:
        k += 1
        m = max(m, k)
    else:
        k = 1

print(m)