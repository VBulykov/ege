f = open('37336.txt', 'r')
numbers = [int(stroka) for stroka in f]
f.close()
#print(numbers)

#with open('37336.txt') as f2:
#    numbers2 = [int(stroka) for stroka in f2]
#print(numbers2)
#print('abc')

k, maximum = 0, -10001

for i in range(len(numbers) - 1):
    if numbers[i] % 3 == 0 or numbers[i + 1] % 3 == 0:
        k += 1
        if numbers[i] + numbers[i + 1] > maximum:
            maximum = numbers[i] + numbers[i + 1]

print(k, maximum)