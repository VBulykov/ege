x = 4 * 625**9 - 25**15 + 2 * 5**11 - 7

k = 0

while x > 0:
    ostatok = x % 5
    if ostatok == 4:
        k += 1
    
    x //= 5

print(k)