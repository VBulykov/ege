f = open('17_11236.txt')
numbers = [int(i) for i in f]
kv_min_2 = min(
        [i for i in numbers if len(str(abs(i))) == 2]
)**2
max4 = max(
    [i for i in numbers if (
            (len(str(abs(i))) == 4) and (str(abs(i))[-1] == '1')
        )
    ]
)
f.close()

summa = []

for i in range(len(numbers) - 2):
    k = 0
    troika = [numbers[i], numbers[i+1], numbers[i+2]]
    for el in troika:
        if el > kv_min_2:
            k += 1
    if k == 2:
        if (
            (abs(numbers[i]) * abs(numbers[i+1]) * abs(numbers[i+2])) % max4 == 0
        ):
            summa.append(sum([abs(i) for i in troika]))

print(summa)
print(len(summa), max(summa))