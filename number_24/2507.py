#извлекаем строки из файла в переменную S
s = [el for el in open('24_2507.txt')]

#находим номер строки с самой длинной цепочкой
maximum = 1
k = 0
n = -1
for i in range(len(s)):
    for j in range(len(s[i]) - 1):
        if s[i][j] == s[i][j+1]:
            k += 1
            if maximum < k:
                maximum = k
                n = i
        else:
            k = 0
#выводим на экран строку с самой длинной цепочкой
print(n)
#создаем алфавит в алфавитном порядке
alphabet = sorted('qwertyuiopasdfghjklzxcvbnm'.upper())
#создаем список с количеством каждой буквы в строке с самой длинной цепочкой
A = []
for bukva in alphabet:
    A.append(s[n].count(bukva))

#сохранили букву которая встречается больше всего раз внутрь перменной буква
BUKVA = alphabet[A.index(max(A))]
print(BUKVA)
'''
maximum_bukva_str = 0
BUKVA = 'A'
A = []
for bukva in alphabet:
    if maximum_bukva_str < s[n].count(bukva):
        maximum_bukva_str = s[n].count(bukva)
        BUKVA = bukva
'''

#считаем количество повторений буквы в файле
summa = 0
for stroka in s:
    summa += stroka.count(BUKVA)
#выводим букву и количество повторений
print(BUKVA, summa)