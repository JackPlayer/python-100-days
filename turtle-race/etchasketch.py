from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def reset_position():
    turtle.setpos(0, 0)
    turtle.clear()
    turtle.setheading(0)


def turn_left():
    turtle.left(5)


def turn_right():
    turtle.right(5)


def go_forward():
    turtle.forward(10)


def go_backward():
    turtle.backward(10)


def main():
    screen.listen()

    screen.onkey(key='w', fun=go_forward)
    screen.onkey(key='s', fun=go_backward)
    screen.onkey(key='d', fun=turn_right)
    screen.onkey(key='a', fun=turn_left)
    screen.onkey(key='c', fun=reset_position)
    screen.exitonclick()


if __name__ == '__main__':
    main()
