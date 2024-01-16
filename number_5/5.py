for n in range(1,200):
    b = ''
    z = n
    while n > 0:
        b = str(n%3) + b
        n //= 3
        #print(b, n)

    b += str(z%3)

    if len(str(int(b,3))) == 3:
        print(len(b))
        print(b)
        
        print(str(int(b,3)))
        break