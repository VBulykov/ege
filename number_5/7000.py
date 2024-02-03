from functools import *

@lru_cache
def func():
    k = 0
    for n in range(100000000, 1000000000):
        summa = 0
        #1
        summa += str(n).count('1')
        summa += str(n).count('2')
        summa += str(n).count('3')
        summa += str(n).count('4')
        summa += str(n).count('5')
        summa += str(n).count('6')
        summa += str(n).count('7')
        summa += str(n).count('8')
        summa += str(n).count('9')
        #2
        n_bin = bin(summa)[2:]
        #3
        if n_bin.count('1') % 2 == 0:
            n_bin = '1' + n_bin + '00'
        else:
            n_bin = '10' + n_bin + '1'
        
        if int(n_bin, 2) == 21:
            k += 1

    return k

print(func())