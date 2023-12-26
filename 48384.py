result_list = []

x_znacheniya = '012345678'
y_znacheniya = '012345678'

result = 0

for x in range(0, 9):
    for y in range(0, 9):
        result = int(('88' + str(x) + '4' + str(y)), 9) + int(('7' + str(x) + '44' + str(y)), 11)
        if result % 61 == 0:
            result_list.append(result / 61)

print(min(result_list))