def f(s, m):
    #s - количество камней
    #m - порог ходов
    
    #возвращаем какой игрок победил
    if s >= 84: 
        return m % 2 == 0
    #если победных ходов нет, то возвращаем 0
    if m == 0: 
        return 0

    #просматриваем следующие возможные ходы
    h = [f(s+1, m-1)]
    if s % 2 == 0: 
        h += [f(s*1.5, m-1)]
    else: 
        h+= [f(s*2, m-1)]

    #если это ход целового игрока, то достаточно победы в ОДНОМ из вариантов
    #иначе нужны победы во ВСЕХ вариантах
    if m % 2 != 0:
        return any(h)
    else:
        return all(h)

print(max([s for s in range(1, 84) if f(s, 2)]))
print(sorted([s for s in range(1, 84) if not f(s, 1) and f(s, 3)])[:2])
print(max([s for s in range(1, 84) if not f(s, 2) and f(s, 4)]))