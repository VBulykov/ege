f = open('7079.txt', 'r')
numbers = [int(stroka) for stroka in f]
f.close()

kolvo = 0
maximum = max([i for i in numbers if str(abs(i))[0] == '8'])
minimum = []

for i in range(len(numbers) - 2):
    troika = [numbers[i], numbers[i+1], numbers[i+2]]
    k = 0
    for el in troika:
        if str(abs(el))[0] == '6':
            k += 1
    
    if k <= 1:
        if sum(troika) >= maximum:
            kolvo += 1 
            minimum.append(sum(troika))

print(kolvo, min(minimum))