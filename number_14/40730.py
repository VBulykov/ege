num = 3 * 125**6 + 2 * 25**9 + 5**12 - 625
s = ''

while num != 0:
    s = str(num % 5) + s
    num //= 5

print(s.count('0'))