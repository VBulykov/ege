for i in range(1, 100):
    binarnoe = bin(i)[2:]
     
    binarnoe += str(binarnoe.count('1') % 2)
    binarnoe += str(binarnoe.count('1') % 2)

    r = int(binarnoe, 2)
    if r > 43:
        print(r)
        break