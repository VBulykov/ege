f = open('7080.txt', 'r')
numbers = [int(stroka) for stroka in f]
f.close()

#numbers_68 = [str(i) for i in numbers if str(i)[-2:] == '68']
#print(numbers_68)

kolvo = 0
summa = []
maximum = max([i for i in numbers if str(i)[-2:] == '68'])

for i in range(len(numbers) - 3):
    chetverka = [
        numbers[i], numbers[i+1], numbers[i + 2], numbers[i+3]
    ]
    k = 0
    for el in chetverka:
        if len(str(abs(el))) == 2:
            k += 1

    if k == 1 or k == 4:
        if sum(chetverka) >= maximum:
            kolvo += 1
            summa.append(sum(chetverka))

print(kolvo, max(summa))