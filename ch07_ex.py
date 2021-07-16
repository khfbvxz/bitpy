'''ch07 추가 연습문제1번'''
# import random
# values=[]
# for i in range(10):
#     values.append(random.randint(1,100))
# print(values)

'''#ch07 추가 연습문제 2번'''
# import random
# values=[]
# for i in range(5):
#     values.append(random.randint(1,20))
# # print(values)
#
# for j in range(5):
#     print(str(values[j])+"\t\t"+'*'*int(values[j]))

'''ch07 추가 연습문제 4번'''
#
# import turtle,random
# t = turtle.Turtle()
# t.shape("turtle")
# s = turtle.Screen()
# s.bgcolor("black")
# color = ["yellow","red","purple","blue","brown","green","white"]
# x = 0
# y = 0
# length = 0
# def draw_star(color,length,x,y): #함수 선언
#     t.penup()
#     t.goto(x,y)
#     t.pendown()
#     t.color(color)
#     t.begin_fill()
#     for i in range(5):
#         t.forward(length)
#         t.left(144)
#     t.end_fill()
# for c in range(30):
#     x = random.randint(-200,200)
#     y = random.randint(-200,200)
#     length = random.randint(20,70)
#     draw_star(color[c%7],length,x,y) # c%7

''' ch07 추가 연습문제 3번'''

# import turtle,random
#
# t = turtle.Turtle()
# t.shape("turtle")
# color = ["yellow","red","purple","blue"]
# x = 0
# y = 0
# def draw_square(x,y,c): #함수 선언
#     t.penup()
#     t.goto(x,y)
#     t.pendown()
#     t.color(c)
#     t.begin_fill()
#     for i in range(4):
#         t.forward(50)
#         t.left(90)
#     t.end_fill()
# for c in color:
#     x=random.randint(-200,200)
#     y=random.randint(-200,200)
#     draw_square(x,y,c)

''' 오늘의 명언 '''

# import random
# r = random.randint(0,2)
# print("#"*30)
# print("#     오늘의 명언")
# print("#"*30)
# my = ["고생 없이 얻을 수 있는 진실", "사람은 사랑 할 때 누구나", "꿈을 지녀라. 그러면 어려운"]
# print(my[r])

''' 스파이럴 그리기 '''
# import turtle
# t = turtle.Turtle()
# color = ["yellow","green","blue","purple","red","brown"]
#
# for i in range(1,200,2):
#     count=+1
#     t.color(color[i % 5])
#     t.forward(10+i)
#     t.left(89)

''' 오륜기 그리기 '''
# import turtle
# t = turtle.Turtle()
# position = [[0, 0, "green"], [-120, 0, "yellow"],
#             [60, 60, "red"], [-60, 60, "black"], [-180, 60, "blue"]]
# # color = ["blue", "yellow","black","green","red"]
# t.width(10)
# for x,y,c in position:
#     t.penup()
#     t.goto(x,y)
#     t.pendown()
#     t.color(c,c)
#     t.circle(60)

'''습도 구하기'''
# sd =  [4.8, 9.4, 17.3, 30.4]
# on =  [9.4, 9.4,  17.3, 17.3]
# # .append()
# sbdo = []
#
# sbdo.append((sd[0]/on[3])*100)
# sbdo.append((sd[1]/on[2])*100)
# sbdo.append((sd[2]/on[3])*100)
# sbdo.append((sd[3]/on[2])*100)
# print(sbdo)

''' '''
