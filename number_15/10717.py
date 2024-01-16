def tri(n, m, k):
    flag1 = flag2 = False
    if n > 0 and m > 0 and k > 0:
        flag1 = True
        if n + m > k and n + k > m and k + m > n:
            flag2 = True
    
    return flag1 and flag2


for A in range(20000, 0, -1):
    if all(not((tri(x, 11, 18) == (not(max(x, 5) > 68))) and tri(x, A, 5)) == True for x in range(1, 100000)):
        print(A)
        break