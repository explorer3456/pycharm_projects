from turtle import Turtle

class Snake():
    def __init__(self):
        self.body_list = []

        for i in range(3):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            self.body_list.append(t)

    def move(self, angle):
        for i in range(len(self.body_list)-1, -1, -1):
            new_x = self.body_list[i - 1].xcor()
            new_y = self.body_list[i - 1].ycor()

            if i > 0:
                self.body_list[i].goto(new_x, new_y)
        self.body_list[0].setheading(angle)
        self.body_list[0].forward(20)




