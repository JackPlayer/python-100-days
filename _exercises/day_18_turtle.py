from turtle import Turtle, Screen
import math
import random


def random_color():
    return random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)


def draw_square(_turtle, stride):
    for _ in range(0, 3):
        _turtle.forward(stride)
        _turtle.right(90)
    _turtle.forward(stride)


def forward_dotted(_turtle, total_stride):

    _turtle.down()
    for _ in range(0, math.floor(total_stride / 5)):
        _turtle.forward(10)
        _turtle.up()
        _turtle.forward(10)
        _turtle.down()


def draw_shape(_turtle, side_length, num_sides):
    turn_angle = 360 / num_sides
    for side in range(0, num_sides):
        _turtle.forward(side_length)
        _turtle.right(turn_angle)


def draw_shapes(_turtle, side_length):
    shapes_num_sides = range(3, 11)

    for sides in shapes_num_sides:
        _turtle.color(random_color())
        draw_shape(_turtle, side_length, sides)


def random_walk(_turtle, max_stride_length, num_strides, is_square=False):
    for _ in range(num_strides):
        _turtle.color(random_color())
        rand_stride_length = random.randint(1, max_stride_length)
        rand_turn_angle = random.randint(0, 359)
        if is_square:
            rand_turn_angle = random.choice([0, 90, 180, 270])
        _turtle.forward(rand_stride_length)
        _turtle.right(rand_turn_angle)


def draw_spirograph(_turtle, circle_radius, num_circles):
    turn_amount = 360 / num_circles
    for _ in range(num_circles):
        turtle.color(random_color())
        turtle.circle(circle_radius)
        turtle.right(turn_amount)


turtle = Turtle()
screen = Screen()

turtle.shape("turtle")
turtle.color("SpringGreen3")
turtle.pensize(2)
turtle.shapesize(3, 3, 3)
turtle.speed(0)
turtle.hideturtle()
screen.setup(800, 800)

screen.colormode(255)
# draw_square(turtle, 888)
# forward_dotted(turtle, 100)
# draw_shapes(turtle, 200)
# random_walk(turtle, 50, 200, is_square=True)
draw_spirograph(turtle, 100, 20)
screen.exitonclick()
