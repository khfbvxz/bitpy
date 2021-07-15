# ch07 추가 연습문제 3번

import turtle,random
t = turtle.Turtle()
t.shape("turtle")
s = turtle.Screen()
s.bgcolor("black")
color = ["yellow","red","purple","blue","brown","green","white"]
x = 0
y = 0
length = 0
def draw_star(color,length,x,y): #함수 선언
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(c)
    t.begin_fill()
    for i in range(5):
        t.forward(length)
        t.left(144)
    t.end_fill()
for c in color:
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    length = random.randint(20,70)
    draw_star(color,length,x,y)
