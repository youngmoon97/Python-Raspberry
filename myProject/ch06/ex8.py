import turtle

swidth, sheight = 800, 450
i, k, tx, ty = [0] * 4

if __name__ == "__main__":
    turtle.title("거북이 구구단")
    turtle.shape("turtle")
    turtle.setup(width=swidth + 50, height=sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.speed(5)
    tx, ty = -500, 250
    turtle.goto(tx, ty)

    for i in range(1, 10):
        for j in range(2, 10):
            turtle.goto(tx + 80 * j, ty - 40 * i)
            gugu = str(i) + "X " + str(j) + " = " + str(i * j)
            turtle.write(gugu, font=("Arial", 12, "bold"))

turtle.done()
