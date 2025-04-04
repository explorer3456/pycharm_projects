from turtle import Screen
from paddle import Paddle

field = Screen()

field.setup(width=800, height=600)
field.bgcolor("black")



user_a = Paddle(350, 0)
user_b = Paddle(-350, 0)


field.exitonclick()
