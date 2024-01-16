numbers = [int(i) for i in open('17_9786.txt')]
max25 = max([i for i in numbers if abs(i) % 100 == 25])
summa = []

for i in range(len(numbers) - 2):
    if (
        (10000 > abs(numbers[i]) > 999) +
        (10000 > abs(numbers[i+1]) > 999) +
        (10000 > abs(numbers[i+2]) > 999)
    ) <= 2 and (
        numbers[i] + numbers[i+1] + numbers[i+2] <= max25
    ):
        summa.append(numbers[i] + numbers[i+1] + numbers[i+2])

print(len(summa), max(summa))


#Истина == True == 1