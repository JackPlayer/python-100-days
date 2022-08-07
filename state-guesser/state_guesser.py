import turtle
import pandas

SCORE_FONT = ("Helvetica", 16, "bold")

class StateGuesser():
    def __init__(self):
        # Screen
        self.screen = turtle.Screen()
        self.screen.title("U.S State Game")
        image = "blank_states_img.gif"
        self.screen.addshape(image)
        turtle.shape(image)

        # Scoreboard
        self.score = 0
        self.score_turtle = turtle.Turtle(visible=False)
        self.score_turtle.speed(0)
        self.score_turtle.penup()
        self.score_turtle.color("black")
        self.score_turtle.goto(- (self.screen.window_width() / 2) + 30, self.screen.window_height() / 2 - 40)
        self.score_turtle.write(f"Current Score: {self.score}", font=SCORE_FONT)

        # State Info
        self.state_turtles = []
        self.states_correct_guessed = []
        self.state_data = pandas.read_csv("50_states.csv", index_col=False)
        self.state_data.reset_index(drop=True, inplace=True)

    def play(self):
        while self.score < 50:
            state = self._ask_for_state()
            if state is None:
                continue
            state_sanitized = state.strip().title()
            if state_sanitized in self.state_data.state.array and state_sanitized not in self.states_correct_guessed:
                self.score += 1
                self.states_correct_guessed.append(state_sanitized)
                self._draw_state(state)
                self._update_current_score()
        self.score_turtle.write("Congratulations, you won!")
        self.screen.mainloop()

    def _ask_for_state(self) -> str:
        answer = self.screen.textinput(title="States", prompt="Enter a state name: ")
        return answer

    def _draw_state(self, state):
        (x, y) = self._get_x_y_from_state(state)

        new_state_turtle: turtle.Turtle = turtle.Turtle(visible=False)
        new_state_turtle.penup()
        new_state_turtle.speed(0)
        new_state_turtle.goto(x, y)
        new_state_turtle.write(state)

        self.state_turtles.append(new_state_turtle)

    def _get_x_y_from_state(self, state: str) -> tuple[int, int]:
        state_row: pandas.DataFrame = self.state_data.loc[self.state_data["state"] == state]
        return (list(state_row["x"])[0], list(state_row["y"])[0])

    def _update_current_score(self):
        self.score_turtle.clear()
        self.score_turtle.write(f"Current Score: {self.score}", font=SCORE_FONT)

def main():
    game = StateGuesser()
    game.play()

if __name__ == "__main__":
    main()