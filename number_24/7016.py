s = open('24_7016.txt').readline()

m = 0
k = 0

for i in range(len(s) - 1):
    if s[i] == 'A':
        for j in range(i + 1, len(s)):
            if s[j] == 'A':
                k = 0
                break
            elif s[j] == 'D':
                m = max(m, k)
                k = 0
                break
            else:
                k += 1
                
print(m + 2)