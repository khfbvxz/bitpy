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

# from tkinter import *
# from tkinter import ttk
# def button_pressed(value):
#     number_entry.insert("end", value)  # 텍스트 창으로 숫자 전송.'end'는 오른쪽끝에 추가하라는 의미.
#     print(value, "pressed")
#
# root = Tk()
# root.title("Calculator")
# root.geometry("100x100")
#
# # 텍스트창의 값 저장할 변수.
# entry_value = StringVar(root, value='')
#
# # textvariable 속성으로 변수 설정.
# number_entry = ttk.Entry(root, textvariable=entry_value, width=10)
# number_entry.grid(row=0, columnspan=1)
#
# button1 = ttk.Button(root, text="1", command=lambda: button_pressed('1'))
# button1.grid(row=1, column=0)
#
# root.mainloop()

from tkinter import *
# tkinter의 기능을 사용하기 위해 소환

win = Tk()  # 기본 윈도우 생성
win.geometry("312x324")  # 창 크기 설정
win.resizable(0, 0)  # 사이즈 조정안되게
win.title("DW's Calculator")  # 창에 출력될 텍스트

def btn_click(item):  # item을 입력 받는다
    global expression  # GV expression 사용
    expression += str(item)  # expression에 입력값 추가
    input_text.set(expression)  # input_text라는 변수에 set()으로 문자열 저장
# 이 메서드의 기능은 입력을 할 때마다 업데이트를 해준다

def bt_clear():  # 입력값을 받지 않아도 된다
    global expression  # GV expression 사용
    expression = ""  # expression에 ""를 넣어 기존값을 overwrite 한다.
    input_text.set("")  # input_text라는 변수에 set()으로 " " 문자열 저장 = 지운다
# 이 메서드는 입력된 값을 지울 때 사용한다

def bt_equal():  # 이미 입력된 값들을 활용하므로 입력이 별도로 필요하지 않다
    global expression  # GV 변수 사용
    result = str(eval(expression))  # eval은 string type의 숫자를 연산 가능하게 한다
    input_text.set(result)  # input_text라는 변수에 set()으로 result를 저장한다
    expression = ""  # 계산이 되면 기존에 있던 값을 지운다.
# 이 메서드는 입력된 값을 계산하는데 사용한다

expression = ""  # GV 선언

input_text = StringVar()
# 입력된 인스턴스를 얻기위해 사용
# StringVar()는 tkinter에서 사용하는 문자열 변수를 사용하게 하게 해줌

input_frame = Frame(win, width=312, height=50, bd=0,
                    highlightbackground="black", highlightcolor="black", highlightthickness=2)
# 입력받는 곳의 창 크기 설정
input_frame.pack(side=TOP)
# 창에서 top쪽에 배치

input_field = Entry(input_frame, font=('arial', 18, 'bold'),
                    textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
# text를 입력받는 필드 input_frame 안에 들어가게 해야하므로 Entry(input_frame) 입력

input_field.grid(row=0, column=0)
# input_filed의 위치를 0,0에다가 둔다

input_field.pack(ipady=10)
# 위젯에대한 y방향 내부 패딩 상수 변경 불가능

# input받는 곳 밑의 프레임 만들기
btns_frame = Frame(win, width=312, height=272.5, bg="grey")
# Frame 넓이  넓이 지정하기
btns_frame.pack()

# 첫번째 줄
# ipadx ipady 위젯에 대한 x,y방향 내부 패딩 상수
# padx, pady 위젯에 대한 x,y 방향 외부 패딩 상수
# columspan 열 위치 조정
# lamda argument : expression
# command = lambda: 함수(매개변수1, 매개변수2)
# 메서드는 코드중복과 코드를 모듈화 하기 위해 사용된다.
clear = Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee",
               cursor="hand2", command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee",
                cursor="hand2", command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

# 두번째줄

seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff",
               cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)

eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff",
               cursor="hand2", command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)

nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff",
              cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)

multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee",
                  cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

# 세번째줄

four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff",
              cursor="hand2", command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)

five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff",
              cursor="hand2", command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)

six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff",
             cursor="hand2", command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)

minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee",
               cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

# 네벗째 줄

one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff",
             cursor="hand2", command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)

two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff",
             cursor="hand2", command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)

three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff",
               cursor="hand2", command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)

plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee",
              cursor="hand2", command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

# 다섯번째 줄
zero = Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee",
               cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)

equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee",
                cursor="hand2", command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)

win.mainloop()