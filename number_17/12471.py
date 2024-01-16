f = open('17_12471.txt')
numbers = [int(i) for i in f]
max13 = max(
    [el for el in numbers if el % 100 == 13]
)
#num = []
#for i in f:
#    print(i)
#    num.append(int(i))
f.close()
#print(len(num))
#print(numbers)
#print(max13)
k = 0
srar = []
for i in range(len(numbers) - 2):
    if ((
        numbers[i] % 2 == 0 and
        numbers[i+1] % 2 == 0 and
        numbers[i+2] % 2 == 0
    ) or (
        (numbers[i] // 100 == 0 and numbers[i] % 100 >= 10) or 
        (numbers[i+1] // 100 == 0 and numbers[i+1] % 100 >= 10) or 
        (numbers[i+2] // 100 == 0 and numbers[i+2] % 100 >= 10)
    )) and (
        (numbers[i] + numbers[i+1] + numbers[i+2]) <= max13
    ):
        k += 1
        srar.append(numbers[i] + numbers[i+1] + numbers[i+2])

print(k, int(sum(srar)/len(srar)))














'''print(100 % 1000)
print(-100 % 1000)
print(100 % 100)
print(-100 % 100)
print('-------')
print(100 // 100)
print(-100 // 100)
print(100 // 1000)
print(-100 // 1000)
print(100 // 10)
print(-100 // 10)

print(213 % 100)
print(-213 % 100)
print(abs(213) % 100)
print(abs(-213) % 100)'''