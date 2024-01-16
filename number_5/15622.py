for i in range(1, 100):
    binarnoe = bin(i)[2:]

    if binarnoe.count('1') % 2 == 0:
        binarnoe += '00'
    else:
        binarnoe += '11'

    r = int(binarnoe, 2)
    if r > 114:
        print(r)
        break