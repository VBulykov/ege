result_list = []

alphabet = '0123456789ABCDE'

result = 0

for x in alphabet:
    result = int(('123' + x + '5'), 15) + int(('1' + x + '233'), 15)
    if result % 14 == 0:
        result_list.append(result / 14)

print(min(result_list))