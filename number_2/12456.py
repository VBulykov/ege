print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (not(y <= (x == w)) and (z <= x)):
                    print(w, x,y, z,(not(y <= (x == w)) and (z <= x)))