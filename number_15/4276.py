def f(x, y):
    return (x * y > A) or (x > y) or (74 > x)

for A in range(6000, 0, -1):
    if all(f(x,y) == 1 for x in range(1000) for y in range(1000)):
        print(A)
        break