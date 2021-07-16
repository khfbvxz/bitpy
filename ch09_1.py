''' 9장 연습문제 1번'''
''' set(myList)'''
myList = [80, 20, 20, 30, 60, 30]

print("주어진 리스트: ", myList)
new_myList = sorted(set(myList))
print('정리된 리스트: ', new_myList)
