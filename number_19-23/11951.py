words = ['АБВГДАБВГДХ', 'ДГВБАДГВБЕ']
print([len(word) for word in words])

#выиграл петя написав букву а
print('п1')

#нужна победа вани
s2 = 'ДГВБАДГВБЕ'
print('АГВБДДГВБЕ')

words = ['ВОРОНА', 'ВОЛК', 'ВОЛНА', 'МОРИС', 'МОРЯНА', 'МОРКОВЬ']

words1 = [word for word in words if len(word) % 2 == 1]
words2 = [word for word in words if len(word) % 2 == 0]
print(f'1 {words1}')
print(f'2 {words2}')

from itertools import product, permutations

s_3 = []
for s in product('АБ', repeat = 3):
    slovo = ''.join(s)
    s_3.append(slovo)

s_6 = []
for s in product('АБ', repeat = 6):
    slovo = ''.join(s)
    s_6.append(slovo)

k = 0
print(len(s_3))
print(s_3)
print(len(s_6))

for s3 in s_3:
    for s6 in s_6:
        if s3 != s6[:3]:
            if s3[0] == s6[0]:
                if s3[1] != s6[1]:
                    k += 1
                    print(s6)
                    print(s3)
                    break

print(k)