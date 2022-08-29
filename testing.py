import turtle


def move(a):
    line.up()
    line.right(a)
    line.forward(100)
    line.down()


window = turtle.Screen()
line = turtle.Turtle()

for i in range(3):
    line.forward(200)
    line.right(120)

move(180)

for i in range(4):
    line.forward(200)
    line.left(90)

move(90)

for i in range(6):
    line.forward(100)
    line.left(60)

move(90)

for i in range(8):
    line.forward(100)
    line.left(45)

window.exitonclick()
