print('A B C F')
for A in range(0, 2):
    for B in range(0, 2):
        for C in range(0, 2):
            if (A or C) and (B or C):
                print(A, B, C, (A or C) and (B or C))



'''print('x y')
for x in range(0, 2):
    for y in range(0, 2):
        print(x, y, not(x > y))'''