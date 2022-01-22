import screen


class Pong:
    def __init__(self, screen_width=800, screen_height=600):
        self.court = screen.Screen(width=screen_width, height=screen_height)


if __name__ == "__main__":
    pong = Pong()
