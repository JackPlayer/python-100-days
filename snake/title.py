from turtle import Turtle

Y_POS = 230
FONT = ("Courier", 50, "bold")


class Title(Turtle):
    def __init__(self, text):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.sety(Y_POS)
        self.write(text, align="center", font=FONT)

    def update(self, text):
        self.clear()
        self.write(text, align="center", font=FONT)