'''신비로운 수 소수를 판별하라'#1'''
# import time
# start = time.time()
#
# n = int(input("n 값을 입력하세요:"))
# count = 1
# for a in range(2,n+1):
#     if n % a == 0:
#         count+=1
'''위랑 출력비교 속도 비교'''
# for a in range(2,n+1):
#     if n % a == 0:
#         count+=3
#         break
#     elif n % a == 0:
#         count+=1
# b = (n+1)//2
# for a in range(2, b):
#     if n % 2== 0:
#         count+=3
#         break
#     elif n % a == 0:
#         count+=1
#
#
# if(count == 2):
#     print("소수입니다.")
# else:
#     print("소수가 아닙니다.")
# print("time",time.time()-start)

'''에라토스테네스의 체
1은 소수가 아니므로 지운다
남은 수 중 가장 작은 2는 남기고, 2의 배수를 모두 지운다
남은 수 중 가장 작은 3은 남기고, 3의 배수를 모두 지운다
남은 수 중 가장 작은 5는 남기고, 5의 배수를 모두 지운다
남은 수 중 가장 작은 7는 남기고, 7의 배수를 모두 지운다
이처럼 남은 수 중 가장 작은수를 고른 후, 그 수보다 큰 그 수의 배수를 모두 지우는 방법을 반복한다
'''
# n=1000
# number = [False,False]+[True]*(n-1)
#
# primes = []
#
# for i in range(2, n+1):
#     if number[i]:
#         primes.append(i)
#         for j in range(2*i, n+1, i):
#             number[j]=False
# print(primes)

'''이차방정식ㄷ의 해'''
# import math
# import sys
# print("ax^2 + bx + c = 에서")
# a = float(input("a값 : "))
# b = float(input("b값 : "))
# c = float(input("c값 : "))
# if a==0:
#     print("a=0이므로 이차방정식이 아님")
#     sys.exit()
# D = b*b-4*a*c
# if D < 0:
#     print("해가 없습니다.")
# else:
#     x1 = (-b + math.sqrt(D)) / (2*a)
#     x2 = (-b - math.sqrt(D)) / (2 * a)
#     print("해.", x1, ",", x2)

# from matplotlib import pyplot as plt
# import numpy as np
# x = np.arange(-2,8)
# y = -x**2 + 5*x +1
# plt.plot(x, y, marker='o', linestyle='--', color='r')
# plt.grid()
# plt.show()

'''대푯값을 구하기'''
# data = [6, 7, 7, 8, 8, 10, 9, 3, 5, 2, 7, 2, 6]
# length = len(data)  # len()은 리스트에 들어있는 원소 개수, 그러니까 리스트의 크기를 알려줌
# average = sum(data)/length
# print(average)
# data.sort()
# print(data)
# n=len(data)
# print("원소 개수 : ", n)
# middle = n//2
# if n % 2 ==1:
#     print("중앙값은:", data[middle])
# else:
#     print("중앙값은", (data[middle-1]+data[middle+1])/2)
'''최빈수'''
# freq = {}
# for i in data:
#     freq[i] = data.count(i)
# max_freq = 0
# for i in freq:
#     print(i, "의 횟수",freq[i])
#     if(freq[i]>max_freq):
#         max_freq = freq[i]
#         max_freq_num = i
# print("최빈수=", max_freq_num)
# print(data.count(7))

'''히스토그램 '''
''' 높은 3 보통 2 적음1 없음 0'''
# #파일을 읽어 데이터를 처리하는 부분
# a = [ ]                      #파일 전체 내용 임시저장 리스트
# data = ['', '', '', '', '']  #공백으로 구분된 자료를 항목별로 분리하여 저장하는 리스트
# score = [0, 0, 0, 0, 0]      #항목 별 설문
# total = 0
# inflie = open("e:\\interest.txt", "r", encoding="UTF-8")
# lines = inflie.readlines()  # 한줄씩 읽어 a 리스트에 저장
# for i in lines:
#     a.append(i)
#
# for i in range(0,5):
#     data[i] = a[i].split()    #data [항목] [점수] 구조로 저장
# for i in range(0,5):          #항목 5개
#     for j in range(1,26):     #25명 자료 조사
#         score[i]+=int(data[i][j])
#     total += score[i]
#     print(data[i][0] + str(score[i])+"점")
# print("합계="+str(total))
# inflie.close()
#
# #터틀
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# pen = ["red","blue","orange","green","purple"]
# t.pensize(2)
# def bar(category,s):
#     t.begin_fill()
#     t.left(90)
#     t.forward(s)
#     t.write(category+""+str(s)+"점")
#     t.right(90)
#     t.forward(50)
#     t.right(90)
#     t.forward(s)
#     t.left(90)
#     t.end_fill()
#     t.forward(10)
#
# for i in range(0,5):
#     t.color(pen[i])
#     category = data[i][0]
#     s = int(score[i])
#     bar(category,s)
#
# s = turtle.Screen()
# s.mainloop()     #터틀 그래픽 창 안꺼지게

'''토끼와 거북이경주'''
# import turtle
# screen = turtle.Screen()
# image1 = "e:\\rab.gif"
# image2 = "e:\\tur.gif"
# screen.addshape(image1)
# screen.addshape(image2)
# t1 = turtle.Turtle() # 토끼
# t2 = turtle.Turtle() # 거북2
#
# t1.shape(image1)
# t1.penup()
# t1.goto(-300,0)
#
# t2.shape(image2)
# t2.penup()
# t2.goto(-300,-200)
# t1.pendown()
# t2.pendown()
#
# import random
# for i in range(10):
#     d1 = random.randint(1,60)
#     t1.forward(d1)
#     d2 = random.randint(1,60)
#     t2.forward(d2)
# screen.mainloop()

