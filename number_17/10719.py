f = open('17_10719.txt', 'r')
numbers = [int(stroka) for stroka in f]
f.close()

k = 0
maximum = -20001

for i in range(len(numbers) - 3):
    if (
        (abs(numbers[i]) % 100 == 13) != 
        (abs(numbers[i+3]) % 100 == 13)):
        k += 1
        maximum = max(maximum, (numbers[i] + numbers[i+3]))

print(k, maximum)
