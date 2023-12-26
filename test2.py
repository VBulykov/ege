for i in range(1, 100):
    n = i
    s = ""
    while n > 0: # перевод в троичную систему
        s += str(n % 3)
        n //= 3
    s = str(i % 3) + s
    r = 0
    for j in range(len(s)): # перевод в десятичную систему
        r += int(s[j]) * 3 ** j
    if r > 99:
        print(s)
        print(r)
        break