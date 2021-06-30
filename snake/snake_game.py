from turtle import Screen
from snake import Snake
import time

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)
    screen.bgcolor("black")
    screen.title("Snake Game")
    snake = Snake()
    screen.listen()

    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.05)
        snake.move()

    screen.exitonclick()
