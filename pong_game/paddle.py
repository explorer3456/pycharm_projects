from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, init_x, init_y):
        super().__init__();
        self.hideturtle()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(init_x, init_y)
        self.showturtle()

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

