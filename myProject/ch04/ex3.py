
import turtle
import random

swidth, sheigth, pSize, exitCount = 300,300,3,0

turtle.title("거북이가 맘대로 다니기")
turtle.shape("turtle")
turtle.pensize(pSize)
turtle.setup(width=swidth+30, height=sheigth+30)
turtle.screensize(swidth,sheigth)
turtle.color('orange')
turtle.bgcolor('pink')
turtle.speed(2)

while True:
    # 랜덤생상
    r=random.random()
    g=random.random()
    b=random.random()
    turtle.pencolor(r,g,b)
    # 랜덤 각도, 거리
    angle = random.randrange(0,360)
    dist = random.randrange(1,100)

    turtle.left(angle)
    turtle.forward(dist)
    curX = turtle.xcor()
    curY = turtle.ycor()

    if(-swidth/2<=curX and curX<=swidth/2) and \
        (-sheigth/2<=curY and curY<=sheigth/2):
        pass
    else:
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()

turtle.done()