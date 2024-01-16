for n in range(1, 1000):
    n_bin = bin(n)[2:] #двоичная запись числа
    
    #n_bin.count('1') - считает количество единиц в двоичной записи
    #n_bin.count('1') % 2    - нашли остаток от деления числа на два

    n_bin = n_bin + str(int(n_bin.count('1')) % 2)  #приписали число в конец строки
    n_bin += str(int(n_bin.count('1')) % 2)

    res = int(n_bin, 2) #перевод в десятичный вид
    if res > 97:
        print(res)
        break

