from turtle import *

tracer(False) #отключаем анимации
m = 20        #масштаб рисунка
#pendown()
left(90)

for i in range(2):
    forward(13 * m)
    right(90)
    forward(20 * m)
    right(90)    

penup()
forward(8 * m)
right(90)
backward(3 * m)
left(90)
pendown()

for i in range(2):
    forward(16 * m)
    right(90)
    forward(8 * m)
    right(90)    

penup()

for x in range(-10, 20):
    for y in range(0, 40):
        goto(x * m, y * m) 
        dot('red')


done()