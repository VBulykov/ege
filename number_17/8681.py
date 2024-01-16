numbers = [int(i) for i in open('17_8681.txt')]
min7 = min([
    i for i in numbers if 10000 > i > 999 and i % 10 == 7
])
l = []

for i in range(len(numbers) - 1):
    if (
        (10000 > numbers[i] > 999 or 10000 > numbers[i+1] > 999) 
        and 
        (numbers[i] * numbers[i+1] % min7 == 0)
    ):
        l.append(numbers[i] * numbers[i+1])

print(len(l), max(l))