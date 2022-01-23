from turtle import Turtle
import time

FONT = ("Arial", 13, "bold")


class Prompt(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.setpos(-110, 0)

    def show_prompt(self, prompt):
        self.write(f"{prompt}", font=FONT)
        time.sleep(1)
        self.clear()
