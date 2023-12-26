alphabet = '0123456789ABCDE'
numbers = []

for x in alphabet:
    for y in alphabet:
        num = int(f'123{x}5', 15) + int(f'1{x}233', 15)
        if num % 14 == 0:
            numbers.append(num)
            
print(min(numbers)//14)