for n in range(6, 5000):
    
    num = 7**500 - int('53', n)

    if num % 6 == 0:
        print(n)
        break