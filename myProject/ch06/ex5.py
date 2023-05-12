
i, sum = 0,0

i=1
while i<11:
    sum+=i
    i+=1
print("1부터 10까지의 합은 %d" %sum)

sum = 0
a,b=0,0

while True:
    a=int(input("더 할 첫번째 수를 입력하세요 : "))
    b=int(input("더 할 두번째 수를 입력하세요 : "))
    sum=a+b
    print("%d + %d = %d" %(a,b,sum))