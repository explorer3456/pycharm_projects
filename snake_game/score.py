from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        self.max_score = 0
        with open("data.txt", mode="r") as data:
            self.max_score = int(data.read())

        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(0, 280)
        self.color("white")
        self.write(arg=f'Score : {self.score}, Highest: {self.max_score}', align="center", font=('Arial', 12, 'normal'))

    def show_game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("")
        self.write("GAME OVER")
        if self.score > self.max_score:
            self.max_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.max_score))

    def update_score(self):
        self.score += 1

