from itertools import permutations

alphabet = 'просто'
k = 0
sp = set()

for s in permutations(alphabet):
    slovo = ''.join(s)

    if 'оо' not in slovo:
        sp.add(slovo)

print(len(sp))