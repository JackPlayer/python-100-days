from turtle import Turtle
from scoreboard import Scoreboard

class Court(Turtle):
    def __init__(self, width, height, color="black"):
        super().__init__()
        self.score_one = Scoreboard()
        self.score_two = Scoreboard()
        self.score_one.setpos(x=-130 , y=height/2 - 30)
        self.score_two.setpos(x=40, y=height/2 - 30)
        self.score_one.set_score(0)
        self.score_two.set_score(0)
        self.penup()
        self.color(color)
        self.hideturtle()
        self.width = width
        self.height = height
        self.draw_center()

    def draw_center(self):
        self.setpos(x=0, y=self.height/2)
        self.pendown()
        self.setheading(270)
        self.forward(self.height)

