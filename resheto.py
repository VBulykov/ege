def func(n):
    IsPrime = [True] * (n + 1)
    IsPrime[0] = False
    IsPrime[1] = False
    d = 2
    
    while d * d <= n:
        if IsPrime[d]:
            for i in range(d * d, n + 1, d):
                IsPrime[i] = False
        d += 1
    
    return IsPrime

print(func(200)[7])