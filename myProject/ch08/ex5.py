import math
import turtle
import random
from tkinter.simpledialog import *

inStr =''
swidth, sheight = 600,600
tx,ty,txtSize =[0] *3

turtle.title('거북 나선 모양의 글자 쓰기')
turtle.shape('turtle')
turtle.setup(width=swidth+50,height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()

inStr = askstring('문자열 입력 ', '거북이 쓸 문자열 입력')

dist = 200
angle = 0
value=int(360*2/len(inStr))


for ch in inStr:
    rad = 3.141592 * angle / 180
    tx = dist*math.cos(rad)
    ty = dist*math.sin(rad)
    dist -= 200/len(inStr)
    angle+=value

    r=random.random()
    g=random.random()
    b=random.random()
    txtSize = random.randrange(10,50)

    turtle.goto(tx,ty)
    turtle.pencolor(r,g,b)
    turtle.write(ch, font=("맑은 고딕",txtSize,"bold"))

turtle.done()
