for n in range(1, 200):
    result = ''
    n_troichnoe = n
    while n_troichnoe > 0: #алгоритм для перевода в троичную систему счисления
        n_troichnoe, ostatok = divmod(n_troichnoe, 3) #в первую переменную записывается целая часть от деления, во вторую остаток
        result = str(ostatok) + result                #записываем остаток в начало строки
    
    result = result + str(n % 3) #выполняем второй пункт
    
    res = 0                      #переводим в десятичную систему счисления
    for i in range(1, len(result) + 1):
        res += int(result[-i]) * 3 ** (i - 1)

    if res > 99:
        print(len(result))
        print(result)
        print(res)
        break