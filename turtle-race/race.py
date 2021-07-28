from turtle import Turtle, Screen
import random

screen = Screen()
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


def initialize_turtles():
    turtles = []
    for color in COLORS:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        turtles.append(new_turtle)

    return turtles


def move_to_start(turtles):
    vertical_spacing = 40
    lowest_y = -150
    x_position = -230
    for index, turtle in enumerate(turtles):
        turtle.penup()
        turtle.goto(x_position, lowest_y + (index + 1) * vertical_spacing)


def finished_race(racer):
    finish_line = screen.screensize()[0] - 200
    current_position = racer.position()[0]

    return current_position >= finish_line


def race(racers, max_stride):
    while True:
        for racer in racers:
            racer.forward(random.randint(1, max_stride))
            if finished_race(racer):
                return racer


if __name__ == '__main__':
    screen.setup(width=500, height=400)

    race_entrants = initialize_turtles()
    move_to_start(race_entrants)
    bet = screen.textinput(title="Place your bet", prompt="Which turtle will win?")

    winner = race(racers=race_entrants, max_stride=30)
    if winner.color() == bet:
        print(f'You win! The {winner.color()[0]} turtle won!')
    print(f'You lost. The {winner.color()[0]} turtle won!')

    screen.exitonclick()
