# 리스트 : [], 요소 값의 생성, 수정, 삭제
# 튜플 : (), 요소의 값을 변경할 수 없다.

tt1 = (10,20,30,40)
print(tt1[0])
print(tt1[1])
print(tt1[2])
print(tt1[3])

print(tt1[:1:3])
print(tt1[1:])
print(tt1[:3])

tt2 = ('A','B')

print(tt1+tt2)
print(tt2*3)

tt3 = ((1,2,3),
       (4,5,6),
       (7,8,9))

for i in tt3:
    print(i)


# 튜플 <-> 리스트
myTuple =(10,20,30)
myList = list(myTuple)
myList.append(40)
for i in myList:
    print(i)

myTuple = tuple(myList)
for i in myTuple:
    print(i)