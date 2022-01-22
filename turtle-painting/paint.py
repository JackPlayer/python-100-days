from turtle import Turtle, Screen
import random

DOT_SIZE = 20
SPACING = 50
GRID_SIZE = 10
COLOR_LIST = [
    (25, 18, 23),
    (206, 152, 98),
    (197, 216, 228),
    (228, 226, 208),
    (129, 161, 184),
    (222, 214, 110),
    (202, 226, 213),
]


def draw_painting(_turtle, start_x, start_y):
    _turtle.penup()
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            _turtle.dot(DOT_SIZE, random.choice(COLOR_LIST))
            _turtle.forward(SPACING)
        _turtle.goto(start_x, start_y + (row + 1) * SPACING)


def move_to_start(_turtle):
    _turtle.penup()
    _turtle.setheading(250)
    _turtle.forward(550)
    _turtle.setheading(0)


turtle = Turtle()
screen = Screen()
screen.setup(1000, 1000)
screen.colormode(255)

turtle.speed(0)
turtle.hideturtle()
turtle.shapesize(5)
move_to_start(turtle)
start_pos = turtle.position()
draw_painting(turtle, start_pos[0], start_pos[1])

screen.exitonclick()
