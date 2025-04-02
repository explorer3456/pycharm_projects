from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body_list = []

        for i in range(3):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            self.body_list.append(t)

    def move(self):
        for i in range(len(self.body_list)-1, -1, -1):
            new_x = self.body_list[i - 1].xcor()
            new_y = self.body_list[i - 1].ycor()

            if i > 0:
                self.body_list[i].goto(new_x, new_y)

        self.body_list[0].forward(20)

    def up(self):
        if self.body_list[0].heading() != DOWN:
            self.body_list[0].setheading(UP)

    def down(self):
        if self.body_list[0].heading() != UP:
            self.body_list[0].setheading(DOWN)

    def left(self):
        if self.body_list[0].heading() != RIGHT:
            self.body_list[0].setheading(LEFT)

    def right(self):
        if self.body_list[0].heading() != LEFT:
            self.body_list[0].setheading(RIGHT)





