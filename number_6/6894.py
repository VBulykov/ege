from turtle import *

tracer(False) #отключаем анимации
m = 20        #масштаб рисунка

#pendown()
left(90)

x = 1

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

penup()
forward(2 * x)
right(90)
forward(x * m)
left(90)
pendown()

for i in range(4):
    forward(x * m)
    right(90)



penup()

for x in range(-30, 20):
    for y in range(-20, 20):
        goto(x * m, y * m) 
        dot('red')


done()