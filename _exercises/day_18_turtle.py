from turtle import Turtle, Screen


def draw_square(_turtle, stride):
    for walk_idx in range(0, 3):
        _turtle.forward(stride)
        _turtle.right(90)
    _turtle.forward(stride)


turtle = Turtle()
screen = Screen()

turtle.shape('turtle')
turtle.color('SpringGreen3')
turtle.shapesize(3, 3, 3)
screen.setup(1000, 1000)
draw_square(turtle, 888)

screen.exitonclick()
