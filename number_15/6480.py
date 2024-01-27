P = [i for i in range(10, 22)]
Q = [i for i in range(13, 39)]
R = [i for i in range(18, 26)]

def f(x, A):
    return (
        (not((x in Q) <= ((x in P) or (x in R)))) 
        <= 
        ((not(x in A)) <= (not(x in Q)))
    ) 

A = 10 39

for i in range(1, 200):
    
    if all(
        f(x, otrezok) 
        for x in range(1000)
        for otrezok in A
    ):
        print(0, A)
        print(len(A))
        break