from itertools import product

alphabet = '0123456789'
chet   = '02468'
nechet = '13579'
k = 0

for s in product(alphabet, repeat=7):
    slovo = ''.join(s)

    if slovo[0] != '0':
        if len(slovo) == len(set(slovo)):
            for chislo in chet:
                slovo = slovo.replace(chislo, 'A')
            
            for chislo in nechet:
                slovo = slovo.replace(chislo, 'B')
            
            if 'AA' not in slovo and 'BB' not in slovo:
                k += 1

print(k)