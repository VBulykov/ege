from turtle import *

tracer(False)
m = 20

left(90)

for i in range(2):
    forward(13*m)
    right(90)
    forward(20*m)
    right(90)
penup()
forward(8*m)
right(90)
backward(3*m)
left(90)
pendown()
for i in range(2):
    forward(16*m)
    right(90)
    forward(8*m)
    right(90)

penup()
for x in range(-10, 40):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot('red')


done()