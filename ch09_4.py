''' 9장 연습문제 4번  출력 s 음...'''
str1 = input("첫 번째 문자열: ")
str2 = input("두 번째 문자열: ")
list(str1)
list(str2)
str3 = list(str1 + str2)
s = list(set(str1).intersection((str2)))
print(s)