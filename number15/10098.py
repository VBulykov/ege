def f(x, y):
    return (x + 2 * y < a) or (y > x) or (x > 60)

for a in range(1000):
    if all(f(x, y) for x in range(1000) for y in range(1000)):
        print(a)
        break