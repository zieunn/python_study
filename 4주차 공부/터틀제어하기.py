import turtle
t = turtle.Turtle()
t.width(10)
t.shape("turtle")
t.color("brown")
move = ""

while move.lower() != "quit" :
    move = input("명령어를 입력하시오: (left, right, forw, back, quit): ")
    if move.lower() == "left" :
        t.left(90)
    elif move.lower() == "right" :
        t.right(90)
    elif move.lower() == "forw" :
        t.forward(100)
    elif move.lower() == "back" :
        t.backward(100) 

turtle.done()