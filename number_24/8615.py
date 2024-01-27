s = open('24_8615.txt').readline()

for el in 'ABCDEF':
    s = s.replace(el, '1')

k = 3
m = 0

s = s.replace('111', ' ')
s = s.replace(' ', '11 11')
sp = s.split(' ')
print(max([len(el) for el in sp]))
'''for i in range(1, len(s) - 1):
    if s[i-1] + s[i] + s[i] != '111':
        k += 1
        m = max(m, k)
    else:
        k = 3'''

#print(m)