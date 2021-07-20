# from tkinter import *
# from tkinter import ttk
# '''
# 윈도우창 +타이틀
# 입력받는 필드 Entry
# 버튼
# '''
# # 함수 추가
# def button_pressed(number):
#     current = number_cal.get()
#     number_cal.delete(0, END)
#     number_cal.insert(0,current+number) #텍스트 창으로 숫자 전송 'end' 오른쪽 .insert 에러
#     print(number,"pressed")
# def button_clear():
#     number_cal.delete(0,END)
#
# def button_add():
#         first_num = number_cal.get()
#         global f_num
#         global math
#         math='add'
#         f_num=int(first_num)
#         number_cal.delete(0,END)
#
#
# window = Tk()
# window.title("myu_계산기")
# window.geometry("320x600") #창 너비, 높이 위치 설정 w h +- x +- y
#
# # 텍스트 창의 값 저장할 변수.
# entry_value = StringVar(window, value='')
# # 숫자 및 결과 표시창
# number_cal = Entry(window, textvariable=entry_value,width=10)
# number_cal.grid(row=0, column=0, columnspan=4,ipadx=80, ipady=40)
# # ipadx ipady 그 창 x y 크기
# # photo = PhotoImage(file="")
# button_squared  = Button(window, text="^", width=10,height=5,fg="white",bg="black",command=lambda: button_pressed('^'));button_squared.grid(row=1, column=0)
# button_sqrt     = Button(window, text="sqrt", width=10,height=5,command=lambda: button_pressed('1'));button_sqrt.grid(row=1, column=1)
# button_clear    = Button(window, text="c", width=10,height=5, command=button_clear());button_clear.grid(row=1, column=2)
# button_back     = Button(window, text="<-", width=10,height=5, command=lambda: button_pressed('1'));button_back.grid(row=1, column=3)
#
# button1 = Button(window, text="1", command=lambda: button_pressed('1'));button1.grid(row=2, column=0) #lambda 익명 함수
# button2 = Button(window, text="2", width=10,height=5, command=lambda: button_pressed('2'));button2.grid(row=2, column=1)
# button3 = Button(window, text="3", width=10,height=5, command=lambda: button_pressed('3'));button3.grid(row=2, column=2)
# button_div = Button(window, text="/", width=10,height=5, command=lambda: button_pressed('/'));button_div.grid(row=2, column=3)
#
# button4 = Button(window, text="4", width=10,height=5, command=lambda: button_pressed('4'));button4.grid(row=3, column=0)
# button5 = Button(window, text="5", width=10,height=5, command=lambda: button_pressed('5'));button5.grid(row=3, column=1)
# button6 = Button(window, text="6", width=10,height=5, command=lambda: button_pressed('6'));button6.grid(row=3, column=2)
# button_mul = Button(window, text="*", width=10,height=5, command=lambda: button_pressed('*'));button_mul.grid(row=3, column=3)
#
# button_7 = Button(window, text="7", width=10,height=5, command=lambda: button_pressed('7'));button_7.grid(row=4, column=0)
# button_8 = Button(window, text="8", width=10,height=5, command=lambda: button_pressed('8'));button_8.grid(row=4, column=1)
# button_9 = Button(window, text="9", width=10,height=5, command=lambda: button_pressed('9'));button_9.grid(row=4, column=2)
# button_sub = Button(window, text="-", width=10,height=5, command=lambda: button_pressed('-'));button_sub.grid(row=4, column=3)
#
# button_0 = Button(window, text="0", width=10,height=5, command=lambda: button_pressed('0'));button_0.grid(row=5, column=0)
# button_point = Button(window, text=".", width=10,height=5, command=lambda: button_pressed('.'));button_point.grid(row=5, column=1)
# button_equal = Button(window, text="=", width=10,height=5, );button_equal.grid(row=5, column=2)
# button_add = Button(window, text="+", width=10,height=5, command=button_add());button_add.grid(row=5, column=3)
#
# window.mainloop()

