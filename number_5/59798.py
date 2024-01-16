for n in range(1, 1000):
    x = y = n
    

    s = ''
    while x > 0:
        s = str(x % 3) + s
        x //= 3

    end = ''
    if y % 3 != 0:
        y = y % 3 * 5
        while y > 0:
            end = str(y % 3) + end
            y //= 3

        s += end
    
    r = int(s, 3)
    if r > 146:
        print(n)
        break

