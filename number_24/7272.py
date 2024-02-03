s = open('24_7272.txt').readline()

s = s.replace('AB', 1)
s = s.replace('CB', 1)

k = 1
m = 0
for i in range(len(s) - 1):
    if s[i] == 1 == s[i+1]:
        k += 1
        m = max(m, k)
    else:
        k = 1

print(m)