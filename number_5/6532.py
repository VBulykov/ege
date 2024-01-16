for n in range(1000000, 0, -1):
    n_bin = bin(n)[2:]

    if n % 3 == 0:
        n_bin = n_bin + bin(3)[2:]
    else:
        n_bin = n_bin + '1'
    
    if int(n_bin, 2) % 5 == 0:
        n_bin = n_bin + bin(5)[2:]
    else:
        n_bin = n_bin + '1'
    
    if int(n_bin, 2) < 10**6:
        print(n)
        break