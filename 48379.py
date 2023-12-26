result_list = []

alphabet = '012345678'
alphabet = sorted('012345678QWERTYUIOPASDFGHJKLZXCVBNM')[:27]
print(alphabet)
result = 0
for a in range(1, 10000):
    for x in alphabet:
        m = int(('842'+ x + '5'), 9)
        n = int(("8" + x + "725"), 9)

        if (m + a) % n == 0:
            result_list.append(a)
            break

print(min(result_list))