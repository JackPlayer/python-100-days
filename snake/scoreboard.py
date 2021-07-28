from turtle import Turtle

X_POS = 200
Y_POS = 270
FONT = ("Arial", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self, score):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(x=X_POS, y=Y_POS)
        self.color("white")
        self.write_score(score)

    def write_score(self, score):
        self.clear()
        self.write(f"Score: {score}", move=False, font=FONT)
