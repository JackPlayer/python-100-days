from turtle import Turtle

FONT = ("Courier", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self, start_score=0):
        super().__init__()
        self.score = start_score
        self.hideturtle()
        self.set_score(start_score)

    def set_score(self, score):
        self.clear()
        self.write(f"Score: {score}", move = False, font = FONT)
