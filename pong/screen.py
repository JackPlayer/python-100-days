import turtle


class Screen:
    def __init__(self, width: int, height: int, title: str):
        self.screen = turtle.Screen()
        self.screen.setup(width=width, height=height)
        self.screen.title(title)
        self.screen.exitonclick()
