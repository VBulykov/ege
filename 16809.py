for n in range(256):
    binarnoe = bin(n)[2:].zfill(8)
    
    binarnoe = binarnoe.replace('1', '#')
    binarnoe = binarnoe.replace('0', '1')
    binarnoe = binarnoe.replace('#', '0')

    r = int(binarnoe, 2)
    if r - n == 133:
        print(n)
        break