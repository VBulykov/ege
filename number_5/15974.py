for n in range(1000, 1, -1):
    dva = bin(n)[2:]
    
    if n % 2 == 0:
        dva = dva + '10'
    else:
        dva = dva + '01'
    
    r = int(dva, 2)

    if r <= 102:
        print(r)
        break