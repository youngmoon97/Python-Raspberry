import random


fruit = ['사과','배','딸기','수박']
print(fruit)
fruit.append('바나나')
print(fruit)
if '딸기' in fruit:
    print("딸기가 있어요~")

numbers = []
for num in range(0,10):
    numbers.append(random.randrange(0,10))
print("생성된 리스트 : ",numbers)

for num in range(0,10):
    if num not in numbers:
        print("숫자 %d는 리스트에 업세요 " %num)
