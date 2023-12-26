n = 9
n_troichnoe = n
result = ''
while n_troichnoe > 0:
    n_troichnoe, ostatok = divmod(n_troichnoe, 3) 
    #print(n_troichnoe, ostatok)
    result = str(ostatok) + result
    #print(result)
#result = str(n % 3) + result
print(result)




z = 9
n = z
s = ""
while n > 0: # перевод в троичную систему
    s = s + str(n % 3)
    n //= 3
    #print(s, n)
#s = str(z % 3) + s
print(s)