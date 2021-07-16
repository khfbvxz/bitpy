''' 8장 추가 연습문제 3번 '''

def testPrime(n):
    for i in range(2,n+1):
        result = True
        for j in range(2,i):
            if i % j == 0:
                result = False
        if result:
            print(i,end=" ")

testPrime(100)