import turtle
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Score
import configuration as conf


class Pong:
    def __init__(
        self,
        screen_width=conf.SCREEN_WIDTH,
        screen_height=conf.SCREEN_HEIGHT,
        bg_color="black",
        title="Pong",
    ):
        self.court = turtle.Screen()
        self.court.title(title)
        self.court.bgcolor(bg_color)
        self.court.tracer(0)

        self.paddle_r = Paddle(start_x=screen_width / 2 - conf.BORDER_ADJUST)
        self.paddle_l = Paddle(start_x=-(screen_width / 2) + conf.BORDER_ADJUST)

        self.ball = Ball()
        self.score_r = Score()
        self.score_l = Score(x_pos=-(conf.SCREEN_WIDTH / 4))

        self.court.listen()
        self.court.onkey(self.paddle_r.go_up, "Up")
        self.court.onkey(self.paddle_r.go_down, "Down")
        self.court.onkey(self.paddle_l.go_up, "w")
        self.court.onkey(self.paddle_l.go_down, "s")
        self.court.setup(width=screen_width, height=screen_height)

    def play(self):
        score_l = 0
        score_r = 0
        is_game_on = True
        while is_game_on:
            time.sleep(0.01)
            self.court.update()
            self.ball.move()

            # Detect collection with a paddle
            if self.did_ball_paddle_collide():
                self.ball.reverse_horizontal_trajectory()

            # Player Scored
            if self.player_scored() == "r":
                score_r += 1
                self.score_r.add_point()
                self.reset()
            elif self.player_scored() == "l":
                score_l += 1
                self.score_l.add_point()
                self.reset()

        self.court.exitonclick()

    def reset(self):
        self.ball.setpos(0, 0)
        self.ball.prev_pos = (0, 0)

    def did_ball_paddle_collide(self):
        return (
            self.ball.ball_past_right()
            and self.ball.get_horizontal_dir() == "r"
            and self.ball.distance(self.paddle_r.xcor(), self.paddle_r.ycor())
            < conf.COLLISION_THRESHOLD
        ) or (
            self.ball.ball_past_left()
            and self.ball.get_horizontal_dir() == "l"
            and self.ball.distance(self.paddle_l.xcor(), self.paddle_l.ycor())
            < conf.COLLISION_THRESHOLD
        )

    def player_scored(self):
        curr_x = self.ball.pos()[0]
        if curr_x > conf.SCREEN_WIDTH / 2 - 10:
            return "l"
        elif curr_x < -(conf.SCREEN_WIDTH / 2) + 10:

            return "r"
        return "no"


if __name__ == "__main__":
    pong = Pong()
    pong.play()
