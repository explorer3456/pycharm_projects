from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.penup()
        self.hideturtle()
        self.shapesize(stretch_wid=1, stretch_len=2)

        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        self.goto(x, y)

        self.move_factor = 1

        self.setheading(180)
        self.showturtle()

    def reset_car(self):
        new_y = random.randint(-260, 260)
        self.goto(260, new_y)

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE + self.move_factor * MOVE_INCREMENT)
        if self.xcor() < -260:
            self.reset_car()

    def locate_car(self, x, y):
        self.goto(x, y)
