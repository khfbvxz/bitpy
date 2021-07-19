'''클래스 와 객체'''
'''
class  
객체 (object)
'''
# class Cookie:
#    pass
# a = Cookie() # a , b 가 객체  a객체는 Cookie 의 인스턴스
# b = Cookie()

'''사칙연산 클래스 만들기'''
class FourCal:
   #pass #pass는 아무것도 수행하지 않는 문법으로 임시로 코드를 작성할 때 주로 사용한다.
   # 클래스 안에 구현된 함수 매서드(Method)
   #__init__ 메서드의 init 앞뒤로 붙은 __는 언더스코어(_) 두 개를 붙여 쓴 것이다.
   def __init__(self, first, second): #생성자
      self.first = first
      self.second = second
   def setdata(self, first, second):  # 첫번쨰 매개변수 self 객체 자동으로 전달
      self.first = first
      self.second = second
   def add(self):
      result = self.first + self.second
      return result
   def mul(self):
      result = self.first * self.second
      return result
   def sub(self):
      result = self.first - self.second
      return result
   def div(self):
      result = self.first / self.second
      return result

# a = FourCal()  # 객체 생성! FourCal 사칙연산 가능하게 하는 클래스
# b = FourCal()
# a.setdata(4, 2) #숫자 4와 2를 a에 지정   객체.메서드
# b.setdata(3, 7)
# print(a.sub()); print(a.add()); print(a.mul()); print(a.div())
c = FourCal(8, 2)
print(c.first); print(c.second); print(c.add())
# FourCal.setdata(a, 4, 2)    # 클래스 이름.메서드
# print(type(a)) #type 함수는 파이썬이 자체로 가지고 있는 내장 함수로 객체 타입을 출력한다.
# print(a.first);print(a.second);
# id 함수는 객체의 주소를 돌려주는 파이썬 내장 함수이다.
# id(a.first) # a의 first 주소값을 확인
# id(b.first) # a의 first 주소값을 확인

'''
생성자 
setdata 메서드 호출하여 초깃값 설정하는 것 보다는 
!!!!생성자를 구현하는 것이 안전한 방법!!!!
'''
'''
클래스의 상속 
class 클래스이름 (상속할 클래스 이름)
보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다.
'''
class MoreFourCal(FourCal): #FourCal 클래스의 모든 기능을 사용할 수 있어야 한다.
   def pow(self):
      result = self.first ** self.second
      return result
d = MoreFourCal(4, 2)
print(d.pow())

'''메서드 오버라이딩
메서드를 동일한 이름으로 다시 만드는 것!
부모 클래스의 메서드 대신 오버라이딩한 메서드가 호출됨!!
'''
class SafeFourCal(FourCal):
   def div(self):
      if self.second == 0:
         return 0
      else:
         return  self.first / self.second
e = SafeFourCal(4, 0)
print(e.div())
'''클래스 변수  클래스이름.클래스 변수'''
class  Family:
   lastname = "김"
a = Family()
b = Family()
print(a.lastname)
# 김
print(b.lastname)
# 김
Family.lastname = "박"
print(a.lastname)
# 박
print(b.lastname)
# 박
# id 값이 모두 같으므로 Family.lastname, a.lastname, b.lastname은 모두 같은 메모리를 가리키고 있다.
