from turtle import Turtle

MARGIN = 30
MOVE_LENGTH = 20
class Paddle(Turtle):
    def __init__(self, start_x, start_y, screen_height):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=4)
        self.color("black")
        self.setpos(x=start_x, y=start_y)
        self.bounds = screen_height / 2 - MARGIN

    def up(self):
        curr_pos = self.pos()
        if self.bounds > curr_pos[1] + MARGIN:
            self.setpos(x=curr_pos[0], y=curr_pos[1] + MOVE_LENGTH)

    def down(self):
        curr_pos = self.pos()
        if -self.bounds < curr_pos[1] - MARGIN:
            self.setpos(x=curr_pos[0], y=curr_pos[1] - MOVE_LENGTH)