alphabet = '0123456789ABC'
numbers = []

for x in alphabet:
    for y in alphabet:
        num = int(f'4C{x}4', 15) + int(f'{x}62A', 13)
        if num % 121 == 0:
            numbers.append(num)
            
print(min(numbers)//121)