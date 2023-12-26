print("x y z f")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not(((not(x) or y or z) and (not(x) or not(z)))):
                print(x, y, z, ((not(x) or y or z) and (not(x) or not(z))))