for A in range(10000, 0, -1):
    if all(((x & A == 0) or not(x & 37 == 0) or (not(x & 12 == 0))) == 1 for x in range(1, 100000)):
        print(A)
        break