numbers = [int(stroka) for stroka in open('7079.txt', 'r')]

max2 = max([i for i in numbers if 100 > abs(i) > 9])

for i in range(len(numbers) - 1):
    pass