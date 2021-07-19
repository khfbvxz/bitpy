'''한 붓 그리기'''
'''
우점 : 한점에서 선이나가는 갯수가 짝수인것
기점 :   ''                  홀수인것

'''
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
#
# t.pensize(10)
#
# def draw(x , y):
#     t.goto(x, y)
#
# s = turtle.Screen()
# s.onscreenclick(draw)
# s.mainloop()

'''테세우스 터틀 미로 탈출 게임'''
'''
방향키 움직이는 게임
1. 터틀 준비
2. 미로그리기
draw_maze()
3. 키보드 이벤트

'''
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(0)
# def draw_mab(x, y): #맵 형성 함수
#     for i in range(2):
#         t.penup()
#         if i == 1:
#             t.goto(x+100, y+100)
#         else:
#             t.goto(x, y)
#         t.pendown()
#         t.forward(300)
#         t.right(90)
#         t.forward(300)
#         t.left(90)
#         t.forward(300)
#
# def turn_left():
#     t.left(10)
#     t.forward(10)
#
# def turn_right():
#     t.right(10)
#     t.forward(10)
# draw_mab(-300,200)
#
# s = turtle.Screen()
# s.onkey(turn_left, "Left")
# s.onkey(turn_right, "Right")
# t.penup()
# t.goto(-300,250)
# t.pendown()
#
# s.listen() # 사용자 입력이 잘 처리되도록 포커스 주는 함수
# s.mainloop() # 계속 터틀 그래픽 사용 가능하게 x버튼 누르기 전까지 사용

'''재귀호출'''
''' 수열
함수는 내부에서 다시 자기 자신을 호출할 수 있습니다.
재귀 어떤 문제를 해걀하기 위해 동일한 문제를 더 작은 경우로 쪼개고 쪼개서 문제를 바로 풀 수 있도록
    간단해질 때까지 나누어 해결하는 방법
종료조건!
'''
# def fact(n):
#     if n == 1:       # 종료조건
#         return 1
#     else:
#         return n * fact(n-1)  #리턴값이 다시 fact(n)함수 호출출
# n = int(input("정를 입력하세요: "))
# f = fact(n)
# print(n, "!은", f , "이다.")

'''프랙털 나무 그리기'''
'''
프랙털 자신의 작은 부분에 자신과 닮은 모습이 나타나고 그안의 작은 부분에도 자신과 닮은 모습니 무한히 반복되어 
      무한히 반복되어 나타나는 현상
직선을 그린다.
직선의 끝에서 가지 나누어지는 
위 반복
'''
import turtle
def tree(length):
    if length > 5:         # 종료조건 길이가 보다크면 순환 작으면 종료
        t.forward(length)  # 직진
        t.right(20)        # R 회전
        tree(length-15)    # 길이가 짧은 상태로 재귀호출
        t.left(40)         # L 회전
        tree(length-15)    # 다시 재귀
        t.right(20)        # R회전 원래 각도로
        t.backward(length) # 후진
t = turtle.Turtle()
t.color("green")
t.speed(0)
t.penup()
t.goto(0,-200)
t.pendown()
t.left(90)   # 시작방향
tree(100)
s = turtle.Screen()
s.listen() # 사용자 입력이 잘 처리되도록 포커스 주는 함수
s.mainloop() # 계속 터틀 그래픽 사용 가능하게 x버튼 누르기 전까지 사용