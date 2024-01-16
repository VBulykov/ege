alphabet_1 = '012345678'
#alphabet_2 ='0123456789A'
minimum = 1000000000000000000
numbers = []

#s = sorted('1234567890qwertyuiopasdfghjklzxcvbnm'.upper())
#print(s)
#s = s[:20]

for x in alphabet_1:
    for y in alphabet_1:
        num = int('88' + x + '4' + y, 9) + int('7' + x + '44' + y, 11)
        #num = int(f'88{x}4{y}', 9) + int(f'7{x}44{y}', 11)
        if num % 61 == 0:
            numbers.append(num)
            #if minimum > num:
            #    minimum = num
        
#print(minimum // 61)
print(min(numbers) // 61)