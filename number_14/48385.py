result_list = []

alphabet = '0123456789ABC'


alphabet_exp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
alphabet_exp = alphabet_exp[:10]



result = 0

for x in alphabet:
    for y in alphabet:
        result = int(('8' + x + '78' + y), 13) + int(('79' + x + y + '7'), 18)
        if result % 9 == 0:
            result_list.append(result / 9)

print(min(result_list))