import turtle
t = turtle.Turtle()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for color in colors :
    t.color(color)
    t.begin_fill()
    for x in range(4) :
        t.forward(100)
        t.right(90)
    t.end_fill()

    t.right(60)

t.done()

