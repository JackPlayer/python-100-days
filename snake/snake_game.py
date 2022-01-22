from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from title import Title
import time

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
score = 0


def did_hit_wall(snake_head):
    margin_px = 5
    snake_head_pos_x = snake_head.xcor()
    snake_head_pos_y = snake_head.ycor()

    hit_right_wall = snake_head_pos_x > SCREEN_WIDTH / 2 - margin_px
    hit_left_wall = snake_head_pos_x < -SCREEN_WIDTH / 2 + margin_px
    hit_top_wall = snake_head_pos_y > SCREEN_HEIGHT / 2 - margin_px
    hit_bottom_wall = snake_head_pos_y < -SCREEN_HEIGHT / 2 + margin_px
    return hit_bottom_wall or hit_left_wall or hit_right_wall or hit_top_wall


def did_hit_self(_snake):
    snake_head_pos_x = _snake.head.xcor()
    snake_head_pos_y = _snake.head.ycor()

    for body_part_idx in range(1, len(_snake.parts)):
        body_part = _snake.parts[body_part_idx]
        body_part_pos_x = body_part.xcor()
        body_part_pos_y = body_part.ycor()
        if body_part_pos_x == snake_head_pos_x and body_part_pos_y == snake_head_pos_y:
            return True
    return False


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)
    screen.bgcolor("black")
    screen.title("Snake Game")
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard(score)
    title = Title("Snake")
    screen.listen()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        if did_hit_wall(snake.head) or did_hit_self(snake):
            title.update("Game Over")
            break
        screen.update()
        if snake.head.distance(food) < 15.0:
            score += 1
            food.refresh()
            snake.add_length()
            scoreboard.write_score(score)
        time.sleep(0.025)
        snake.move()

    screen.exitonclick()
