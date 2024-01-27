print('X Y Z F')
for x in range(0, 2):
    #цикл - for
    for y in range(0, 2):
        for z in range(0, 2):
            if not((x or y) <= (z == x)):
                #условный оператор - if
                print(x, y, z, (x or y) <= (z == x))
