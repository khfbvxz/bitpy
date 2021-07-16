'''lab 1 BMI 계산기'''
# h = float(input("키를 m단위로 입력하세요:"))
# g = float(input("몸무게를 kg단위로 입력하세요:"))
# bmii = 0
#
# def bmi(h, g):
#     bmii = g / (h ** 2)
#     return bmii
# bmi(h, g)
# if bmi(h, g) < 18.5:
#     print("당신은 저체중입니다.")
# elif bmi(h, g) >= 18.5 and bmi(h, g) <= 22.9:
#     print("당신은 정상체중입니다.")
# elif bmi(h, g) >= 23 and bmi(h, g) <= 24.9:
#     print("당신은 정상체중입니다.")
# elif bmi(h, g) >= 25 and bmi(h, g) <= 29.9:
#     print("당신은 정상체중입니다.")
# else:
#     print("당신은 고도비만입니다.")

'''환전 계산기'''
# money = float(input("환전 금액(원)을 입력하세요: "))
# na = input("국가를 입력하세요: ")
#
# h = [["미국", "일본", "유럽연합", "중국"], [1182.5, 1078.14, 1286.74, 169.22]]
# def aa(money,na):
#     if na == "미국":
#         coin = money / 1182.5
#         print(money, " 원은 ", coin, "달러입니다.")
#     elif na == "일본":
#         coin = money / 1078.14
#         print(money, " 원은 ", coin, "엔입니다.")
#     elif na == "유럽연합":
#         coin = money / 1286.74
#         print(money, " 원은 ", coin, "유로입니다.")
#     elif na == "중국":
#         coin = money / 169.22
#         print(money, " 원은 ", coin, "위안입니다.")
#     else:
#         print("해당 국가 정보가 없습니다.")
# aa(money,na)
'''n각형 그리는 함수'''

# import turtle
# t=turtle.Turtle()
# num=turtle.textinput("","몇 각형을 원하시나요: ")
# t.shape("turtle")
#
# num2=int(num)
# ang=180*(num2-2)
# def n_polygon():
#     for i in range(10):
#         t.left(10)
#         for num in range(num2):
#             t.forward(100)
#             t.left(180-(ang/num2))
# n_polygon()

''' 클릭하는 곳에 사각형 그리기'''
# import turtle
# t = turtle.Turtle()
# def square(length):
#     for i in range(4):
#         t.forward(length)
#         t.left(90)
# def drawit(x, y):
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.begin_fill()
#     t.color("green")
#     square(100)
#     t.end_fill()
#
# s = turtle.Screen()
# s.onscreenclick(drawit)
# s.mainloop()  # 창 꺼지지 않게 하는 함수

'''한 붓 그리기'''
