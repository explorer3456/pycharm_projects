from turtle import Turtle
import math

DIRECTION_LEFT = 1
DIRECTION_RIGHT = -1
STEP_SIZE = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__();
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        self.direction = DIRECTION_LEFT
        self.setheading(45)

    def bounce(self):
        self.setheading(360 - self.heading())

    def move(self):
        new_x = self.xcor() + (self.direction * STEP_SIZE)
        new_y = self.ycor() + (self.direction * math.tan(math.radians(self.heading())) * STEP_SIZE)
        self.goto(new_x, new_y)

    def reset_ball(self):
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()




