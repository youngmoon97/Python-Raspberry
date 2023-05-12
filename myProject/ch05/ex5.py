import turtle

swidth, sheight = 500,500

turtle.title("무지개색 원그리기")
turtle.shape("turtle")
turtle.setup(width=swidth+50,height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()
turtle.goto(0,-sheight/2)
turtle.pendown()
turtle.speed(10)