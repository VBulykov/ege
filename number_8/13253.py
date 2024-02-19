from itertools import product

s1 = []
s2 = []
alphabet1 = 'конец'
alphabet2 = 'дракон'

for s in product(alphabet1, repeat=5):
    slovo = ''.join(s)
    
    s1.append(slovo)

for s in product(alphabet2, repeat=5):
    slovo = ''.join(s)
    
    s2.append(slovo)

k = 0

for element in s1:
    if element not in s2:
        k += 1

for element in s2:
    if element not in s1:
        k += 1

print(k)