'''ch10 추가 연습문제 1번'''
# infile = open("E:\\input.txt", "r", encoding="UTF-8") #파일 객체 생성, 파일 여는 모두"r"
# lines = infile.readlines()
# print(lines)
# infile.close()# 파일 닫기

# infile = open("E:\\input.txt", "r", encoding="UTF-8")
# line = infile.read()
# print(line)
# infile.close()
import random

'''ch10 추가 연습문제 2번'''
# infile = open("E:\\input.txt","r",encoding="UTF-8") #파일 객체 생성, 파일 여는 모두"r"
# # lines = infile.readlines( ) #  모든 줄을 읽어 lines 에 저장
# lines = infile.read()
# # print(lines)
# lists = []                  # 빈 리스트 생성
# lists.append(lines)         # lines를 lists에 저장
# print(lists)
# infile.close()# 파일 닫기
# lists = []
# for line in infile:
#     line1 = line.rstrip()
#     print(line1)
# for lists in infile:
#     # line3 =
#     lists.append(infile.readline())
# # print(lines)
# print(lists)

# infile = open("E:\\input.txt", "r", encoding="UTF-8")
# # line = infile.readlines()
# list_file = []
# for line in infile:
#     line = line.rstrip()
#     list_file.append(line)  #파일의 줄의 내용을 반복문을 통해 리스트에 추가
# # print(line)
# print(list_file)
# infile.close()

'''ch10 추가 연습문제 3번  split 이용해서 공백 제외 도 한번 하기'''
# def count_char(data): # 글자수 세는 함수
#     count = 0
#     for i in data:
#         count += len(i)  # 변수의 글자수를 세는 함수 len()사용
#     return count
# filename =input("파일 이름을 입력하세요: ") # E:\\input.txt E:\\obama.txt
# infile = open(filename,"r",encoding="UTF-8")
# list_file = []
# for line in infile:
#     line = line.rstrip()
#     list_file.append(line)  #파일의 줄의 내용을 반복문을 통해 리스트에 추가
# print("파일 안에는 총",count_char(list_file),"개의 글자가 있습니다.")
# infile.close()
# # print(list_file[1])
# # print(list_file[1].split())

# filename =input("파일 이름을 입력하세요: ") # E:\\input.txt E:\\obama.txt
# infile = open(filename,"r",encoding="UTF-8")

'''10장 lab 파일복사'''
# infile = open("e:\\phones4.txt","r",encoding="UTF-8")
# outfile = open("output2.txt","w")
# #전체파일 읽기
# s = infile.read()
# outfile.write(s)
# outfile.close()
# infile.close()
''' 10장 lab 연설문 데이터 분석'''
# 입력 파일 출력력 파일 열기
# infile = open("e:\\obama.txt","r")
# outfile = open("output.txt","w")
# '''입력파일로부터  연설문 한문단 즉 줄바꿈이 발생하기전까지 가져와서 단어별로 분리
# 반복문 알스트립이용 리스트의 형태로 저장가능 리스트에 저장된 문장 스플릿 이용하여 단어로 분리
# '''
# word_dic = { }  # 해당단어 그횟수 값
# total_count = 0 # 전체 단어수
# for line in infile:
#     line = line.rstrip()   #줄바꿈 문자를 잘라내서 다시 라인에 저장
#     word_list = line.split() # 스플릿 단어를 분리
#     for word in word_list:  #단어 처리
#         word = word.lower()  #소문자로 바꾸는 함수 lower()
#         word = word.strip(',') # 콤마 제거
#         word = word.strip('.') #마침표 제거
#
#         if word in word_dic: # 단어 세기
#             word_dic[word] += 1
#             total_count += 1
#         else:
#             word_dic[word] = 1
#             total_count += 1
# # 단어별 빈도수를 결과파일에 저장하고 총 단어수를 화면에 출력
# result = ""  #글쓰는 형식을 담아두는 변수
# for key in sorted(word_dic.keys()): #알파벳 순으로 정렬
#     result = key + " " + str(word_dic[key])+'\n'
#     outfile.write(result)
#
# print("총 단어 수 = ", total_count)
# # 입력 파일 출력 파일 닫기
# outfile.close()
# infile.close()
'''ch 10 추가연습문제 4번
https://lvolz.tistory.com/12
https://ponyozzang.tistory.com/447
https://appia.tistory.com/235
'''
# filename =input("파일 이름을 입력하세요: ") # E:\\input.txt E:\\obama.txt
# infile = open(filename,"r",encoding="UTF-8")
# line = infile.read()
# Alphabat = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' #알파벳 문자열 생성
# print(Alphabat[2])
# ch_freq = [0]*52
# for ch in line:
#     if ch in Alphabat:
#         id = Alphabat.find(ch) #find() 지정한 문자가 몇번쨰에 있는지
#         ch_freq[id] += 1
# print("{",end="")
# for i in range(0,52):
#     print("'",Alphabat[i],"'", ":",ch_freq[i],end=", ")
# word_ch = [ ]  # 해당단어 그횟수 값
# total_count = 0 # 전체 단어수
# for line in infile:
#     line = line.rstrip()   #줄바꿈 문자를 잘라내서 다시 라인에 저장
#     word_list = line.split() # 스플릿 단어를 분리
#     for word in word_list:  #단어 처리
#         word = word.lower()  #소문자로 바꾸는 함수 lower()
#         word = word.strip(',') # 콤마 제거
#         word = word.strip('.') #마침표 제거
#         word = word.split()
#         print(word)
#         if i in word_ch: # 단어 세기
#             word_ch[i] += 1
#             total_count += 1
#         else:
#             word_ch[i] = 1
#             total_count += 1
# # 단어별 빈도수를 결과파일에 저장하고 총 단어수를 화면에 출력
# result = ""  #글쓰는 형식을 담아두는 변수
# for key in sorted(word_ch.keys()): #알파벳 순으로 정렬
#     result = key + " " + str(word_ch)+'\n'
# print(word_ch)
# print("총 단어 수 = ", total_count)

'''평균 강수량 통계 '''
# import csv
# f = open("e:\\weathers_dae.csv", "r")
# data = csv.reader(f) #줄단위로 읽어오는
# count = 0  # 1~12 10번 120
# sum = 0    #총 강수량
# for line in data:
#     count += 1
#     sum += float(line[2])
# print("강원도 2009년 1월 부터 2019 9월 까지 총 강수량:" , sum)
# print("강원도 2009년 1월 부터 2019 9월 까지 평균 강수량:", sum/count)
# f.close()

'''행맨'''
# infile = open("e:\\hang.txt","r",encoding="UTF-8")
# line = infile.readlines()#모든 줄 읽기
# word = random.choice(line).rstrip() # 리스트 중 항목 무작위 선탣 choice rstrip() 줄바꿈 기호 제거
# print(word)
# # 단어를 하나씩 쪼개야함
# solution = list(word) #하나하나 쪼개서 할려면 list()
# # print(solution)
# result = list('_'*len(word)) # 글자 수 만큼 --- len()변수의 길이
# # print(result)
#
# print("turtle")
# print(list("turtle"))
# print(list("_"*len("turtle")))
#
# turns = 10
# while turns > 0:
#     guess = input("단어를 추측하세요:")
#     turns -= 1
#     i = 0 # 각각의 항목 변수를 카운트하는 변수
#     for c in word:  # 단어가 같을 떄 글자 표시되게
#         if c == guess:
#             result[i] = c
#         i += 1
#     print(result)
#     if result == solution:
#         print("성공입니다.")
#         break
#     if turns <= 0:
#         print("실패하였습니다.")
#         break
#
# infile.close()