
# 딕셔너리 : key와 value쌍으로 구성

dic1 = {1:'a',2:'b',3:'c'}

print(dic1)

student1 = {'학번':1000, '이름':'홍길동','학과':'컴퓨터공학과'}
print(student1)
student1['연락처'] = ['010-8888-9999']
print(student1)
student1['학과']=['파이썬학과']
print(student1)

print(student1.get('학과'))
print(student1.get('연락처'))
print(student1.keys())

singer={}
singer['이름'] = '트와이스'
singer['구성원수']=9
singer['데뷰'] = '서바이벌 식스틴'
singer['대표곡'] = 'signal'

for k in singer.keys():
    print('%s ---> %s '% (k,singer[k]))