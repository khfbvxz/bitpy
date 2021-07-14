##print(2+17)
##print(2-17)
##print(2*17)
##print(17**2)
##print(10*2**7)
##print(2**2**3)
##print(17/5)      #실수 나눗셈
##print(17//5)     #정수 몫


##p = int(input("나누어지는 수를 입력하시오: "))
##q = int(input("나누는 수를 입력하시오: "))
##print("나눗셈의 몫=", p//q)
##print("나눗셈의 나머지=", p%q)


##sec =1000
##min = sec//60
##remainder = sec % 60
##print(min,'분',remainder,'초')


##x = y = 100
##print(x)
##print(y)


##x=1000
##print("초깃값 x=",x)
##x+=2
##print("x += 2 후의 x=",x)
##x-=2
##print("x -= 2 후의 x=",x)

##x=int(input("첫 번째 수:"))
##y=int(input("첫 번째 수:"))
##z=int(input("첫 번째 수:"))
##
##avg = (x+y+z)/3
##print("평균",avg)


##x=(-1)
##y=3
##print((-y)**3 + 2*(x**2)*y)


##F=int(input("화씨온도: "))
##C=(F-32)*(5/9)
##print("섭씨온도:",C)


##x1=int(input("x1:"))
##y1=int(input("y1:"))
##x2=int(input("x2:"))
##y2=int(input("y2:"))
##result=(((x2-x1)**2)+((y2-y1)**2))**0.5
##
##print("두 점 사이의 거리= ",result)


##r=141.4
##import turtle
##t=turtle.Turtle()
##t.shape("turtle")
##t.left(45)
##t.forward(r)
##t.up()
##t.goto(0,0)
##t.down()
##t.goto(100,0)
##t.goto(100,100)
##t.setheading(90)

#t.setheading() : 터틀의 머리 방향으 특정한 각도로 설정합니다.


##import time
##sec=time.time()
##x_1=sec//60   # 전체시간 (분)단위
##realmin=x_1%60
##x_2=x_1//60
##realhour=x_2%24
##korea=realhour+9
##print("현재 한국 시간: ",korea,"시",realmin,"분")



##insert = int(input("투입한 돈: "))
##price = int(input("물건가격: " ))
##change = insert-price
##print("거스름돈: ",change)
##five=int(change//500)
##one=int((change-(five*500))//100)
##print("500원 동전의 개수: ",five)
##print("100원 동전의 개수: ",one)
