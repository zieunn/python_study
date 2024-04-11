import turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
t = turtle.Turtle()

for i in range(30) :
    x = random.randint(-500, 500)
    y = random.randint(-500, 500)
    r = random.randint(50, 100)
    color = random.choice(colors)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

    

