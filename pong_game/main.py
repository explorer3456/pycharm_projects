from turtle import Screen
from paddle import Paddle


is_game_done = False

field = Screen()

field.setup(width=800, height=600)
field.bgcolor("black")
field.tracer(0)
field.listen()

# initialize paddle
user_a = Paddle(350, 0)
user_b = Paddle(-350, 0)

field.onkey(fun=user_a.move_up, key="w")
field.onkey(fun=user_a.move_down, key="s")

field.onkey(fun=user_b.move_up, key="t")
field.onkey(fun=user_b.move_down, key="g")

while not is_game_done:
    field.update()

field.exitonclick()
