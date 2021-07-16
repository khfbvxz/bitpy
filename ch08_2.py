''' 8장 추가 연습문제 2번 '''

def add(a,b):
    result = a+b
    print("(", a, "+", b , " ) = " ,result)
    return result

def sub(a,b):
    result = a-b
    print("(", a, "-", b, " ) = ", result)
    return result

def mul(a , b):
    result = a*b
    print("(", a, "*", b, " ) = ", result)
    return result

def div(a , b):
    result = a / b
    print("(", a, "/", b, " ) = ", result)
    return result

a = 20
b = 10
add(a,b)
sub(a,b)
mul(a,b)
div(a,b)