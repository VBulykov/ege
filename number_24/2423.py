s = open('24_2423.txt').readline()

for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
        if s[i:j] == sorted(s[i:j]):
            