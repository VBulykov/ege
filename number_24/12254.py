s = open('24_12254.txt').readline()
k = 1
maximum = 1

for i in range(len(s) - 1):
    if s[i] + s[i+1] in 'RSQR':
        k += 1
        maximum = max(maximum, k)
    else:
        k = 1

print(maximum)