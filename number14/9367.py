num = 9**8 + 3**5 - 9

s = ''
while num != 0:
    s = str(num % 3) + s
    num //= 3

#while num != 0:
#    s += str(num % 3)
#    num //= 3

print(s.count('2'))