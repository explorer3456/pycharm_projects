from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=f'{self.left_score}', align="center", font =("Arial", 80, "normal"))
        self.goto(100, 200)
        self.write(arg=f'{self.right_score}', align="center", font =("Arial", 80, "normal"))



