import turtle
import configuration as conf


class Score(turtle.Turtle):
    def __init__(self, x_pos=conf.SCREEN_WIDTH / 4):
        super().__init__()
        self.setpos(x=x_pos, y=conf.SCREEN_HEIGHT / 2 - 60)

        self.color("white")
        self.write("0", font=("Arial", 16, "bold"))
        self.hideturtle()
        self.penup()
        self.points = 0

    def add_point(self):
        self.points += 1
        self.clear()
        self.write(self.points, font=("Arial", 16, "bold"))
