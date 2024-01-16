numbers = [int(i) for i in open('17_9840.txt')]

max4 = max([
    i for i in numbers if (
       999 < abs(i) < 10000 and abs(i) % 100 == 39
    )
])**2

summa = []

for i in range(len(numbers) - 1):
    if (
        (999 < abs(numbers[i]) < 10000) !=
        (999 < abs(numbers[i+1]) < 10000)
    ):
        if (numbers[i] + numbers[i+1])**2 <= max4:
            summa.append(numbers[i] + numbers[i+1])

print(len(summa), max(summa))