'''앵그리 터틀 게임'''
# import math,turtle,random
# player = turtle.Turtle()    # 객체 생성()
# player.shape("turtle")
# screen = player.getscreen()
# def turn_left():
#     player.left(5)
# def turn_right():
#     player.right(5)
# def start_p():
#     x = 0  # 초기값
#     y = 0
#     velocity = 50               #초기속도 50 픽셀/sec
#     angle = player.heading()    #초기각도
#     vx = velocity*math.cos(angle*3.14/180)  # 도-> 라디안  거북이의 x방향 속도
#     vy = velocity*math.sin(angle*3.14/180)
#     while player.ycor() >= 0:  # . ycor() y 좌표를 구하기 위해
#         vx = vx                   # 초기속도에서 변하지 않음
#         vy = vy - 10                # 초기속도에서 중력가속도 만큼 점멎 느려짐
#         x = x + vx                 # 터틀 현재 위치 계산
#         y = y + vy
#         player.goto(x, y)
# screen.onkeypress(turn_left,"Left")   #각도 왼쪽
# screen.onkeypress(turn_right,"Right") #각도 오른쪽
# screen.onkeypress(start_p,"space")   #출발 space키
# screen.listen()
# screen.mainloop()

''' 터틀 아스테로이드 게임 '''
'''
소행성 배치 및 소행성 움직이기
터틀 우주선 생성 후 사용자가 터틀을 조정할 수 있게
터틀이 소행성 만나면 클리어 나도록

'''
#
# import turtle,random
# astero = [] # astero 리스트 생성
# for i in range(10):
#     smallp = turtle.Turtle()
#     smallp.color("red")
#     smallp.shape("circle")
#     smallp.penup()
#     smallp.speed(0)
#     smallp.goto(random.randint(-300,300),random.randint(-300,300))
#     astero.append(smallp)     # 소행성 리스트에 추가
# player = turtle.Turtle()
# player.color("blue")
# player.shape("turtle")
# player.penup()
# player.speed(0)
#
# screen = player.getscreen()
# def turn_left():
#     player.left(30)
# def turn_right():
#     player.right(30)
# def gogo():
#     player.forward(20)
# def play():
#     player.forward(2)
#     for a in astero:
#         a.right(random.randint(-180,180))
#         a.forward(2)
#         if player.distance(a)<20:
#             player.write("clear")
#             a.ht()
#     screen.ontimer(play,10)
# screen.ontimer(play,10)
# screen.onkeypress(turn_left,"Left")
# screen.onkeypress(turn_right,"Right")
# screen.onkeypress(gogo)
# screen.listen()
# screen.mainloop()

'''틱택토 게임'''
# import turtle
# t = turtle.Turtle()
# window = turtle.Screen()
#
# window.setup(600, 600)
# window.bgcolor("black")
#
# t.hideturtle()
# t.speed(10)
# t.pensize(10)
# t.pencolor("white")
# t.down()
#
#
# # 가로선 그리기
# for i in range(3):
#     t.up()
#     t.goto(-300, i*200-300)
#     t.down()
#     t.forward(600)
# t.left(90)
#
# # 세로선 그리기
# for i in range(1, 3):
#     t.up()
#     t.goto(i * 200 - 300, -300)
#     t.down()
#     t.forward(600)
# t.pencolor("green")
# t.up()
#
# #x표시 그리기
# def draw_x(x, y):
#     t.up()
#     t.goto(x+50, y-200)
#     t.down()
#     t.write("X", font=('Arial', 100, 'normal'))
# # o 표시 그리기
# def draw_o(x,y):
#     t.up()
#     t.up()
#     t.goto(x + 50, y - 200)
#     t.down()
#     t.write("O", font=('Arial', 100, 'normal'))
# #전체보드 그린기
# def draw(borad):
#     x = -300
#     y = 300
#     for piece in borad:
#         if piece == "X":
#             draw_x(x,y)
#         elif piece == "O":
#             draw_o(x,y)
#         x = x +200
#         if x>=300:
#             x = -300
#             y = y - 200
# board = ["","","","","","","",""] # 공백 리스트 생성
# nextTurn="X"
# # 사용자가 보드를 클릭하면 해당되는 칸을 찾는다.
# def clicked(x,y):
#     global nextTurn, board
#     print(x,"",y)
#     column = (x+300)//200
#     row = -(y - 300)//200
#     cell = column + row * 3
#     cell = int(cell)
#     print(row,"",column)
#     board[cell]=nextTurn
#     if nextTurn == "X":nextTurn="O"
#     else:nextTurn="X"
#     draw(board)
# draw(board)
# window.onscreenclick(clicked)
# turtle.mainloop()

'''우리나라 인구분석'''
'''
반복 가능한 데이터: iter() 함수로 반복자를 구할 수 있는 데이터
반복자: next() 함수로 값을 하나씩 꺼낼 수 있는 데이터
iter() 함수: 반복 가능한 데이터를 입력받아 반복자를 반환하는 함수
next() 함수: 반복자를 입력받아 다음 출력값을 반환하는 함수
'''
# import csv
# data = csv.reader(open("e:\\201801_201801_주민등록인구기타현황(평균연령)_avgAge.csv"), delimiter=",")
# # delimiter=","  CSV 파일이 뭘로 나누어져 있는지(\t, ' ', '+' 등)를 나타낸다.
# next(data)
# next(data)
# woman = {'age': 0,'loc':''}
# for row in data:
#     # print(row)
#     # print(row[0], row[2])
#     row[2] = float(row[2])
#     if woman['age']<row[2]:
#         woman['age']=row[2]
#         woman['loc']=row[0]
# print('여성 평균 연령이 가장 높은 지역은',woman['loc'],'이고 평균 연령은',woman['age'],'입니다')