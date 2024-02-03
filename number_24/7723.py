from itertools import product
s = open('24_7723.txt').readline()

comb = ['11D', '11R', '18D', '18R', '81D', '81R', '88D', '88R']

for c in comb:
    s = s.replace(c, 'X')

k = 0
maximum = 0
for i in range(len(s)):
    if s[i] == 'X':
        k += 1
        maximum = max(maximum, k)
    else:
        k = 0

print(maximum)