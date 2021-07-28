from turtle import Turtle
import random

MAX_X = 280
MAX_Y = 280


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-MAX_X, MAX_X)
        random_y = random.randint(-MAX_Y, MAX_Y)
        self.setpos(x=random_x, y=random_y)
