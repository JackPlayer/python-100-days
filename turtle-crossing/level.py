from turtle import Turtle

FONT = ("Arial", 10, "bold")


class Level(Turtle):
    def __init__(self, draw_x, draw_y):
        super().__init__()
        self.penup()
        self.current_level = 1
        self.hideturtle()
        self.color("black")
        self.setpos(x=draw_x, y=draw_y)
        self.write(f"Level:  {self.current_level}", font=FONT)

    def next_level(self):
        self.clear()
        self.current_level += 1
        self.write(f"Level:  {self.current_level}", font=FONT)

    def reset(self):
        self.clear()
        self.current_level = 1
        self.write(f"Level:  {self.current_level}", font=FONT)
