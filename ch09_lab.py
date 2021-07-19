'''가위바위보 게임'''

# import random
#
# def  match(com, my):
#     if match_t[com] == my:
#         return '졌습니다.'
#     elif com == my:
#         return '비겼습니다.'
#     else:
#         return '이겼습니다.'
# dic_val = { 1:'가위' , 2:'바위', 3:'보'}
# match_t = {'가위':'보', '바위':'가위', '보':'바위'}
# comrad = dic_val[random.randint(1,3)]
# mine = input('가위, 바위, 보 입력 : ')
# result = match(comrad, mine)
# print(result)

'''행성까지 여행 시간'''
'''
거리 = 속 * 시
'''
# planet_table = {'수성':9170007000, '금성':414000000,
#                '화성': 78400000, '목성':628700000,
#                 '토성':1277400000, '천왕성':2750400000,
#                 '해왕성':4347400000 }
# planet_name = input("행성 이름: ")
# speed = int(input("이동속도(km/h): "))
# distance = planet_table[planet_name]  #거리 value 가져오기
# time = distance / speed  # 시간 = 거리/속력  실수값
# year = int(time) // (365*24)   # 정수형으로 형변황
# month = int(time - (year*365*24)) // (30 * 24) # 한달 30일 가정
# day = int(time - (year*365*24) - (month*30 * 24)) // 24
# hour = int(time - (year*365*24) - (month*30 * 24)-day*24)
# print("이동시간: 약",time," 시간")
# print("이동시간: 약",year,"년",month,"월",day,"일",hour,"시간")

'''멘델의 유전법칙 시뮬레이션'''
# import random
# # 0=R # 1=r
# bean_table = []
# def make_bean():  # 우성 열성 완두콩 만드는 함수
#     a = random.randrange(0, 2)
#     b = random.randrange(0, 2)
#     if a == 0 and b == 0:
#         c = 'RR'
#     elif a == 0 and b == 1:
#         c = 'Rr'
#     elif a == 1 and b == 0:
#         c = 'rR'
#     else:
#         c = 'rr'
#     bean_table.append(c)  # 만든 완두콩 리스트에 추가
# def count_bean(b_t): # RR Rr rR rr 갯수 카운트 함수
#     b_t_dict = { }
#     for j in b_t:
#         if j in b_t_dict:
#             b_t_dict[j] += 1
#         else:
#             b_t_dict[j] = 1
#     print(b_t_dict)  # 카운트된 딕셔너리 출력
#     rate(b_t_dict)   # 비율 함수 호출
# def rate(b_t):
#     rate = ((b_t['RR']+b_t['Rr']+b_t['rR'])/b_t['rr'])
#     print(rate,": 1")     #비율 결과 출력 함수
# for i in range(1, 100):   # 100번 반복!
#     make_bean()
# count_bean(bean_table)

'''튜링상 수상자 데이터 분석'''
'''
딕셔너리 
리스트
정리
'''
# turing_awards = []  #리스트
# turing_awards.append({'이름': '팀 버너스리', '수상년도': 2016, '국적': '영국', '대표업적': '월드 와이드 웹의 하이퍼텍스트 시스템을 고안하여 개발'})
# turing_awards.append({'이름': '리처드 해밍', '수상년도': 1968, '국적': '미국', '대표업적': '오류 검출 부호 및 오류 정정 부호'})
# turing_awards.append({'이름': '에츠허르 데이크스트라', '수상년도': 1972, '국적': '네덜란드', '대표업적': '프로그래밍 언어 연구, 데이터스트라 알고리즘'})
# turing_awards.append({'이름': '더글라스 엥겔바트', '수상년도': 1977, '국적': '미국', '대표업적': '마우스의 발명, 대화형 컴퓨팅'})
# turing_awards.append({'이름': '데니스리치', '수상년도': 1983, '국적': '미국', '대표업적': '유닉스 운영 체제 개발, C언어 개발'})
#
# for award in turing_awards:
#     print(award['이름'])
#
# for award in turing_awards:
#     if award['수상년도'] <= 1990:
#         print(award['이름'],award['수상년도'])
#
# nationality = set()
# for award in turing_awards:
#     nationality.add(award['국적'])
# print(nationality)

'''파이썬으로 이메일 보내기'''
'''
SMTP(Simple Mail Transfer Protocol) : 인터넷에서 이메일을 보내기 위해 이용되는 프로토콜
MINE(Multipurpose Internet Mail Extensions) : 전자 우편을 위한 표준 포멧
euc-kr : 인코딩 표준
'''
# import smtplib                       # 메일을 쓰기 위한 모듈
# from email.mime.text import MIMEText
#
# send_email = 'khfbvxz@gamil.com'
# recipient_email = 'khfbvxz@naver.com'
# contents = '파이썬 이메일 보네기'
#
# msg = MIMEText(contents, _charset='euc-kr')
# msg['Subject'] = '파이썬 이메일 보내기 '  # Subject 는 키
#
# msg['From'] = send_email
# msg['To'] = recipient_email
#
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.ehlo()
# server.starttls()
# server.ehlo()
#
# server.login("khfbvxz","yuhwan0625")
# server.sendmail(send_email,recipient_email,msg.as_string())
# server.quit()