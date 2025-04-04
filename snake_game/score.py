from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        self.write(arg=f'Score : {self.score}', align="center", font=('Arial', 12, 'normal'))


    def update_score(self):
        self.score += 1
        self.write(arg=f'Score : {self.score}', align="center", font=('Arial', 12, 'normal'))
