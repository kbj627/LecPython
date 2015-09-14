import turtle
import math
import random
import time

radius = 200

turtle.title('[Report 1-1] 201111256 강태욱')
turtle.shape('turtle')

turtle.penup()
turtle.goto(0, -200)
turtle.pendown()

turtle.color('red')
turtle.begin_fill()
turtle.circle(radius)
turtle.end_fill()

turtle.color((1.0, 1.0, 0.0))
turtle.penup()
turtle.circle(radius)

flag = True
x = 0
y = 0
rand_Val = (-7, -6, -5, -4, -3, 0, 3, 4, 5, 6, 7)
increase_X = random.choice(rand_Val)
increase_Y = random.choice(rand_Val)

turtle.goto(x, y)
time.sleep(1)

while flag :
    turtle.goto(x, y)
    if math.sqrt(math.pow(x + increase_X, 2) + math.pow(y + increase_Y, 2)) > radius:
        increase_X = random.choice(rand_Val)
        increase_Y = random.choice(rand_Val)
        while abs(increase_X) + abs(increase_Y) < 5 :
            increase_X = random.choice(rand_Val)
            increase_Y = random.choice(rand_Val)
    else :
        x += increase_X
        y += increase_Y
    time.sleep(0.02)