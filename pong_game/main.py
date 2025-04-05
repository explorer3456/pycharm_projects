from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
import math

is_game_done = False

field = Screen()

field.setup(width=800, height=600)
field.bgcolor("black")
field.tracer(0)
field.listen()

# initialize paddle
user_a = Paddle(350, 0)
user_b = Paddle(-350, 0)
ball = Ball()

field.onkey(fun=user_a.move_up, key="w")
field.onkey(fun=user_a.move_down, key="s")

field.onkey(fun=user_b.move_up, key="t")
field.onkey(fun=user_b.move_down, key="g")

def is_ball_hit_wall(b_obj):
    return b_obj.ycor() > 270 or b_obj.ycor() < -270

def is_ball_hit_paddle(b_obj, paddle):
    return b_obj.xcor() > 320 and b_obj.distance(paddle) < 50

while not is_game_done:
    field.update()

    ball.move()

    if is_ball_hit_wall(ball):
        ball.bounce()

    if is_ball_hit_paddle(ball, user_a) or is_ball_hit_paddle(ball, user_b):
        ball.direction *= -1
        ball.bounce()

    time.sleep(0.25)

field.exitonclick()
