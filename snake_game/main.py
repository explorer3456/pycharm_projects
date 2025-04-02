from turtle import Turtle, Screen
import time
from snake import Snake


snake = Snake()

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.tracer(0)
s.listen()

s.onkey(fun=snake.up, key="w")
s.onkey(fun=snake.down, key="s")
s.onkey(fun=snake.left, key="a")
s.onkey(fun=snake.right, key="d")


is_game_done = False

while not is_game_done:
    s.update()
    snake.move()
    time.sleep(0.1)

s.exitonclick()
