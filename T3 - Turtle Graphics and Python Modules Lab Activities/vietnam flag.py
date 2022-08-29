import turtle

screen = turtle.Screen()
line = turtle.Turtle()
screen.bgcolor('red')
line.left(72)
line.speed(1000)

line.pencolor('yellow')
line.fillcolor('yellow')
line.pensize(1)
line.begin_fill()

for i in range(5):
    line.forward(200)
    line.right(144)

line.end_fill()


screen.exitonclick()
