numbers = [
    int(stroka) for stroka in open('17-383.txt', 'r')
]

max2 = max(
    [i for i in numbers if 100 > abs(i) > 9]
)
k = 0
max_el = -10000000000000

for i in range(len(numbers) - 1):
    if (
        ((9 < abs(numbers[i]) < 100) or (9 < abs(numbers[i+1]) < 100))
        and
        ((numbers[i] + numbers[i+1]) <= max2)
    ):
        k += 1
        max_el = max(max_el, numbers[i] + numbers[i+1])

print(k, max_el)