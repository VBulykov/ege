for n in range(1, 10000):
    n_bin = bin(n)[2:]
    
    if n_bin.count('1') % 2 == 0:
        n_bin = '1' + n_bin + '00' 
    else:
        n_bin = '11' + n_bin
    
    r = int(n_bin, 2)
    if r >= 412:
        print(n)
        break