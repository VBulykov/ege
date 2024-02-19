print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(((x and not(y)) <= (z and w)) and ((y <= z) or (w <= x))):
                    print(x, y, z, w, 
                        ((x and not(y)) <= (z and w)) and ((y <= z) or (w <= x))      
                    )