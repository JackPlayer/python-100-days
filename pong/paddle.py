import turtle
import configuration as conf


class Paddle(turtle.Turtle):
    def __init__(self, stretch_w=5, stretch_h=1, start_x=0, start_y=0):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=stretch_w, stretch_len=stretch_h)
        self.penup()

        self.goto(x=start_x, y=start_y)

    def go_down(self):
        curr_y = self.ycor()
        if curr_y < -(conf.SCREEN_HEIGHT / 2) + (
            conf.BORDER_ADJUST * 2
        ):  # Bottom Boundary
            return
        self.sety(curr_y - conf.MOVE_STEP)

    def go_up(self):
        curr_y = self.ycor()
        if curr_y > conf.SCREEN_HEIGHT / 2 - conf.BORDER_ADJUST * 2:  # Top Boundary
            return
        self.sety(curr_y + conf.MOVE_STEP)
