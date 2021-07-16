''' 9장 연습문제 5번  출력 음... '''

a = {10, 20, 30, 40, 50, 60}
b = {30, 40, 50, 60, 70, 80}
i = a & b
c = sorted(a - i)
d = sorted(b - i)

print(i)
print("어느 한 쪽에만 있는 요소들",list(c),list(d))
