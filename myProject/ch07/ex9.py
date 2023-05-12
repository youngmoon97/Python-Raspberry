# ex9.py

import turtle
import random

myTurtle, tx, ty, tColor, tSize, tShape = [None] * 6
shapeList = []
playserTurtle = []
swidth, sheight = 500, 500

if __name__ == "__main__":
    turtle.title("거북 리스트 활용")
    turtle.setup(width=swidth+50, height=sheight+50)
    turtle.screensize(swidth, sheight)
    shapeList = turtle.getshapes()
  #  print(shapeList)
    for i in range(1, 100):
        random.shuffle(shapeList) #리스트 섞기
        myTurtle = turtle.Turtle(shapeList[0])
         # print(shapeList[0])
        tx = random.randint(-swidth // 2, swidth // 2)
        ty = random.randint(-sheight // 2, sheight // 2)

        r = random.random(); g = random.random(); b = random.random();
        tSize = random.randrange(1, 3)
        playserTurtle.append([myTurtle, tx, ty, tSize, r, g, b])

    for tList in playserTurtle:
        myTurtle = tList[0]
        myTurtle.color(tList[4], tList[5], tList[6])
        myTurtle.pencolor(tList[4], tList[5], tList[6])
        myTurtle.turtlesize(tList[3])
        myTurtle.goto(tList[1], tList[2])

    print(playserTurtle)

    turtle.done();