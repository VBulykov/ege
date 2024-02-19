from itertools import permutations

alphabet = 'макака'
m = set()

for s in permutations(alphabet):
    slovo = ''.join(s)

    if 'кк' not in slovo and 'аа' not in slovo:
        m.add(slovo)

print(len(m))