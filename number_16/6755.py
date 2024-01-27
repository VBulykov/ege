A = [7, 7, 7, 7, 7, 7, 7]

for n in range(7, 2025):
    A.append(n + 1 + A[n-2])


print(A[2024] - A[2020])