spisok_chisel = []
for n in range(100, 1000):
    #n = 518
    #    012
    #n // 100 = 5
    #n //  10 = 51 % 10  = 1
    #n % 10 = 8
    per_vt = int(str(n)[0]) * int(str(n)[1])
    vt_tr  = int(str(n)[1]) * int(str(n)[2])

    if per_vt > vt_tr:
        result = str(per_vt) + str(vt_tr)
    else:
        result = str(vt_tr) + str(per_vt)

    if result == '240':
        spisok_chisel.append(n)

print(max(spisok_chisel))