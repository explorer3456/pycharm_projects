from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.level = 0
        self.hideturtle()
        self.goto(-260, 260)
        self.write(arg=f'Level:{self.level}', align="left", font=FONT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.write(arg=f'Level:{self.level}', align="left", font=FONT)
