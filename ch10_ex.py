# infile = open("E:\\phones1.txt", "r")
# lines = infile.read(n)   앞에서 부터 n개의 문자 출력
# lines = infile.readlines()  #['홍길동 010-1234-5678\n', '김철수 010-1111-2222\n', '김영희 010-3333-4444']
#                              #<class 'list'>  줄 바뀜 부분 마다 리스트 형태로
# print(lines)
# print(type(lines))    문자열 str
# infile.close()

# infile = open("E:\\phones4.txt", "r", encoding="UTF8")
# line1 = infile.readline()
# print(line1)
# line2 = infile.readline()
# print(line2)
# line3 = infile.readline()
# print(line3)
# infile.close()
'''파일 한줄씩 읽어오기 rstrip 파이썬 검색해서 확인 '''
# infile = open("e:\\phones1.txt", "r")
# line = infile.readline( ).rstrip() # rstrip의 역할 줄바꿈기호 삭제하고 읽을 수 있음
# # 전우치 010-8888-9999 \n <줄바꿈 개행문자   enter
# # while line != "":  #라인이 데이터 없이 공백이면 끝
# #     print(line)
# #     line = infile.readline( ).rstrip( )
# for line in infile:
#     line4 = line.rstrip()
#     print(line4)
#
# infile.close( )

'''파일에 데이터 쓰기'''
# outfile = open("e:\\phones1.txt", "w")
#
# outfile.write("전우치 010-8888-9999\n")
# outfile.write("홍길동 010-7878-3434\n")
# outfile.write("김서방 010-2222-1111\n")
# outfile.close()

'''파일에 새로운 데이터 이어서 쓰기'''
# outfile = open("e:\\phones1.txt", "a")
# outfile.write("강감찬 010-2222-3333\n")
# outfile.write("김유신 010-4567-5678\n")
# outfile.write("정약용 010-2323-1212\n")
# outfile.close()
'''파일에서 단어 단위로 읽어오기'''
'''split() 함수 공백문자 기준으로 해서 단어 분리'''
# a = "All's well that ends well"
# print(a.split())
# infile = open("e:\\wether.txt","r")
# for line in infile:
#     word_list = line.split()
#
#     for word in word_list:
#         print(word)
# infile.close()

'''csv파일을 사용해보기'''
import csv
f = open("e:\\input.csv", "r", encoding="UTF-8")
data = csv.reader(f)
for line in data:
    print(line)
f.close()
'''
파이선에서 파일을 읽을때 아래와 같은 오류가 표시된다면,
UnicodeDecodeError: 'cp949' codec can't decode byte 0xe2 in position 6987: illegal multibyte sequence
아래와 같이 파일을 여세요.
open('파일경로.txt', 'rt', encoding='UTF8')
cp949 코덱으로 인코딩 된 파일을 읽어들일때 요런 문제가 생긴다고 하는 군요.
'''

# text = ' Water boils at 100 degrees '  # Water boils at 100 degrees
# t = 'a'
# print(text)
# print(text.strip(' Water '))    # 맨 왼쪽부터 왼쪽 !!!!!!!
# print(text.lstrip(' Water boils '))
# print(text.lstrip(' Water boils  '))
# print(text.lstrip(' Water boils'))
# print(text.rstrip(' 100 degrees '))  # 오른쪽
# print(t); print(int(t))
# print(text.rstrip('at 100 degrees '))  # 오른쪽
# print(text.strip(' degrees '))         # 양쪽