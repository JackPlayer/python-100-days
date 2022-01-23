from turtle import Turtle
import random

CAR_COLORS = ["dark slate gray", "light sky blue", "tomato", "sea green", "violet"]

DRIVE_STEP = 1


class Car(Turtle):
    def __init__(self, start_x, start_y, start_speed):
        super().__init__()
        self.color(random.choice(CAR_COLORS))
        self.penup()
        self.speed = start_speed
        self.setpos(x=start_x, y=start_y)
        self.setheading(180)
        self.shape("square")
        self.shapesize(1, 3)

    def drive(self):
        self.forward(DRIVE_STEP * self.speed)

    def speed_up(self, factor=1.1):
        self.speed *= factor
