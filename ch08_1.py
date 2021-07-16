''' 8장 추가 연습문제  1번 기본 grid 어케 하는지'''

import turtle
t = turtle.Turtle()
t.shape("turtle")

def f_x(x):
    result = x**2+1
    return result
t.goto(300,0)
t.goto(0,0)
t.goto(0,300)
t.goto(0,0)
for i in range(0,150):
    t.goto(i , f_x(i)*0.01)
