from itertools import *

alphabet = 'СПОРТЛОТО'
k = 1
spisok = []

for s in set(permutations(alphabet)):
    slovo = ''.join(s)
    if slovo[0] != 'О' and slovo[-1] != 'О':
        spisok.append(slovo)

spisok = sorted(spisok)
print(spisok[-1])
print(len(spisok))


'''
[ A B C]
  0 1 2
  1 2 3

len([]) = 3
'''