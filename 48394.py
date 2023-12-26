result_list = []

alphabet = '0123456789'

result = 0

for x in alphabet:
    result = int(('4C' + x + '4'), 15) + int((x + '62A'), 13)
    if result % 121 == 0:
        result_list.append(result / 121)

print(min(result_list))