import sys
num = 343**1515 - 6 * 49**1520 + 5 * 49**1510 - 3 * 7*1530 - 1550
s = ''

sys.set_int_max_str_digits(4600)

while num > 0:
    s = str(num % 7) + s
    num //= 7

s1 = ''
for i in range(len(s)):
    if s[i] != 0:
        s1 = s
        break
    else:
        s1 = s[i:]


print(s1.count('0'))