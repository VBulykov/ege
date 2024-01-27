from turtle import *

tracer(False) #отключаем анимации
m = 20        #масштаб рисунка

#pendown()
left(90)

left(40)
for i in range(5):
    right(-95)
    forward(12 * m)
    left(45)
    forward(8 * m)
    left(40)

penup()

for x in range(-30, 20):
    for y in range(-20, 20):
        goto(x * m, y * m) 
        dot('red')


done()