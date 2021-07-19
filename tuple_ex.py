'''
튜플 몇가기 점 제외하곤 리스트와 거의 비슷
차이첨
리스트는 [ ]   튜플 ( )
리스트는 그 값의 생성, 삭제, 수정 가능
튜플은 그 값 바꿀 수 없음!!!

'''

t1 = ()
t2 = (1,)  # 1개의 요소만 가질 때 요소 뒤 반드시 , 콤마 붙여야함
t3 = (1, 2, 3)
t4 = 1, 2, 3   # 괄호 () 생략해도 무방
t5 = ('a','b', ('ab', 'cd'))

''' 튜플 요소값 삭제 및 변경 '''
t6 = (1, 2, 'a', 'b')
# del t6[0] # 오류 TypeError: 'tuple' object doesn't support item deletion
# print(t6)
# t6[0] = 'c' # 오류 TypeError: 'tuple' object does not support item assignment
# print(t6)
'''인덱싱 하기'''
print(t6[0]); print(t6[3])
'''슬라이싱 하기'''
print(t6[1:])
'''튜플 더하기 곱하기 '''
t7 = (3, 4)
print(t6+t7); print(t7 * 3)
'''튜플 길이 구하기 len() 함수 '''
print(len(t6))