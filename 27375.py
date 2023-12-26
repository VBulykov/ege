for n in range(1, 1000):
    result = ''
    n_vre = n
    while n_vre > 0:
        result = str(n_vre % 3) + result
        n_vre //= 3
    
    result += str(n % 3)
    res = int(result, 3)

    res_2 = 0
    for i in range(1, len(result) + 1):
        res_2 += int(result[-i]) * 3 ** (i - 1)


    if res > 99:
        print(res)
        print(res_2)
        break
