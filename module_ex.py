'''
모튤 : 함수니 변수 또는 클래스를 모아 놓은 파일
      다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일
'''

'''모듈 만들기'''
# mod1.py
# def add(a, b):
#     return a + b
# def sub(a, b):
#     return a-b
# import mod1  모듈 이름
# import mod1
# print(mod1.add(3, 4))
# 같은 파일안에 넣을 것  # 폴터이름.파일이름 as 닉네임(단축)
#다른곳에서 지정해서 불러오고 싶다면

# from mod1 import add #from 모듈이릉 import 함수이름 모듈 이름 없이 함수 이름만 사용하고싶을 때
# print(add(3, 4))
# from mod1 import add,sub #from 모듈이릉 import 함수이름 모듈 이름 없이 함수 이름만 사용하고싶을 때
# from mod1 import *
# # * 문자는 "모든 것"
# print(add(3, 4)); print(sub(3, 4))
# import sys
# sys.path는 파이썬 라이브러리가 설치되어 있는 디렉터리를 보여 준다.
# sys.path.append('모듈의 경로') #경로 추가후
# import 사용
''' if __name__ == "__main__": 의 의미 '''
'''mod1.py 파일을 변경 '''
'''
if __name__ == "__main__"을 사용하면 C:\doit>python mod1.py처럼 직접 이 파일을
실행했을 때는 __name__ == "__main__"이 참이 되어 if문 다음 문장이 수행된다. 반대
로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는 __name__ ==
"__main__"이 거짓이 되어 if문 다음 문장이 수행되지 않는다.
'''
'''
__name__ 뱐수
파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다. 
만약 C:\doit>python mod1.py처럼 직접 mod1.py 파일을 실행할 경우 mod1.py의 __name__ 변수에는 
__main__ 값이 저장된다. 
하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import 할 경우에는 mod1.py의 __name__ 
변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다.
mod1.__name__
'''
import mod2
print(mod2.PI)
print(mod2.add(mod2.PI, 4.4))
