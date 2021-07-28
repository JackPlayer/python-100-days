from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.parts = []
        for part in range(0, 3):
            body_part = Turtle(shape="square")
            body_part.penup()
            body_part.color("white")
            body_part.setx(-20 * part)

            self.parts.append(body_part)
        self.head = self.parts[0]

    def move(self):
        reversed_snake = list(reversed(self.parts))
        for index in range(len(reversed_snake)):

            is_front_part = (index == len(reversed_snake) - 1)

            if is_front_part:
                reversed_snake[index].forward(MOVE_DISTANCE)
            else:
                part_in_front = reversed_snake[index + 1]
                reversed_snake[index].goto(part_in_front.position())

    def left(self):
        front_part = self.parts[0]
        if front_part.heading() != 0:
            front_part.setheading(180)

    def right(self):
        front_part = self.parts[0]
        if front_part.heading() != 180:
            front_part.setheading(0)

    def up(self):
        front_part = self.parts[0]
        if front_part.heading() != 270:
            front_part.setheading(90)

    def down(self):
        front_part = self.parts[0]
        if front_part.heading() != 90:
            front_part.setheading(270)

    def add_length(self):
        tail = self.parts[len(self.parts) - 1]
        body_part = Turtle(shape="square")
        body_part.penup()
        body_part.color("white")

        if tail.heading() == 0:
            body_part.sety(tail.ycor())
            body_part.setx(tail.xcor() - 20)

        elif tail.heading() == 90:
            body_part.sety(tail.ycor() - 20)
            body_part.setx(tail.xcor())

        elif tail.heading == 180:
            body_part.sety(tail.ycor())
            body_part.setx(tail.xcor() + 20)

        elif tail.heading == 270:
            body_part.sety(tail.ycor() + 20)
            body_part.setx(tail.xcor())
        self.parts.append(body_part)
