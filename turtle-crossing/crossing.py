import time
import random
from turtle import Screen
from player import Player
from level import Level
from car_manager import CarManager
from prompt import Prompt

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
INVERSE_CAR_POPULATION = 70  # Lower numbers will produce more cars
SPEED_INCREASE_FACTOR = 1.3  # The factor that the speed will increase after each level
HIT_THRESHOLD = 30


class Crossing:
    def __init__(self):
        self.level = 1
        self.screen = Screen()
        self.screen.tracer(0)
        self.player = Player(-(SCREEN_HEIGHT / 2) + 30)
        self.level = Level(
            draw_x=-(SCREEN_WIDTH / 2) + 30, draw_y=SCREEN_HEIGHT / 2 - 50
        )
        self.car_manager = CarManager(
            num_cars=1,
            start_x=SCREEN_WIDTH / 2 + 60,
            screen_height=SCREEN_HEIGHT,
            screen_width=SCREEN_WIDTH,
            speed=1,
        )
        self.prompt = Prompt()
        self.screen.listen()

        self.screen.onkey(self.player.move_up, "Up")

    def play(self):
        game_on = True
        current_speed = 1
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.mainloop()
        while game_on:
            time.sleep(0.01)
            if self.should_add_new_car():
                self.car_manager.add_car()
                print("adding new car")

            if self.is_player_at_finish():
                time.sleep(0.25)
                current_speed = current_speed * SPEED_INCREASE_FACTOR
                self.car_manager.speed_up_all(SPEED_INCREASE_FACTOR)

                self.level.next_level()
                self.prompt.show_prompt("NEXT LEVEL")

                self.player.reset()

            if self.car_manager.did_car_hit(self.player.xcor(), self.player.ycor(), HIT_THRESHOLD):
                self.prompt.show_prompt("GAME OVER")

                time.sleep(5)
                self.reset()
                self.screen.update()
                continue

            self.car_manager.cleanup()
            self.car_manager.drive_all()
            self.screen.update()
        self.screen.exitonclick()

    def is_player_at_finish(self):
        player_pos_y = self.player.ycor()
        return player_pos_y > SCREEN_HEIGHT / 2 - 20

    def should_add_new_car(self):
        return random.randint(0, INVERSE_CAR_POPULATION) == 1

    def reset(self):
        self.level.reset()
        self.car_manager.reset()
        self.player.reset()


if __name__ == "__main__":
    crossing = Crossing()
    crossing.play()
