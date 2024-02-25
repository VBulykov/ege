'''
from turtle import *
m = 40
tracer(0)
color('red')
for x in range(3, 4):
    left(90)
    for i in range(2):
        fd(3 * x * m)
        right(90)
    
    fd(x * m)
    right(90)
    
    fd(2 * x * m)
    left(90)
    
    fd(2 * x * m)
    right(90)
    fd(x * m)

    penup()
    setheading(90)
    goto(0, -5 * m)
    for i in range(30):
        for j in range(30):
            fd(1 * m)
            dot(5, 'black')
        goto(i * m, -5 * m)
    break
exitonclick()
'''

for x in range(1, 10000000):
    if (x * 3 - 1) * (x - 1) + (3 * x - x) * (x - 1) > 500000:
        print(x)
        break