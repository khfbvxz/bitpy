#3장 1번

##chi=2
##pig=4
##cow=3
##leg=(chi*2)+(pig*4)+(cow*4)
##print("닭의 수: " ,chi)
##print("돼지의 수: " ,pig)
##print("소의 수: " ,cow)
##print("전체 다리의 수 :",leg)



#3장 2번

##x1=int(input("x1:"))
##y1=int(input("y1:"))
##x2=int(input("x2:"))
##y2=int(input("y2:"))
##result=(((x2-x1)**2)+((y2-y1)**2))**0.5
##print("두 점 사이의 거리= ",result)


#3장 3번

##r=141
##import turtle
##t=turtle.Turtle()
##t.shape("turtle")
##t.left(45)
##t.forward(r)
##t.up()
##t.goto(0,0)
##t.down()
##t.setheading(0)
##t.forward(100)
##t.left(90)
##t.forward(100)


#3장 4번  다시 풀어

'''
import turtle
t=turtle.Turtle()
t.shape("turtle")

##x1=int(input("x1:"))
##y1=int(input("y1:"))
##x2=int(input("x2:"))
##y2=int(input("y2:"))
##result=(((x2-x1)**2)+((y2-y1)**2))**0.5
##r=result
x1=turtle.textinput("x1:","x1의 값을 입력하세요")
y1=turtle.textinput("y1:","y1의 값을 입력하세요")
x2=turtle.textinput("x2:","x2의 값을 입력하세요")
y2=turtle.textinput("y2:","y2의 값을 입력하세요")
##result=(((x2-x1)**2)+((y2-y1)**2))**0.5
t.goto(x1,y1)
t.up
t.goto(x2,y2)
t.down
t.write("선의 길이="+((((x2-x1)**2)+((y2-y1)**2))**0.5))
##t.write("직선의 길이="+result);
'''

import time
sec=time.time()
x_1=sec//60   # 전체시간 (분)단위
realmin=int(x_1%60)
x_2=x_1//60
enghour=int(x_2%24+1)

print("현재 시간(영국 그리니치 시각): ",enghour,"시",realmin,"분")


