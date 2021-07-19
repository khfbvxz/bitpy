'''모듈'''
'''
'어떤 것의 일부' , '부품'   특정 기능을 하는 컴퓨터 시스템
기능별 단위로 구분한 것   데이터, 함수, 클래스 등을 모아서 파일로 저장해 놓은 것
'''
'''모듈 가져오기 '''
# import math
# result = math.gcd(255, 300)
# print(result)
''' 모듈 이름없이 함수 이름만 쓰고 싶은 경우'''
# from math import *
# result = gcd(255, 300)
# print(result)

'''tkinter  그래픽 사용자 인터페이스
  TK interface
  파이썬을 설치할 때 기본으로 포함되는 그래픽 모듈
  윈도우를 생성하고 위젯을 이용하여 사용자와 상호작용하는 프로그램을 작성할 수
있도록 함.
  기본적인 도형을 빠르게 그릴 수 있음
 '''
''' tkinter의 위젯들
Button      간단한 버튼 수행할 때
Canvas      화면에 무엇인가를 그릴떄
Checkbutton 2가지의 구별되는 값을 가지는 변수를 표현
Entry       한 줄의 텍스트를 입력받는 필드
Frame       컨테이너 클래스  프레임은 경계선과 배경을 가지고 있음, 다른 위젯들을 그룹핑하는데 사용
Label       텍스트나 이미지를 표시
Listbox     선택사항을 표시
Menu        메뉴를 펴ㅛ시 풀다운메뉴나 팝업 메뉴가 가능
Menubutton  메뉴 버튼 풀가운 메뉴가능
Message     텍스트를 표시합니다. Label 위젯과 비슷합니다. 하지만 자동적으로 주어진 크기로 텍스트 축소
Radiobutton 여러 값을 가질 수 있는 변수를 표시
Scale       슬라이더를 끌어서 값을 입력하는 데 사용
Scollbar    캔버스, 엔트리, 리스트 박스, 텍스트 위젯을 위한 스크롤바
Text        형식을 가지는 테스트 표시
Toplevel    최상위 윈도우로 표시되는 독립적인 컨테이너
LabelFrame  경계선과 제목을 가지는 프레임 위젯의 변형
PaneWindow  자식 위젯들을 크기조졸이 가능한 패널로 관리하는 컨테이너 위젯,
Sprinbox    특정한 범위에서 값을 선택하는 엔트리 위젯의 변형
단순 위젯 : Button, Canvas, Checkbutton, Entry, Label, Message
컨테이너 위젯 : Frame, Toplevel, LavelFrame, PanedWindow

윈도우 배치 관리자 (Layout manager)
Pack  압축 배치 관리자
Place 절대 배치 관리자 또는 absolute
Grid  격자 배치 관리자 
'''
# from tkinter import *
# def process1():
#     print("안녕하세요?")
# def process():
#     temperature = float(e1.get())
#     mytemp = (temperature-32)*5/9
#     e2.insert(0,str(mytemp))
# window = Tk()
# button = Button(window, text="클릭하세요!", command=process1)
# button.pack()
# bg="배경색" fg="글자색?"
# w = Label(window, text="박스 #1", bg="red", fg="white")
# w.place(x=0, y=0)
# w = Label(window, text="박스 #2", bg="green", fg="black")
# w.place(x=20, y=20)
# w = Label(window, text="박스 #3", bg="blue", fg="white")
# w.place(x=40, y=40)


# l1 = Label(window, text="화씨", font='helvetica 16 italic') # 폰투
# l2 = Label(window, text="섭씨")
# l1.grid(row=0, column=0)
# l2.grid(row=1, column=0)
#
# e1 = Entry(window,bg="green",fg="yellow")
# e2 = Entry(window)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
#
# b1 = Button(window, text="화씨->섭씨", command=process)
# b2 = Button(window, text="섭씨->화씨",font='helvetica 12 italic')
# b1.grid(row=2, column=0)
# b2.grid(row=2, column=1)


# import tkinter as tk
# def open():
#     pass
# def quit():
#     window.quit()
# window = tk.Tk() #윈도우 생성
# menubar = tk.Menu(window)
# filemenu = tk.Menu(menubar)
#
# filemenu.add_command(label="열기", command=open)
# filemenu.add_command(label="종료", command=quit)
#
# menubar.add_cascade(label="파일", menu=filemenu)
# window.config(menu=menubar)
# window.mainloop()

'''my paint 프로그램'''
# from tkinter import *
#
# def paint(event):
#     x1,y1 = (event.x-1), (event.y+1)
#     x2, y2 = (event.x - 1), (event.y + 1)
#     canvas.create_oval(x1, y1, x2, y2)
# window = Tk()
# canvas = Canvas(window)
# canvas.pack()
# canvas.bind("<B1-Motion>",paint)
# window.mainloop()

'''라이브러리 
PIL(Python Imaging Libary) 또는 필로우(Pillow) 영상처리 라이브러리
맷플롯립(Matplotlib)
 : 자료를 차트나 플롯(plot)으로 시각화(visualization)하는 라이브러리
넘파이(Numpy)
 : 통계, 선형대수, 행렬계산, 금융운용 등을 포함한 과학 계산과 수학작업에 많이 사용되는 라이브러리
Scrapy : 웹에서 자료를 모을 때 사용하는 라이브러리
파이게임(Pygame) 게임을 제작하기 위한 프레임워크
pip 파이썬 표준 패키지 
pip 실행할수있는지 확인하는 방법
'''
# from PIL import Image, ImageTk
# import tkinter as tk
# window = tk.Tk()
# canvas = tk.Canvas(window,width=500,height=500)
# canvas.pack()
# img = Image.open("E:\\kao.png")
# tk_img=ImageTk.PhotoImage(img)
# canvas.create_image(250, 250, image=tk_img)
# window.mainloop()

'''맷플롯립'''
from matplotlib import pyplot as plt

# x = [1, 2, 3]
# y = [1, 2, 3]
#
# plt.plot(x, y, marker='o')
# plt.title("My Plot")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.legend(["test"])
# plt.show()

from matplotlib import pyplot as plt
import csv
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="C:\Windows\Fonts\malgun.ttf").get_name()
rc('font', family=font_name)

infile = open("e:\\input2.csv","r")
data = csv.reader(infile)
x=[]
y=[]
for line in data:
    x.append(line[0])
    y.append(float(line[2]))
plt.plot(x, y, marker='o')
plt.title("2009년")
plt.xlabel("월")
plt.ylabel("강수량")
plt.show()
infile.close()