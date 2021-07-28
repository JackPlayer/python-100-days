from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
score = 0


def did_collide(_food, snake_part):
    return _food.position() == snake_part.position()


if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)
    screen.bgcolor("black")
    screen.title("Snake Game")
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard(score)
    screen.listen()

    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')

    game_is_on = True
    while game_is_on:
        screen.update()
        if snake.head.distance(food) < 15.0:
            score += 1
            food.refresh()
            snake.add_length()
            scoreboard.write_score(score)
        time.sleep(0.1)
        snake.move()

    screen.exitonclick()
