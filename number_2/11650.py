print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not( ((y and (x == (not(z)))) <= w) and (z <= y) ):
                    print(x, y, z, w, ((y and (x == (not(z)))) <= w) and (z <= y))