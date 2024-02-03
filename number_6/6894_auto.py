from turtle import *
m = 15
tracer(0)
left(90)

color('red')

for x in range(2, 1000):
    #рисуем точки
    color('black')
    penup()
    for x_dot in range(0, 3 * (x) + 1):
        for y_dot in range(0, 4 * (x) + 1):
            goto(x_dot*m, y_dot*m) 
            dot('black')
    goto(0, 0)
    pendown()
    #рисуем большую фигуру
    color('red')
    forward(x * m)
    for i in range(3):
        forward(3*x * m)
        right(90)
    left(90)
    for i in range(3):
        forward(x * m)
        right(90)
    left(180)
    forward(x * m)
    left(90)
    for i in range(2):
        forward(x * m)
        right(90)  
    #рисуем внутренний квадрат      
    color('blue')
    penup()
    forward(2*x * m)
    right(90)
    forward(x * m)
    left(90)
    pendown()
    for i in range(4):
        forward(x * m)
        right(90)
    penup()
    goto(0, 0)
    pendown()

    break
    clear()

done()

for n in range(1, 1000):
    #вывели количество точек для фигуры
    if (4*n -1) * (3*n - 1) - (n+1)**2 - (n+1) * n > 440000:
        print(n)
        break