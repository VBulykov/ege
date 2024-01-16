res = set()

for x in range(1, 152):
    bin_x = bin(x)[2:]
    
    if x % 3 == 0:
        bin_x += bin_x[-3:]
    else:
        bin_x += bin((x % 3) * 3)[2:]
    
    r = int(bin_x, 2)

    if r > 151:
        res.add(r)

print(res)
print(min(res))