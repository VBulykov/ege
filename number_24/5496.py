s = open('24_5496.txt').readline()
s = s.split('D')
ps = 'D'
maximum = []

for i in range(len(s)):
    if s[i].count('O') <= 2:
        ps = ps + s[i] + 'D'
        maximum.append(len(ps))
    else:
        ps = 'D'

print(max(maximum))