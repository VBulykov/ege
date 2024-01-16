for A in range(1, 10000):
    if all(((A + x > 700 - A) and (A % 100 + 100 % x > 50)) == True for x in range(1, 100000)):
        print(A)
        break