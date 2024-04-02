import turtle

t = turtle.Turtle() #터틀 불러오기

signal = input("신호를 입력하세요(red, yellow, green): ")

if signal == "red" :
    t.penup()  #커서의 이동경로 표시 안되게
    t.goto(0,100) #해당좌표로 커서 이동
    t.pendown() #커서의 이동경로가 표시 되게
    t.color("red") #색깔 지정
    t.begin_fill()
    t.circle(50) #반지름 50짜리 원 그리기
    t.end_fill()
    t.color("green")
    t.penup() #내가 추가함
    t.goto(100, 100)
    t.pendown() #내가 추가함
    t.circle(50)
    t.color("yellow")
    t.penup() #내가 추가함
    t.goto(200, 100)
    t.pendown() #내가 추가함
    t.circle(50)

elif signal == "yellow" :
    t.penup()
    t.goto(0, 100)
    t.color("red")
    t.pendown()
    t.circle(50)
    t.color("green")
    t.penup()
    t.goto(100, 100)
    t.pendown()
    t.circle(50)
    t.color("yellow")
    t.penup()
    t.goto(200, 100)
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.end_fill()
elif signal == "green" :
    t.penup()
    t.goto(0, 100)
    t.color("red")
    t.pendown()
    t.circle(50)
    t.color("green")
    t.penup()
    t.goto(100, 100)
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.color("yellow")
    t.penup()
    t.goto(200, 100)
    t.pendown()
    t.circle(50)
else :
    print("지원되지 않는 신호입니다.")

turtle.done()