s = open('24_7891.txt').readline()

A = []
for i in '0123456789QWERTYUIOPASDFGHJKLZXCVBNM':
    for q in s.split(i):
        A.append(len(q) + 2)
        
print(max(A))