# import tkinter as tk
# operator={'+':1,''}
# def Button_clear():
#
#
# window =tk.Tk()
# window.title("계산기_v.뮤")
#
# entry_value = tk.StringVar()
# displays = tk.Entry(window,textvariable = entry_value)
# displays.grid(row=0, column=0,columnspan=4)
#
#
#
#
# tk.Button(window, text="1", width=10,height=5).grid(row=1, column=0)
# tk.Button(window, text="2", width=10,height=5).grid(row=1, column=1)
# tk.Button(window, text="3", width=10,height=5).grid(row=1, column=2)
# tk.Button(window, text="0", width=10,height=5).grid(row=1, column=3)
# tk.Button(window, text="0", width=10,height=5).grid(row=2, column=0)
# tk.Button(window, text="0", width=10,height=5).grid(row=2, column=1)
# tk.Button(window, text="0", width=10,height=5).grid(row=2, column=2)
# tk.Button(window, text="0", width=10,height=5).grid(row=2, column=3)
# tk.Button(window, text="0", width=10,height=5).grid(row=3, column=0)
# tk.Button(window, text="0", width=10,height=5).grid(row=3, column=1)
# tk.Button(window, text="0", width=10,height=5).grid(row=3, column=2)
# tk.Button(window, text="0", width=10,height=5).grid(row=3, column=3)
# tk.Button(window, text="0", width=10,height=5).grid(row=4, column=0)
# tk.Button(window, text="0", width=10,height=5).grid(row=4, column=1)
# tk.Button(window, text="0", width=10,height=5).grid(row=4, column=2)
# tk.Button(window, text="0", width=10,height=5).grid(row=4, column=3)
# window.mainloop()

import tkinter as tk
from tkinter.font import Font

results=""
results1=""
results2=""
def Button_click(event):
    print(event)

    global results1
    results1 += str(event)
    results=results1
    text_value.set(results)
    print(results)
def clear():
    global results1
    results1 =""
    displays.delete(0, tk.END)

def enter():
    global results1
    try:
        in_results=eval(results1)
        displays.delete(0,tk.END)
        displays.insert(0,in_results) # 계산 결과 출력력    # results=0
        results1=""
    except:
        displays.delete(0, tk.END)
        displays.insert(0, '다시 입력하세요')
        results1 = ""
def backspace():
    global results1
    results2 = results1[:-1]
    text_value.set(results2)
    results1 = results2

window=tk.Tk()
window.title("myu_계산기")
window.geometry("800x600")
window.resizable(0,0)
font = Font(family='Comic Sans MS',size=30)
text_value = tk.StringVar()
displays = tk.Entry(window,textvariable = text_value,justify="right",font=font
                    )

displays.grid(row=0, column=0,columnspan=4,ipadx=80, ipady=40)
# displays.pack() #위치를 정해주는 명령어
# 파이 루트 제곱 e 00
tk.Button(window, text="c", width=10,height=5,command=lambda :clear()).grid(row=1, column=0)
tk.Button(window, text="(", width=10,height=5,command=lambda :Button_click('(')).grid(row=1, column=1)
tk.Button(window, text=")", width=10,height=5,command=lambda :Button_click(')')).grid(row=1, column=2)
tk.Button(window, text="/", width=10,height=5,command=lambda :Button_click('/')).grid(row=1, column=3)
tk.Button(window, text="7", width=10,height=5,command=lambda :Button_click('7')).grid(row=2, column=0)
tk.Button(window, text="8", width=10,height=5,command=lambda :Button_click('8')).grid(row=2, column=1)
tk.Button(window, text="9", width=10,height=5,command=lambda :Button_click('9')).grid(row=2, column=2)
tk.Button(window, text="*", width=10,height=5,command=lambda :Button_click('*')).grid(row=2, column=3)
tk.Button(window, text="4", width=10,height=5,command=lambda :Button_click('4')).grid(row=3, column=0)
tk.Button(window, text="5", width=10,height=5,command=lambda :Button_click('5')).grid(row=3, column=1)
tk.Button(window, text="6", width=10,height=5,command=lambda :Button_click('6')).grid(row=3, column=2)
tk.Button(window, text="-", width=10,height=5,command=lambda :Button_click('-')).grid(row=3, column=3)
tk.Button(window, text="1", width=10,height=5,command=lambda :Button_click('1')).grid(row=4, column=0)
tk.Button(window, text="2", width=10,height=5,command=lambda :Button_click('2')).grid(row=4, column=1)
tk.Button(window, text="3", width=10,height=5,command=lambda :Button_click('3')).grid(row=4, column=2)
tk.Button(window, text="+", width=10,height=5,command=lambda :Button_click('+')).grid(row=4, column=3)
tk.Button(window, text="0", width=10,height=5,command=lambda :Button_click('0')).grid(row=5, column=0)
tk.Button(window, text=".", width=10,height=5,command=lambda :Button_click('.')).grid(row=5, column=1)
tk.Button(window, text="<-", width=10,height=5,command=lambda :backspace()).grid(row=5, column=2)
equals=tk.Button(window, text="=", width=10,height=5,command=lambda :enter())
equals.grid(row=5, column=3)

window.mainloop()