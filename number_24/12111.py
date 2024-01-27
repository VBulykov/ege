s = open('24_12111.txt').readline()

s = s.replace('HPY', '1')
s = s.replace('NYN', '2')

k = 1
m = 1

for i in range(len(s) - 1):
    if s[i] + s[i+1] in ['11', '22', '21', '12']:
        k += 1
        m = max(m, k)
    else:
        k = 1

print(m)