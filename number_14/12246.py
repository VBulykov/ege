num = 2 * 729**333 + 2 * 243**334 - 81**335 + 2 * 27**336 - 2 * 9**337 - 338

num_9 = ''

while num != 0:
    num_9 = num_9 + str(num % 9)
    num //= 9

sum = 0
for i in range(1, 9):
    sum += num_9.count(str(i))

print(sum)