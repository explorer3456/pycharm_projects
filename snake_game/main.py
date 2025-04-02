from turtle import Turtle, Screen
import time
from snake import Snake

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.tracer(0)

snake = Snake()

is_game_done = False

while not is_game_done:
    s.update()
    snake.move(angle=-45)
    time.sleep(1.0)

s.exitonclick()
