# ch07 추가 연습문제 2번
import random
values=[]
for i in range(5):
    values.append(random.randint(1,20))
print(values)

for j in range(5):
    print(str(values[j])+"\t\t"+'*'*int(values[j]))

