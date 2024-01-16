for n in range(100, 1000):
    s = str(n)

    a = int(s[0]) * int(s[1])
    b = int(s[1]) * int(s[2])

    if a > b:
        s_new = str(b) + str(a)
    else:
        s_new = str(a) + str(b)
    
    if int(s_new) == 621:
        print(n)
        break








