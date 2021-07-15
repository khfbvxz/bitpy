# ch07 추가 연습문제 3번

import turtle,random

t = turtle.Turtle()
t.shape("turtle")
color = ["yellow","red","purple","blue"]
x = 0
y = 0
def draw_square(x,y,c): #함수 선언
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(c)
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.left(90)
    t.end_fill()
for c in color:
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    draw_square(x,y,c)
