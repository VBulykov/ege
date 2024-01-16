f = open('37337.txt', 'r')
numbers = [int(stroka) for stroka in f]
f.close()

k = 0; maximum = 0

for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if (
            (numbers[i] % 160 != numbers[j] % 160) and 
            (numbers[i] % 7 == 0 or numbers[j] % 7 == 0)
        ):
            k += 1
            if maximum < numbers[i] + numbers[j]:
                maximum = numbers[i] + numbers[j]

print(k, maximum)