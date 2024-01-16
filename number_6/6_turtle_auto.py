from turtle import *

tracer(False) #отключаем анимации
m = 20        #масштаб рисунка

#pendown()
left(90)

for i in range(4):
    forward(12 * m)
    right(90)
right(30)


for i in range(3):
    forward(8 * m)
    right(60)
    forward(8 * m)
    right(120)



penup()

for x in range(-30, 20):
    for y in range(-20, 20):
        goto(x * m, y * m) 
        dot('red')


done()