import turtle
import configuration as conf


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.prev_pos = (0, 0)

    def move(self):

        curr_pos = self.pos()

        new_x = curr_pos[0]
        new_y = curr_pos[1]

        # Hit the top wall
        if self.did_hit_top_wall() and self.get_horizontal_dir() == "r":
            new_x = curr_pos[0] + conf.BALL_STEP
            new_y = curr_pos[1] - conf.BALL_STEP

        elif self.did_hit_top_wall() and self.get_horizontal_dir() == "l":
            new_x = curr_pos[0] - conf.BALL_STEP
            new_y = curr_pos[1] - conf.BALL_STEP

        elif self.did_hit_bottom_wall() and self.get_horizontal_dir() == "r":
            new_x = curr_pos[0] + conf.BALL_STEP
            new_y = curr_pos[1] + conf.BALL_STEP

        elif self.did_hit_bottom_wall() and self.get_horizontal_dir() == "l":
            new_x = curr_pos[0] - conf.BALL_STEP
            new_y = curr_pos[1] + conf.BALL_STEP

        else:
            self.continue_trajectory(self.prev_pos, curr_pos)
            self.prev_pos = curr_pos
            return

        self.setpos(new_x, new_y)
        self.prev_pos = curr_pos

    def continue_trajectory(self, prev_pos, curr_pos):
        current_x = curr_pos[0]
        current_y = curr_pos[1]

        prev_x = prev_pos[0]
        prev_y = prev_pos[1]

        # Up right
        if current_x >= prev_x and current_y >= prev_y:
            self.setpos(current_x + conf.BALL_STEP, current_y + conf.BALL_STEP)

        # Down Right
        elif current_x < prev_x and current_y >= prev_y:
            self.setpos(current_x - conf.BALL_STEP, current_y + conf.BALL_STEP)

        # Down Left
        elif current_x < prev_x and current_y < prev_y:
            self.setpos(current_x - conf.BALL_STEP, current_y - conf.BALL_STEP)

        # Up Left
        else:
            self.setpos(current_x + conf.BALL_STEP, current_y - conf.BALL_STEP)

    def reverse_horizontal_trajectory(self):
        curr_pos = self.pos()
        new_x = curr_pos[0]
        new_y = curr_pos[1]

        if self.get_horizontal_dir() == "r":
            new_x = curr_pos[0] - conf.BALL_STEP
        else:
            new_x = curr_pos[0] + conf.BALL_STEP

        if self.get_vertical_dir() == "u":
            new_y = curr_pos[1] + conf.BALL_STEP
        else:
            new_y = curr_pos[1] - conf.BALL_STEP

        self.setpos(new_x, new_y)
        self.prev_pos = curr_pos

    def did_hit_top_wall(self):
        curr_y = self.ycor()

        return curr_y >= conf.SCREEN_HEIGHT / 2 - conf.BORDER_ADJUST

    def did_hit_bottom_wall(self):
        curr_y = self.ycor()

        return curr_y <= -(conf.SCREEN_HEIGHT / 2) + conf.BORDER_ADJUST

    def get_horizontal_dir(self):
        curr_x = self.xcor()
        prev_x = self.prev_pos[0]

        if curr_x >= prev_x:
            return "r"
        return "l"

    def get_vertical_dir(self):
        curr_y = self.ycor()
        prev_y = self.prev_pos[1]

        if curr_y >= prev_y:
            return "u"
        return "d"

    def ball_past_right(self):
        curr_x = self.pos()[0]

        return curr_x > conf.SCREEN_WIDTH / 2 - conf.BORDER_ADJUST - 30

    def ball_past_left(self):
        curr_x = self.pos()[0]

        return curr_x < -(conf.SCREEN_WIDTH / 2) + conf.BORDER_ADJUST + 30
