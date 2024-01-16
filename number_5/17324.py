d = set() #множество

for n in range(10, 1001):
    binarnoe = bin(n)[3:] #срез начался не с привычной 2 а с 3
    if '1' in binarnoe:
        one_i = binarnoe.index('1') #индекс первой единицы слева 
        binarnoe = binarnoe[one_i:]
    else:
        binarnoe = "0"
    
    r = int(binarnoe, 2)
    r = n - r
    print(r)
    d.add(r)

print(d)
print(len(d))