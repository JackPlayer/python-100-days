from turtle import Turtle

STEP_SIZE = 5


class Player(Turtle):
    def __init__(self, start_y):
        super().__init__()
        self.penup()
        self.color("black")
        self.start_y = start_y
        self.setpos(0, start_y)
        self.shape("turtle")
        self.setheading(90)

    def move_up(self):
        curr_pos = self.pos()
        self.setpos(x=curr_pos[0], y=curr_pos[1] + STEP_SIZE)

    def reset(self):
        self.setpos(0, self.start_y)
