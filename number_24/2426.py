s = open('24_2426.txt').readline()
s = s.replace('B', 'A')
s = s.replace('C', 'A')
s = s.split('A')
print(max(map(len, s)))

#2423