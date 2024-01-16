k = 100000000000000000000
stroki = []


for i in range(101, 1000):
    s = '1' * i

    while '111' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '11', 1)

    if k > s.count('1'):
        k = s.count('1')

print(k)

for j in range(101, 1000):
    s2 = '1' * j
    length = j
    
    while '111' in s2:
        s2 = s2.replace('111', '22', 1)
        s2 = s2.replace('222', '11', 1)
    
    if s2.count('1') == k:
        print(length)
        break