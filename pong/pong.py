from turtle import Screen
from court import Court
from paddle import Paddle
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = Screen()

def initialize_game():
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    court = Court(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

def pong():
    initialize_game()
    opponent = Paddle(start_x = -SCREEN_WIDTH / 2 + 40, start_y = 0, screen_height=SCREEN_HEIGHT)
    player = Paddle(start_x = SCREEN_WIDTH / 2 - 40, start_y = 0, screen_height=SCREEN_HEIGHT)
    screen.listen()
    screen.onkey(player.up, "Up")
    screen.onkey(player.down, "Down")

    game_is_on = True

    screen.exitonclick()

if __name__ == "__main__":
    pong()