'''계산기 만들기 과제'''
import tkinter as tk

cal_values = 0
oprator = {'+':1, '-': 2, '/': 3,'*': 4,'C': 5,'=': 6}#딕셔너리 사용 명령을 정수로 치환
stovalue = 0 # 더하기 할것지 빼기할건지
opPre = 0  #이전 op 무엇인지 알기위해 변수 선언
def clear():
    global cal_values, stovalue, opPre
    cal_values = 0
    opPre = 0
    stovalue = 0
    str_value.set(cal_values) # 0을 다시 출력
def number_click(value):
    # print('숫자',value)
    global cal_values
    cal_values = (cal_values*10) + value  # 숫자 누르면 자리수 증가되게
    str_value.set(cal_values)
def oprator_click(value):
    # print('명령',value)
    #현재 눌린것과 이전에 눌린게 무엇인지 알아야함
    global cal_values, oprator, stovalue, opPre
    op = oprator[value] #키값
    if op == 5: #C
        clear()
    elif cal_values == 0: # 처음 눌럿거나 명령이 없을 때 값이 없을 떄
        opPre = 0  #이전의 명령을 초기화
    elif opPre == 0: #이전 명령이 없고 명령이 새로 눌렸을때
        stovalue=cal_values  # 현재값 저장
        cal_values = 0       # 화면 값 0으로 초기화
        str_value.set(cal_values) # 출력


    opPre = op #백업

def button_click(value):
    # print(value)
    try:
        value = int(value) # 숫자는 에러x 다른것 에러 #숫자일떄 넘버라는 함수
        number_click(value)
    except:
        oprator_click(value)

win = tk.Tk()   #윈도우 생성
win.title("뮤 계산기")

# 누를떄 연산하고 결과 출력
# 버튼을 누를떄 액션 처리
#


str_value = tk.StringVar()
str_value.set(str(cal_values)) # 문자로 변환해서 set을 하면
dis = tk.Entry(win, textvariable=str_value, justify='right') #폰트도 키우자
               # 에딧창에 계속 자동으로 업데이트  justify 숫자 어디에 배치할 것인가 columnsean 몇개 가져갈것인가가dis.grid(column=0, row=0)
dis.grid(column=0, row=0, columnspan=4, ipadx=100, ipady=50) # ipadx 크기 키우는
'''열을 어디까지 쓸것인가'''
calItem=[['1','2','3','4'],
         ['5','6','7','8'],
         ['9','0','+','-'],
         ['/','*','C','=']]
for i,items in enumerate(calItem): #i 인덱스  items 하나의 리스트 cal[i][k]
    for k,item in enumerate(items): # k 1 2 3 4 items 문자

        try:
            color = int(item)
            color = 'black'  # 숫자만
        except:
            color = 'green'   # 기호들

        bt = tk.Button(win,
                       text=item,
                       width=10,
                       height=5,
                       bg = color,
                       fg = 'red',
                       command=lambda cmd=item: button_click(cmd) # lambda 간이적인 함수
                       ) #변수 선언
        bt.grid(column=k, row=(i+1)) # +1은 실행창 때문에


# tk.Button(win, text='1', width=10, height=5).grid(column=0, row=1)
# tk.Button(win, text='2', width=10, height=5).grid(column=1, row=1)
# tk.Button(win, text='3', width=10, height=5).grid(column=2, row=1)
# tk.Button(win, text='4', width=10, height=5).grid(column=4, row=1)
#
# tk.Button(win, text='5', width=10, height=5).grid(column=0, row=2)
# tk.Button(win, text='6', width=10, height=5).grid(column=1, row=2)
# tk.Button(win, text='7', width=10, height=5).grid(column=2, row=2)
# tk.Button(win, text='8', width=10, height=5).grid(column=4, row=2)
#
# tk.Button(win, text='9', width=10, height=5).grid(column=0, row=3)
# tk.Button(win, text='0', width=10, height=5).grid(column=1, row=3)
# tk.Button(win, text='+', width=10, height=5).grid(column=2, row=3)
# tk.Button(win, text='-', width=10, height=5).grid(column=4, row=3)
#
# tk.Button(win, text='/', width=10, height=5).grid(column=0, row=4)
# tk.Button(win, text='*', width=10, height=5).grid(column=1, row=4)
# tk.Button(win, text='c', width=10, height=5).grid(column=2, row=4)
# tk.Button(win, text='=', width=10, height=5).grid(column=4, row=4)

win.mainloop()