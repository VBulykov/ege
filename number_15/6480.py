P = [i for i in range(10, 22)]
Q = [i for i in range(13, 39)]
R = [i for i in range(18, 26)]
A = []

def f(x, A):
    return (
        (not((x in Q) <= ((x in P) or (x in R)))) 
        <= 
        ((not(x in A)) <= (not(x in Q)))
    )

for x in range(1, 200):
    if not((f(x, A))):
        A.append(x)

print(A)
print(len(A))