for n in range(2, 100000):
    n_bin = bin(n)[2:]
    str_bin = str(n_bin)

    str_bin = str_bin[:-1]

    if n % 2 == 0:
        str_bin += '01'
    else:
        str_bin += '10'

    result = int(str_bin, 2)

    if result == 2018:
        print(n)