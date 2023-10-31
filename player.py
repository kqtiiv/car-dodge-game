from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        if self.ycor() < FINISH_LINE_Y:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(0, new_y)

    def next_level(self):
        self.goto(STARTING_POSITION)

    def reached_end(self):
        return self.ycor() > FINISH_LINE_Y - 10






